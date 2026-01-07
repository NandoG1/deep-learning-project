# Plant Disease Dataset

This directory contains the dataset used for training and evaluating the plant disease detection model. The dataset is organized into two main folders: **raw** and **proc** (processed).

## Dataset Overview

- **Total Classes:** More than 35 plant disease and healthy conditions
- **Dataset Source:** [PlantVillage Dataset on Kaggle](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset)
- **Image Format:** JPG/JPEG
- **Plant Types:** Apple, Blueberry, Cherry, Corn, Grape, Orange, Peach, Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, Tomato

---

## Directory Structure

```
data/
├── raw/                          # Raw dataset (original images)
│   ├── Apple___Apple_scab/       # ~100 images per class
│   ├── Apple___Black_rot/
│   ├── Apple___Cedar_apple_rust/
│   ├── Apple___healthy/
│   ├── Blueberry___healthy/
│   ├── Cherry_(including_sour)___healthy/
│   ├── Cherry_(including_sour)___Powdery_mildew/
│   ├── Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot/
│   ├── Corn_(maize)___Common_rust_/
│   ├── Corn_(maize)___healthy/
│   ├── Corn_(maize)___Northern_Leaf_Blight/
│   ├── Grape___Black_rot/
│   ├── Grape___Esca_(Black_Measles)/
│   ├── Grape___healthy/
│   ├── Grape___Leaf_blight_(Isariopsis_Leaf_Spot)/
│   ├── Orange___Haunglongbing_(Citrus_greening)/
│   ├── Peach___Bacterial_spot/
│   ├── Peach___healthy/
│   ├── Pepper,_bell___Bacterial_spot/
│   ├── Pepper,_bell___healthy/
│   ├── Potato___Early_blight/
│   ├── Potato___healthy/
│   ├── Potato___Late_blight/
│   ├── Raspberry___healthy/
│   ├── Soybean___healthy/
│   ├── Squash___Powdery_mildew/
│   ├── Strawberry___healthy/
│   ├── Strawberry___Leaf_scorch/
│   ├── Tomato___Bacterial_spot/
│   ├── Tomato___Early_blight/
│   ├── Tomato___healthy/
│   ├── Tomato___Late_blight/
│   ├── Tomato___Leaf_Mold/
│   ├── Tomato___Septoria_leaf_spot/
│   ├── Tomato___Spider_mites Two-spotted_spider_mite/
│   ├── Tomato___Target_Spot/
│   ├── Tomato___Tomato_mosaic_virus/
│   └── Tomato___Tomato_Yellow_Leaf_Curl_Virus/
│
└── proc/                         # Processed dataset (split for training)
    ├── train/                    # Training set (~70% of data)
    │   ├── Apple___Apple_scab/   # ~50 images per class
    │   ├── Apple___Black_rot/
    │   ├── ... (all 38 classes)
    │   └── Tomato___Tomato_Yellow_Leaf_Curl_Virus/
    │
    ├── val/                      # Validation set (~15% of data)
    │   ├── Apple___Apple_scab/
    │   ├── Apple___Black_rot/
    │   ├── ... (all 38 classes)
    │   └── Tomato___Tomato_Yellow_Leaf_Curl_Virus/
    │
    └── test/                     # Test set (~15% of data)
        ├── Apple___Apple_scab/
        ├── Apple___Black_rot/
        ├── ... (all 38 classes)
        └── Tomato___Tomato_Yellow_Leaf_Curl_Virus/
```

## Folder Descriptions

### 📁 `raw/` - Raw Dataset

**Purpose:** Contains the original, unprocessed images directly from the source dataset.


### 📁 `proc/` - Processed Dataset

**Purpose:** Contains preprocessed and split data ready for model training, validation, and testing.

#### Subdirectories:

**`train/`** - Training Set
- Used to train the model
- Model learns patterns and features from this data
- Largest subset (~70% of processed data)

**`val/`** - Validation Set
- Used to tune hyperparameters and monitor training
- Helps prevent overfitting
- Not used for final model evaluation (~15% of processed data)

**`test/`** - Test Set
- Used for final model evaluation
- Provides unbiased performance metrics
- Never seen during training (~15% of processed data)

## Class Categories

### 🍎 Apple (4 classes)
- Apple___Apple_scab
- Apple___Black_rot
- Apple___Cedar_apple_rust
- Apple___healthy

### 🫐 Blueberry (1 class)
- Blueberry___healthy

### 🍒 Cherry (2 classes)
- Cherry_(including_sour)___healthy
- Cherry_(including_sour)___Powdery_mildew

### 🌽 Corn/Maize (4 classes)
- Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot
- Corn_(maize)___Common_rust_
- Corn_(maize)___Northern_Leaf_Blight
- Corn_(maize)___healthy

### 🍇 Grape (4 classes)
- Grape___Black_rot
- Grape___Esca_(Black_Measles)
- Grape___Leaf_blight_(Isariopsis_Leaf_Spot)
- Grape___healthy

### 🍊 Orange (1 class)
- Orange___Haunglongbing_(Citrus_greening)

### 🍑 Peach (2 classes)
- Peach___Bacterial_spot
- Peach___healthy

### 🌶️ Pepper/Bell (2 classes)
- Pepper,_bell___Bacterial_spot
- Pepper,_bell___healthy

### 🥔 Potato (3 classes)
- Potato___Early_blight
- Potato___Late_blight
- Potato___healthy

### 🫐 Raspberry (1 class)
- Raspberry___healthy

### 🌱 Soybean (1 class)
- Soybean___healthy

### 🎃 Squash (1 class)
- Squash___Powdery_mildew

### 🍓 Strawberry (2 classes)
- Strawberry___healthy
- Strawberry___Leaf_scorch

### 🍅 Tomato (10 classes)
- Tomato___Bacterial_spot
- Tomato___Early_blight
- Tomato___healthy
- Tomato___Late_blight
- Tomato___Leaf_Mold
- Tomato___Septoria_leaf_spot
- Tomato___Spider_mites Two-spotted_spider_mite
- Tomato___Target_Spot
- Tomato___Tomato_mosaic_virus
- Tomato___Tomato_Yellow_Leaf_Curl_Virus

## Dataset Source & Download

### Original Dataset
The full PlantVillage dataset is available on Kaggle:

**🔗 [PlantVillage Dataset on Kaggle](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset)**

### Dataset Information
- **Name:** PlantVillage Disease Classification
- **Total Images:** 54,000+ images
- **Classes:** 38 different classes
- **Image Size:** Variable (typically 256×256)
- **License:** Open for academic and research purposes

### How to Download Full Dataset

1. **Manual Download:**
   - Visit the [Kaggle dataset page](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset)
   - Click "Download" button
   - Extract to `data/raw/` directory


## Data Augmentation

During training, the following augmentations may be applied (defined in training scripts):

- Random horizontal flip
- Random rotation (±15 degrees)
- Color jitter (brightness, contrast, saturation)
- Random resized crop
- Normalization

## License

The PlantVillage dataset is available for academic and research purposes. Please refer to the original dataset page on Kaggle for detailed license information.