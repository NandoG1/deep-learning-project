import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, Subset
import numpy as np
import os

def get_data_loaders(config):
    data_dir = config['project']['data_dir']
    img_size = config['data']['img_size']
    batch_size = config['data']['batch_size']
    max_images = config['data']['max_images_per_class']
    num_workers = config['data']['num_workers']

    train_transforms = transforms.Compose([
        transforms.RandomResizedCrop(img_size),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(15),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    val_test_transforms = transforms.Compose([
        transforms.Resize(img_size),
        transforms.CenterCrop(img_size),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    dataset_full = datasets.ImageFolder(data_dir)
    class_names = dataset_full.classes
    num_classes = len(class_names)

    indices_per_class = {i: [] for i in range(num_classes)}
    all_limited_indices = []

    for idx, label in enumerate(dataset_full.targets):
        if len(indices_per_class[label]) < max_images:
            indices_per_class[label].append(idx)
            all_limited_indices.append(idx)

    total_limited_data = len(all_limited_indices)

    np.random.shuffle(all_limited_indices)
    
    train_split = config['data']['train_split']
    val_split = config['data']['val_split']

    train_count = int(train_split * total_limited_data)
    val_count = int(val_split * total_limited_data)

    train_idx = all_limited_indices[:train_count]
    val_idx = all_limited_indices[train_count : train_count + val_count]
    test_idx = all_limited_indices[train_count + val_count :]

    dataset_aug = datasets.ImageFolder(data_dir, transform=train_transforms)
    dataset_clean = datasets.ImageFolder(data_dir, transform=val_test_transforms)

    train_dataset = Subset(dataset_aug, train_idx)
    val_dataset   = Subset(dataset_clean, val_idx)
    test_dataset  = Subset(dataset_clean, test_idx)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=num_workers, pin_memory=True)
    val_loader   = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers, pin_memory=True)
    test_loader  = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers, pin_memory=True)

    train_targets = [dataset_full.targets[i] for i in train_idx]
    class_counts = np.bincount(train_targets, minlength=num_classes)
    class_counts = np.where(class_counts == 0, 1, class_counts)
    
    class_weights = len(train_targets) / (num_classes * class_counts)
    class_weights_tensor = torch.tensor(class_weights, dtype=torch.float)

    return train_loader, val_loader, test_loader, class_weights_tensor, class_names