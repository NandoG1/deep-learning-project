import os
import io
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
from flask import Flask, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)

MODEL_PATH = '../outputs/models/plant_disease_model.pth' 

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

CLASS_NAMES = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Blueberry___healthy',
    'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch',
    'Strawberry___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus'
]

def build_model(num_classes):
    model = models.efficientnet_b0(weights=None)

    in_features = model.classifier[1].in_features
    model.classifier = nn.Sequential(
        nn.Dropout(0.5),
        nn.Linear(in_features, num_classes)
    )
    return model

model = build_model(len(CLASS_NAMES))


state_dict = torch.load(MODEL_PATH, map_location=DEVICE)
model.load_state_dict(state_dict)

model.to(DEVICE)
model.eval()


transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(256),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

def predict_single_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    
    input_tensor = transform(image).unsqueeze(0).to(DEVICE)
    
    with torch.no_grad():
        outputs = model(input_tensor)
        probabilities = torch.nn.functional.softmax(outputs, dim=1)
        confidence, predicted_idx = torch.max(probabilities, 1)
    
    predicted_class = CLASS_NAMES[predicted_idx.item()]
    confidence_score = confidence.item() * 100
    
    return predicted_class, confidence_score

def get_gemini_recommendation(disease_name):
        
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    prompt = f"""
    Pengguna memiliki tanaman yang terdeteksi penyakit: '{disease_name}'.
    
    Tugas kamu:
    1. Konfirmasi apakah ini penyakit berbahaya atau kondisi sehat.
    2. Jika penyakit, jelaskan penyebab singkatnya.
    3. Berikan 3-4 langkah solusi praktis untuk mengobatinya.
    4. Berikan tips pencegahan.
    
    Gunakan Bahasa Indonesia yang ramah dan format poin-poin. Buat tulisannya kayak artikel (anggap tidak ada pengguna).
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Gagal menghubungi AI: {str(e)}"

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "Server Ready", "model": "Plant Disease Detection EfficientNet"})

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({"error": "Model not loaded properly"}), 500
        
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    try:
        image_bytes = file.read()
        pred_class, confidence = predict_single_image(image_bytes)
        
        ai_advice = get_gemini_recommendation(pred_class)
        
        return jsonify({
            "status": "success",
            "prediction": pred_class,
            "confidence": f"{confidence:.2f}%",
            "ai_recommendation": ai_advice
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)