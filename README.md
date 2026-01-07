# 🌿 Plant Disease Detection System

A comprehensive deep learning-based plant disease detection system that uses EfficientNet-B0 to identify more than 35 different plant diseases and healthy conditions. The system includes both a RESTful API backend and an interactive web interface, powered by PyTorch and enhanced with AI treatment recommendations.

## Overview

This project provides an end to end solution for detecting plant diseases from leaf images. It leverages state of the art deep learning techniques to help farmers, agricultural researchers, and plant enthusiasts quickly identify plant health issues and receive actionable treatment recommendations.

**Key Highlights:**
- **More Than 35 Plant Disease Classes** - Covering Apple, Tomato, Grape, Potato, Corn, and more
- **86% Accuracy** - High-performance EfficientNet-B0 model
- **AI Recommendations** - Powered by Google Gemini for personalized treatment advice
- **Dual Interface** - REST API and Web UI for flexible integration
- **Production Ready** - Deployable on cloud platforms

---

## Project Structure

```
DL/
│
├── app/                          # Application layer
│   ├── app.py                    # Streamlit web interface
│   ├── model_loader.py           # Flask REST API backend
│   ├── requirements.txt          # App-specific dependencies
│   └── README.md                 # Application documentation
│
├── config/                       # Configuration files
│   └── config.yaml               # Model and training configuration
│
├── data/                         # Dataset directory
│   ├── raw/                      # Raw dataset (~100 images/class)
│   │   ├── Apple___Apple_scab/
│   │   ├── Tomato___healthy/
│   │   └── ... (38 classes)
│   ├── proc/                     # Processed dataset (~50 images/class)
│   │   ├── train/                # Training set (70%)
│   │   ├── val/                  # Validation set (15%)
│   │   └── test/                 # Test set (15%)
│   └── README.md                 # Dataset documentation
│
├── notebooks/                    # Jupyter notebooks
│   ├── exploration.ipynb         # Data exploration and visualization
│   └── experiments.ipynb         # Model experiments and prototyping
│
├── outputs/                      # Training outputs
│   ├── models/                   # Saved model checkpoints
│   │   └── plant_disease_model.pth
│   ├── logs/                     # TensorBoard event files
│   └── plots/                    # Training plots and visualizations
│
├── report/                       # Project reports and documentation
│
├── src/                          # Source code
│   ├── __init__.py
│   ├── data_loader.py            # Data loading and preprocessing
│   ├── model.py                  # Model architecture definition
│   ├── train.py                  # Training script
│   ├── evaluate.py               # Evaluation script
│   └── utils.py                  # Utility functions
│
├── requirements.txt              # Project dependencies
├── LICENSE                       # License file
└── README.md                     # This file
```

---

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- CUDA-capable GPU (optional, for faster training)
- Google Gemini API key (for AI recommendations)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/plant-disease-detection.git
cd plant-disease-detection
```

### Step 2: Create Virtual Environment (Recommended)

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

**Windows PowerShell:**
```powershell
$env:GEMINI_API_KEY="your_gemini_api_key_here"
```

**Linux/Mac:**
```bash
export GEMINI_API_KEY="your_gemini_api_key_here"
```

### Step 5: Download Dataset

Download the PlantVillage dataset from Kaggle:

Download manually from [Kaggle PlantVillage Dataset](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset)

---

## How to Run

### 1: Web Application (Streamlit)

Start the interactive web interface:

```bash
cd app
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

**Features:**
- Upload leaf images
- View disease predictions
- See confidence scores
- Get AI-powered treatment recommendations
- Download analysis reports

---

### 2: REST API (Flask)

Start the Flask backend server:

```bash
cd app
python model_loader.py
```

The API will be available at `http://localhost:5000`

**API Endpoints:**

1. **Health Check**
   ```bash
   curl http://localhost:5000/
   ```

2. **Predict Disease**
   ```bash
   curl -X POST -F "file=@path/to/leaf_image.jpg" http://localhost:5000/predict
   ```

## Dataset

### Dataset Information

- **Source:** [PlantVillage Dataset on Kaggle](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset)
- **Total Classes:** 38 (diseases + healthy conditions)
- **Plant Types:** 14 different crops
- **Image Format:** JPG/JPEG, RGB
- **Image Size:** 256×256 pixels (after preprocessing)

Thank You For Support!