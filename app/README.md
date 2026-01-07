# Plant Disease Detection Application

A comprehensive plant disease detection system featuring a Flask REST API backend and a Streamlit web interface. This application uses a deep learning model (EfficientNet-B0) to identify plant diseases from leaf images and provides AI treatment recommendations using Google Gemini.

## Overview

The application consists of two main components:
1. **Flask API** (`model_loader.py`) - RESTful backend service for image classification
2. **Streamlit Web App** (`app.py`) - User-friendly frontend interface

## Installation

### Prerequisites

- Python 3.8+
- PyTorch
- Flask
- Streamlit
- Google Gemini API Key

### Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   ```bash
   # For Windows PowerShell
   $env:GEMINI_API_KEY="your_api_key_here"
   
   # For Linux/Mac
   export GEMINI_API_KEY="your_api_key_here"
   ```

3. **Ensure model file exists:**
   The trained model should be located at: `../outputs/models/plant_disease_model.pth`


## Usage

### Option 1: Flask API (Backend Service)

Start the Flask API server:

```bash
python model_loader.py
```

The API will be available at: `http://localhost:5000`

### Option 2: Streamlit Web Interface

Start the Streamlit application:

```bash
streamlit run app.py
```

The web interface will open in your browser at: `http://localhost:8501`

#### Using the Web Interface

1. **Landing Page:**
   - View application features and benefits
   - Check model accuracy metrics (86% accuracy, 84% precision, 85% recall)
   - Browse supported plant classes
   - Read FAQ section

2. **Upload & Analyze:**
   - Click "Join" or "Start for free" button
   - Upload a clear image of a plant leaf (JPG, JPEG, or PNG)
   - Click "Analyze Image"
   - View results including:
     - Detected disease name
     - Confidence score with visual bar
     - Severity level classification
     - AI-generated treatment recommendations (in Indonesian)

3. **Download Report:**
   - Download analysis results as a text file
   - Analyze another image without page reload


## Architecture

```
┌─────────────────────────────────────────┐
│         Streamlit Web Interface         │
│              (app.py)                   │
│  - User uploads image                   │
│  - Display results & recommendations    │
└──────────────┬──────────────────────────┘
               │ HTTP POST /predict
               ▼
┌─────────────────────────────────────────┐
│          Flask REST API                 │
│         (model_loader.py)               │
│  - Receives image                       │
│  - Performs inference                   │
│  - Gets AI recommendations              │
└──────────────┬──────────────────────────┘
               │
               ├──────────────┐
               ▼              ▼
    ┌──────────────┐  ┌──────────────┐
    │ EfficientNet │  │ Google Gemini│
    │   Model      │  │     API      │
    │ (PyTorch)    │  │              │
    └──────────────┘  └──────────────┘
```

---

## Technologies Used

- **Deep Learning:** PyTorch, TorchVision
- **Web Framework:** Flask, Streamlit
- **Image Processing:** PIL (Pillow)
- **AI Integration:** Google Gemini API
- **HTTP Client:** Requests
- **Model Architecture:** EfficientNet-B0

---

## License

See LICENSE file in the root directory.

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## Contact & Support

For issues, questions, or contributions, please refer to the project repository.

---

## Acknowledgments

- Model trained on plant disease dataset
- EfficientNet architecture from TorchVision
- AI recommendations powered by Google Gemini
