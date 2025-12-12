import torch.nn as nn
from torchvision import models

def build_model(num_classes, pretrained=True):
    weights = 'IMAGENET1K_V1' if pretrained else None
    model = models.efficientnet_b0(weights=weights)

    for param in model.features.parameters():
        param.requires_grad = False

    in_features = model.classifier[1].in_features
    model.classifier = nn.Sequential(
        nn.Dropout(0.5),
        nn.Linear(in_features, num_classes)
    )

    return model