# src/evaluate.py
import torch
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.metrics import classification_report, confusion_matrix

from src.utils import load_config
from src.data_loader import get_data_loaders
from src.model import build_model

def evaluate():
    config = load_config("config/config.yaml")
    device = torch.device(config['training']['device'] if torch.cuda.is_available() else "cpu")
    
    PROJECT_DIR = config['project']['project_dir']
    CHECKPOINT_DIR = os.path.join(PROJECT_DIR, config['project']['checkpoint_dir'])
    BEST_MODEL_PATH = os.path.join(CHECKPOINT_DIR, 'best_model.pth')

    _, _, test_loader, _, class_names = get_data_loaders(config)

    model = build_model(num_classes=len(class_names))
    
    if os.path.exists(BEST_MODEL_PATH):
        print(f"Loading best model from: {BEST_MODEL_PATH}")
        model.load_state_dict(torch.load(BEST_MODEL_PATH, map_location=device))
    else:
        print("Best model not found!")
        return

    model = model.to(device)
    model.eval()

    y_true = []
    y_pred = []

    with torch.no_grad():
        for images, labels in test_loader:
            images = images.to(device)
            labels = labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)

            y_true.extend(labels.cpu().numpy())
            y_pred.extend(predicted.cpu().numpy())

    print("\nClassification Report:")
    print(classification_report(y_true, y_pred, target_names=class_names))

    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(12, 10))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title('Confusion Matrix (Test Set)')
    plt.show()

if __name__ == "__main__":
    evaluate()