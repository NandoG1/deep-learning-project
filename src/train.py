import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.tensorboard import SummaryWriter
import os
import time
import argparse

# Import modules sendiri
from src.utils import load_config, seed_everything, plot_history
from src.data_loader import get_data_loaders
from src.model import build_model

def train_engine(model, train_loader, val_loader, criterion, optimizer, num_epochs, device, 
                 log_dir, checkpoint_path, best_model_path, start_epoch=0, resume_history=None):
    
    os.makedirs(log_dir, exist_ok=True)
    writer = SummaryWriter(log_dir)
    
    if resume_history:
        history = resume_history
    else:
        history = {'train_loss': [], 'val_loss': [], 'train_acc': [], 'val_acc': []}

    best_acc = 0.0
    if resume_history and len(resume_history['val_acc']) > 0:
         best_acc = max(resume_history['val_acc'])


    for epoch in range(start_epoch, num_epochs):
        print(f"\nEpoch {epoch+1}/{num_epochs}")
        
        # --- TRAIN ---
        model.train()
        running_loss, correct, total = 0.0, 0, 0
        
        for batch_idx, (images, labels) in enumerate(train_loader):
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

            if (batch_idx + 1) % 10 == 0:
                print(f"\rBatch {batch_idx+1}/{len(train_loader)} | Loss: {loss.item():.4f}", end="")

        epoch_train_loss = running_loss / len(train_loader)
        epoch_train_acc = 100 * correct / total

        # --- VAL ---
        model.eval()
        val_loss_accum, val_correct, val_total = 0.0, 0, 0

        with torch.no_grad():
            for images, labels in val_loader:
                images, labels = images.to(device), labels.to(device)
                outputs = model(images)
                loss = criterion(outputs, labels)
                val_loss_accum += loss.item()
                _, predicted = torch.max(outputs, 1)
                val_total += labels.size(0)
                val_correct += (predicted == labels).sum().item()

        epoch_val_loss = val_loss_accum / len(val_loader)
        epoch_val_acc = 100 * val_correct / val_total

        # --- LOGGING ---
        history['train_loss'].append(epoch_train_loss)
        history['val_loss'].append(epoch_val_loss)
        history['train_acc'].append(epoch_train_acc)
        history['val_acc'].append(epoch_val_acc)

        writer.add_scalar('Loss/train', epoch_train_loss, epoch)
        writer.add_scalar('Loss/val', epoch_val_loss, epoch)
        writer.add_scalar('Accuracy/train', epoch_train_acc, epoch)
        writer.add_scalar('Accuracy/val', epoch_val_acc, epoch)

        print(f"\n   -> Train Loss: {epoch_train_loss:.4f} Acc: {epoch_train_acc:.2f}%")
        print(f"   -> Val   Loss: {epoch_val_loss:.4f} Acc: {epoch_val_acc:.2f}%")

        # --- SAVE CHECKPOINT ---
        checkpoint = {
            'epoch': epoch + 1,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'history': history,
            'best_acc': best_acc
        }
        torch.save(checkpoint, checkpoint_path)

        if epoch_val_acc > best_acc:
            best_acc = epoch_val_acc
            torch.save(model.state_dict(), best_model_path)

    writer.close()
    return history

if __name__ == "__main__":
    config = load_config("config/config.yaml")
    seed_everything(config['training']['seed'])
    
    device = torch.device(config['training']['device'] if torch.cuda.is_available() else "cpu")

    PROJECT_DIR = config['project']['project_dir']
    LOG_DIR = os.path.join(PROJECT_DIR, config['project']['log_dir'], config['project']['experiment_name'])
    CHECKPOINT_DIR = os.path.join(PROJECT_DIR, config['project']['checkpoint_dir'])
    os.makedirs(CHECKPOINT_DIR, exist_ok=True)

    CHECKPOINT_PATH = os.path.join(CHECKPOINT_DIR, 'last_checkpoint.pth')
    BEST_MODEL_PATH = os.path.join(CHECKPOINT_DIR, 'best_model.pth')

    train_loader, val_loader, test_loader, class_weights, class_names = get_data_loaders(config)

    model = build_model(num_classes=len(class_names))
    model = model.to(device)

    criterion = nn.CrossEntropyLoss(weight=class_weights.to(device))
    optimizer = optim.Adam(model.parameters(), lr=config['training']['learning_rate'])

    start_epoch = 0
    resume_history = None
    if os.path.exists(CHECKPOINT_PATH):
        print(f"Loading checkpoint from {CHECKPOINT_PATH}")
        checkpoint = torch.load(CHECKPOINT_PATH)
        model.load_state_dict(checkpoint['model_state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        start_epoch = checkpoint['epoch']
        resume_history = checkpoint['history']

    history = train_engine(
        model, train_loader, val_loader, criterion, optimizer, 
        config['training']['epochs'], device, LOG_DIR, CHECKPOINT_PATH, BEST_MODEL_PATH,
        start_epoch, resume_history
    )

    plot_history(history)