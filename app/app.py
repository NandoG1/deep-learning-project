import streamlit as st
from PIL import Image
import requests
import io

# Page configuration
st.set_page_config(
    page_title="Brillance - Effortless Custom Contract Billing",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if 'current_page' not in st.session_state:
    st.session_state.current_page = 'landing'

API_URL = "https://nando123G-dl-back-end.hf.space/predict"

def call_prediction_api(image_file):
    try:
        img_byte_arr = io.BytesIO()
        image_file.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        
        files = {'file': ('image.png', img_byte_arr, 'image/png')}
        
        response = requests.post(API_URL, files=files, timeout=300)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"API returned status code {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-color: #37322F;
        --secondary-color: #49423D;
        --text-muted: #605A57;
        --background: #F7F5F3;
        --card-bg: #FFFFFF;
        --border-color: rgba(55, 50, 47, 0.12);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main background */
    .stApp {
        background-color: #F7F5F3 !important;
    }
    
    /* Force text color throughout (exclude buttons) */
    .stApp p, .stApp div:not(.stButton):not(.stDownloadButton) span, .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {
        color: #37322F !important;
    }
    
    /* Remove default padding from main container */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }
    
    /* Hero section styling */
    .hero-title {
        font-family: 'Georgia', serif !important;
        font-size: 3.5rem !important;
        font-weight: 400 !important;
        color: #37322F !important;
        text-align: center !important;
        line-height: 1.2 !important;
        margin-bottom: 1rem !important;
    }
    
    .hero-subtitle {
        font-size: 1.1rem !important;
        color: rgba(55, 50, 47, 0.80) !important;
        text-align: center !important;
        max-width: 500px !important;
        margin: 0 auto 2rem auto !important;
        line-height: 1.6 !important;
    }
    
    /* Section headers */
    .section-badge {
        display: inline-block !important;
        padding: 6px 14px !important;
        background: white !important;
        border: 1px solid rgba(2, 6, 23, 0.08) !important;
        border-radius: 90px !important;
        font-size: 0.75rem !important;
        font-weight: 500 !important;
        color: #37322F !important;
        margin-bottom: 1rem !important;
    }
    
    .section-title {
        font-size: 2.5rem !important;
        font-weight: 600 !important;
        color: #49423D !important;
        text-align: center !important;
        margin-bottom: 0.5rem !important;
        letter-spacing: -0.02em !important;
    }
    
    .section-description {
        font-size: 1rem !important;
        color: #605A57 !important;
        text-align: center !important;
        line-height: 1.7 !important;
        max-width: 500px !important;
        margin: 0 auto !important;
    }
    
    /* Feature cards */
    .feature-card {
        background: white;
        border: 1px solid #E0DEDB;
        border-radius: 8px;
        padding: 1.5rem;
        height: 100%;
    }
    
    .feature-card h3 {
        font-size: 0.875rem !important;
        font-weight: 600 !important;
        color: #49423D !important;
        margin-bottom: 0.5rem !important;
    }
    
    .feature-card p {
        font-size: 0.875rem !important;
        color: #605A57 !important;
        line-height: 1.5 !important;
    }
    
    /* Pricing cards */
    .pricing-card {
        background: white;
        border: 1px solid #E0DEDB;
        border-radius: 12px;
        padding: 2rem;
        text-align: left;
    }
    
    .pricing-card.featured {
        background: #37322F;
        border-color: transparent;
    }
    
    .pricing-card.featured h3,
    .pricing-card.featured .price,
    .pricing-card.featured .features li {
        color: white !important;
    }
    
    .pricing-card h3 {
        font-size: 1.125rem;
        font-weight: 500;
        color: rgba(55, 50, 47, 0.90);
        margin-bottom: 0.5rem;
    }
    
    .pricing-card .price {
        font-family: 'Georgia', serif;
        font-size: 3rem;
        font-weight: 500;
        color: #37322F;
        margin: 1rem 0;
    }
    
    .pricing-card .features {
        list-style: none;
        padding: 0;
        margin-top: 1.5rem;
    }
    
    .pricing-card .features li {
        padding: 0.5rem 0;
        color: rgba(55, 50, 47, 0.80);
        font-size: 0.8rem;
    }
    
    /* Testimonial styling */
    .testimonial-quote {
        font-size: 1.5rem;
        font-weight: 500;
        color: #49423D;
        line-height: 1.4;
        letter-spacing: -0.01em;
    }
    
    .testimonial-author {
        font-size: 1.1rem;
        font-weight: 500;
        color: rgba(73, 66, 61, 0.90);
    }
    
    .testimonial-company {
        font-size: 1rem;
        color: rgba(73, 66, 61, 0.70);
    }
    
    /* FAQ styling */
    .faq-question {
        font-size: 1rem;
        font-weight: 500;
        color: #000000;
    }
    
    .faq-answer {
        font-size: 0.875rem;
        color: #000000;
        line-height: 1.6;
    }
    
    /* FAQ expander styling */
    div[data-testid="stExpander"] {
        background-color: transparent !important;
        border: 1px solid #E0DEDB !important;
        border-radius: 8px !important;
        margin-bottom: 0.5rem !important;
    }
    
    div[data-testid="stExpander"] summary {
        background-color: white !important;
        color: #000000 !important;
        font-weight: 500 !important;
        padding: 1rem !important;
    }
    
    div[data-testid="stExpander"] summary:hover {
        background-color: #F7F5F3 !important;
    }
    
    div[data-testid="stExpander"][open] {
        background-color: white !important;
    }
    
    div[data-testid="stExpander"] div[role="button"] {
        background-color: transparent !important;
    }
    
    div[data-testid="stExpander"] p {
        color: #000000 !important;
        background-color: transparent !important;
    }
    
    div[data-testid="stExpander"] .faq-answer {
        background-color: transparent !important;
    }
    
    /* Footer styling */
    .footer-brand {
        font-size: 1.25rem;
        font-weight: 600;
        color: #49423D;
    }
    
    .footer-tagline {
        font-size: 0.875rem;
        color: rgba(73, 66, 61, 0.90);
    }
    
    .footer-heading {
        font-size: 0.875rem;
        font-weight: 500;
        color: rgba(73, 66, 61, 0.50);
        margin-bottom: 0.75rem;
    }
    
    .footer-link {
        font-size: 0.875rem;
        color: #49423D;
        text-decoration: none;
        display: block;
        padding: 0.25rem 0;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #37322F !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 0.75rem 3rem !important;
        font-weight: 500 !important;
    }
    
    .stButton > button:hover {
        background-color: #49423D !important;
        color: #FFFFFF !important;
    }
    
    .stButton > button:active,
    .stButton > button:focus {
        color: #FFFFFF !important;
    }
    
    /* Force button text to be white */
    .stButton button p,
    .stButton button span,
    .stButton button div {
        color: #FFFFFF !important;
    }
    
    /* Download button styling */
    .stDownloadButton > button {
        color: #FFFFFF !important;
    }
    
    .stDownloadButton button p,
    .stDownloadButton button span,
    .stDownloadButton button div {
        color: #FFFFFF !important;
    }
    
    /* Metric styling */
    .metric-value {
        font-family: 'Georgia', serif !important;
        font-size: 3rem !important;
        font-weight: 500 !important;
        color: #37322F !important;
    }
    
    .metric-label {
        font-size: 0.875rem !important;
        color: #605A57 !important;
    }
    
    /* Divider styling */
    hr {
        border: none !important;
        border-top: 1px solid rgba(55, 50, 47, 0.12) !important;
        margin: 2rem 0 !important;
        opacity: 1 !important;
    }
    
    /* Logo cloud */
    .logo-placeholder {
        background: rgba(55, 50, 47, 0.08) !important;
        border-radius: 4px !important;
        padding: 1rem 2rem !important;
        text-align: center !important;
        color: #605A57 !important;
        font-weight: 500 !important;
    }
    
    /* Upload page styling */
    .upload-container {
        background: white;
        border: 1px solid #E0DEDB;
        border-radius: 12px;
        padding: 2.5rem;
        margin: 2rem 0;
    }
    
    .upload-header {
        font-size: 2rem !important;
        font-weight: 600 !important;
        color: #49423D !important;
        margin-bottom: 0.5rem !important;
        letter-spacing: -0.02em !important;
    }
    
    .upload-subheader {
        font-size: 1rem !important;
        color: #605A57 !important;
        margin-bottom: 2rem !important;
        line-height: 1.6 !important;
    }
    
    .result-container {
        background: #F7F5F3;
        border: 1px solid #E0DEDB;
        border-radius: 12px;
        padding: 2rem;
        margin-top: 2rem;
    }
    
    .result-header {
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        color: #37322F !important;
        margin-bottom: 1.5rem !important;
    }
    
    .classification-box {
        background: white !important;
        border: 1px solid #E0DEDB !important;
        border-radius: 8px !important;
        padding: 1.5rem !important;
        margin-bottom: 1.5rem !important;
    }
    
    .classification-label {
        font-size: 0.875rem !important;
        color: rgba(55, 50, 47, 0.60) !important;
        font-weight: 500 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        margin-bottom: 0.5rem !important;
    }
    
    .classification-value {
        font-family: 'Georgia', serif !important;
        font-size: 2rem !important;
        font-weight: 500 !important;
        color: #37322F !important;
        margin-bottom: 0.5rem !important;
    }
        font-size: 0.875rem;
        color: rgba(55, 50, 47, 0.60);
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }
    
    .classification-value {
        font-family: 'Georgia', serif;
        font-size: 2rem;
        font-weight: 500;
        color: #37322F;
        margin-bottom: 0.5rem;
    }
    
    .confidence-bar {
        background: rgba(55, 50, 47, 0.08);
        height: 8px;
        border-radius: 4px;
        overflow: hidden;
        margin-top: 1rem;
    }
    
    .confidence-fill {
        background: #37322F;
        height: 100%;
        transition: width 0.5s ease;
    }
    
    .recommendation-box {
        background: white;
        border: 1px solid #E0DEDB;
        border-radius: 8px;
        padding: 1.5rem;
    }
    
    .recommendation-title {
        font-size: 1.125rem !important;
        font-weight: 600 !important;
        color: #49423D !important;
        margin-bottom: 1rem !important;
    }
    
    .recommendation-text {
        font-size: 0.9375rem !important;
        color: #605A57 !important;
        line-height: 1.7 !important;
    }
    
    /* File uploader styling */
    [data-testid="stFileUploader"] {
        background: white !important;
        border: 2px dashed #E0DEDB !important;
        border-radius: 1px !important;
        padding: 2rem !important;
    }
    
    [data-testid="stFileUploader"]:hover {
        border-color: #37322F !important;
    }
    
    /* File uploader text color */
    [data-testid="stFileUploader"] label,
    [data-testid="stFileUploader"] p,
    [data-testid="stFileUploader"] span,
    [data-testid="stFileUploader"] div {
        color: #605A57 !important;
    }
    
    [data-testid="stFileUploader"] small {
        color: #605A57 !important;
    }
    
    /* File uploader button */
    [data-testid="stFileUploader"] button {
        background-color: #37322F !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
    }
    
    [data-testid="stFileUploader"] button:hover {
        background-color: #49423D !important;
    }
    
    /* Back button */
    .back-button {
        color: #605A57;
        text-decoration: none;
        font-size: 0.9375rem;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 1.5rem;
        cursor: pointer;
    }
    
    .back-button:hover {
        color: #37322F;
    }
            
    html {
        scroll-behavior: smooth;
    }
</style>
""", unsafe_allow_html=True)


def render_header():
    st.markdown("""
    <style>
    /* Header button alignment */
    div[data-testid="column"]:nth-of-type(3) {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 2rem !important;
    }
    div[data-testid="column"]:nth-of-type(3) > div {
        display: flex;
        align-items: center;
    }
    div[data-testid="column"]:nth-of-type(3) .stButton {
        margin: 0 !important;
        margin-left: auto !important;
    }
    div[data-testid="column"]:nth-of-type(3) .stButton > button {
        padding: 0.5rem 1.5rem !important;
        font-size: 0.875rem !important;
        margin: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style=''>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([0.7, 3, 0.7])
    
    with col1:
        st.markdown("""
        <div style='display: flex; align-items: center; height: 32px;'>
            <span style='font-size: 30px; font-weight: 900; color: #49423D;'>NatVision</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='display: flex; justify-content: center; align-items: center; gap: 2.5rem; height: 32px;'>
            <a href='#benefit' style='text-decoration: none; color: rgba(49, 45, 43, 0.80); font-size: 0.875rem; font-weight: 500;'>Benefit</a>
            <a href='#metrics' style='text-decoration: none; color: rgba(49, 45, 43, 0.80); font-size: 0.875rem; font-weight: 500;'>Metrics</a>
            <a href='#faq' style='text-decoration: none; color: rgba(49, 45, 43, 0.80); font-size: 0.875rem; font-weight: 500;'>FaQ</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        if st.button("Join", key="login_btn"):
            st.session_state.current_page = 'upload'
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<hr style='margin: 0.75rem 0 1.5rem 0;'>", unsafe_allow_html=True)

def render_hero():
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <h1 class="hero-title">
        AI-powered plant disease detection <br> by Deep Learning
    </h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <p class="hero-subtitle" id="benefit">
       Upload a leaf photo and get instant health analysis powered by AI. 
        Include a classification and a recommendation action.
    </p>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Start for free", key="hero_cta", use_container_width=True):
            st.session_state.current_page = 'upload'
            st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True) 
    st.markdown("<hr>", unsafe_allow_html=True)


def render_feature_cards():
    st.markdown("<br>", unsafe_allow_html=True)
    
    features = [
        {
            "title": "Accurate Disease Detection",
            "description": "Identify plant diseases with high precision using an AI model trained on thousands of real-world images."
        },
        {
            "title": "Simple & Easy to Use",
            "description": "Upload a photo of a leaf or fruit, and get instant diagnostic results — no expert knowledge required."
        },
        {
            "title": "Actionable Care Recommendations",
            "description": "Receive suggested treatment steps to help prevent further crop damage and support healthy plant growth."
        }
    ]
    
    cols = st.columns(3)
    for i, feature in enumerate(features):
        with cols[i]:
            st.markdown(f"""
            <div class="feature-card">
                <h3>{feature['title']}</h3>
                <p>{feature['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)

def render_social_proof():
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown('<div id="metrics" style="text-align: center;"><span class="section-badge">Supported Plant Classes</span></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Plant classes we can accurately detect</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-description">Our model is trained to recognize a wide variety of plant diseases and healthy conditions across multiple crop types.</p>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    logo_cols = st.columns(4)
    companies = ["Apple – Apple Scab", "Apple – Black Rot", "Blueberry – Healthy", "Cherry – Powdery Mildew"]
    for i, company in enumerate(companies):
        with logo_cols[i]:
            st.markdown(f'<div class="logo-placeholder">{company}</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    logo_cols2 = st.columns(4)
    companies2 = ["Corn – Common Rust", "Grape – Black Rot", "Bell Pepper – Healthy", "And many more..."]
    for i, company in enumerate(companies2):
        with logo_cols2[i]:
            st.markdown(f'<div class="logo-placeholder">{company}</div>', unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)

def render_metrics():
    st.markdown("<br>", unsafe_allow_html=True)
    
    metrics = [
        {"value": "86%", "label": "Accuracy"},
        {"value": "84%", "label": "Precision"},
        {"value": "85%", "label": "Recall"},
        {"value": "83%", "label": "F1 Score"}
    ]
    
    cols = st.columns(4)
    for i, metric in enumerate(metrics):
        with cols[i]:
            st.markdown(f"""
            <div style="text-align: center; padding: 1.5rem;" id="faq">
                <div class="metric-value">{metric['value']}</div>
                <div class="metric-label">{metric['label']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)

def render_faq():
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<h2 style="font-size: 2rem; font-weight: 600; color: #49423D; letter-spacing: -0.02em;">Frequently Asked Questions</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color: #605A57; font-size: 1rem;">Explore your data, build your dashboard, bring your team together.</p>', unsafe_allow_html=True)
    
    with col2:
        faq_data = [
            {
                "question": "What is this application and who is it for?",
                "answer": "This app is a plant disease detection tool designed for farmers, gardeners, researchers, and anyone who wants quick insights into plant health. Simply upload a leaf image, and the system will identify the disease and provide recommendations."
            },
            {
                "question": "How does the plant disease classification work?",
                "answer": "Our model analyzes the uploaded leaf image using a deep learning classifier trained on thousands of plant disease samples. It then predicts the most likely class and provides a confidence score for transparency."
            },
            {
                "question": "What is the confidence score shown in the results?",
                "answer": "The confidence score represents how certain the model is about its prediction. Higher scores indicate stronger confidence in the detected disease or healthy condition."
            },
            {
                "question": "What kind of recommendations will I receive?",
                "answer": "After classification, the app uses Google Gemini to generate personalized suggestions—such as treatment steps, prevention tips, and care recommendations—based on the detected disease."
            },
            {
                "question": "Which plant types does the system support?",
                "answer": "Our model supports over 30 classes, including diseases from apples, tomatoes, grapes, potatoes, peppers, citrus plants, and more. You can view the full list on the “Supported Classes” section."
            },
            {
                "question": "Is my uploaded image stored anywhere?",
                "answer": "No. Images are processed securely and are not stored on our servers. Your data remains private and is only used to generate your classification result."
            }
        ]
        
        for faq in faq_data:
            with st.expander(faq["question"]):
                st.markdown(f'<p class="faq-answer">{faq["answer"]}</p>', unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)

def render_cta():
    st.markdown("""
    <div style="text-align: center; padding: 3rem 0;">
        <h2 style="font-size: 2.5rem; font-weight: 600; color: #49423D; margin-bottom: 1rem; letter-spacing: -0.02em;">
            Ready to improve your plant health diagnostics?
        </h2>
        <p style="color: #605A57; font-size: 1.1rem; max-width: 500px; margin: 0 auto 2rem auto;">
            Join thousands of growers, researchers, and plant enthusiasts who rely on our AI-powered system to identify diseases quickly and accurately.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    cta_col1, cta_col2, cta_col3 = st.columns([1, 1, 1])
    with cta_col2:
        if st.button("Get started today", key="cta_btn", use_container_width=True):
            st.session_state.current_page = 'upload'
            st.rerun()
    
    st.markdown("<hr>", unsafe_allow_html=True)


def render_footer():
    st.markdown("""
    <div style='text-align: center; padding: 1.5rem 0; color: #605A57; font-size: 0.875rem;'>
        © 2025 NatVision. All rights reserved.
    </div>
    """, unsafe_allow_html=True)


def render_upload_page():
    if st.button("← Back to Home", key="back_btn"):
        st.session_state.current_page = 'landing'
        st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <span class="section-badge">AI Analysis</span>
        <h1 class="upload-header" style="text-align: center; margin-top: 1rem;">Upload Your Plant Leaf Image</h1>
        <p class="upload-subheader" style="text-align: center; max-width: 600px; margin: 0 auto;">
            Upload a clear image of your plant leaf and our AI will analyze it to detect diseases 
            and provide personalized treatment recommendations.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("""
        <div class="upload-container">
            <h3 style="font-size: 1.25rem; font-weight: 600; color: #49423D; margin-bottom: 1rem;">
                Step 1: Upload Image
            </h3>
            <p style="font-size: 0.875rem; color: #605A57; margin-bottom: 1.5rem;">
                Choose a clear photo of your plant leaf. For best results, ensure good lighting and focus on the affected area.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            "Choose an image file",
            type=['jpg', 'jpeg', 'png'],
            label_visibility="collapsed"
        )
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            st.markdown("""
            <div style="background: #F7F5F3; border: 1px solid #E0DEDB; border-radius: 8px; padding: 1rem;">
                <h4 style="font-size: 0.875rem; font-weight: 600; color: #49423D; margin-bottom: 0.75rem;">
                    Image Guidelines
                </h4>
                <ul style="font-size: 0.8125rem; color: #605A57; margin: 0; padding-left: 1.25rem;">
                    <li>Clear, well-lit photograph</li>
                    <li>Focus on the leaf surface</li>
                    <li>Minimum resolution: 224x224 pixels</li>
                    <li>Supported formats: JPG, PNG</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            if st.button("Analyze Image", key="analyze_btn", use_container_width=True):
                loading_placeholder = st.empty()
                with loading_placeholder.container():
                    st.markdown("""
                    <div style="text-align: center; padding: 2rem; background: #F7F5F3; border-radius: 12px; border: 1px solid #E0DEDB; margin-bottom: 16px;">
                        <div style="margin-bottom: 1rem;">
                            <div style="display: inline-block; width: 50px; height: 50px; border: 4px solid #E0DEDB; border-top: 4px solid #37322F; border-radius: 50%; animation: spin 1s linear infinite;"></div>
                        </div>
                        <h4 style="color: #49423D; font-size: 1rem; font-weight: 600; margin: 0;">Analyzing your image...</h4>
                        <p style="color: #605A57; font-size: 0.875rem; margin-top: 0.5rem;">Please wait while our AI processes the image</p>
                    </div>
                    <style>
                    @keyframes spin {
                        0% { transform: rotate(0deg); }
                        100% { transform: rotate(360deg); }
                    }
                    </style>
                    """, unsafe_allow_html=True)
                
                result = call_prediction_api(image)
                
                loading_placeholder.empty()
                
                predicted_class = result.get('prediction', 'Unknown')
                confidence_str = result.get('confidence', '0.00%')
                ai_recommendation = result.get('ai_recommendation', 'No recommendation available')
                
                try:
                    confidence_value = float(confidence_str.replace('%', ''))
                except:
                    confidence_value = 0.0
                
                if "healthy" in predicted_class.lower():
                    severity = "Healthy"
                elif confidence_value >= 85:
                    severity = "High Confidence"
                elif confidence_value >= 70:
                    severity = "Moderate Confidence"
                else:
                    severity = "Low Confidence"
                
                disease_display = predicted_class.replace('___', ' - ').replace('_', ' ')
                
                st.session_state.prediction_result = {
                    "disease": disease_display,
                    "confidence": confidence_value,
                    "severity": severity,
                    "recommendation": ai_recommendation
                }
                st.session_state.analysis_complete = True
                st.rerun()
    
    with col2:
        if st.session_state.get('analysis_complete', False):
            result = st.session_state.prediction_result
            
            st.markdown("""
            <div class="upload-container">
                <h3 style="font-size: 1.25rem; font-weight: 600; color: #49423D; margin-bottom: 1rem;">
                    Step 2: Analysis Results
                </h3>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="classification-box">
                <div class="classification-label">Disease Detected</div>
                <div class="classification-value">{result['disease']}</div>
                <div style="margin-top: 1rem;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                        <span style="font-size: 0.875rem; color: #605A57;">Confidence</span>
                        <span style="font-size: 0.875rem; font-weight: 600; color: #37322F;">{result['confidence']}%</span>
                    </div>
                    <div class="confidence-bar">
                        <div class="confidence-fill" style="width: {result['confidence']}%;"></div>
                    </div>
                </div>
                <div style="margin-top: 1rem;">
                    <span style="font-size: 0.875rem; color: #605A57;">Severity Level: </span>
                    <span style="font-size: 0.875rem; font-weight: 600; color: #37322F;">{result['severity']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="recommendation-box">
                <div class="recommendation-title">Treatment Recommendations</div>
                <div class="recommendation-text">{result['recommendation']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)

            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                if st.button("Analyze Another Image", key="reset_btn", use_container_width=True):
                    st.session_state.analysis_complete = False
                    st.rerun()
            with btn_col2:
                st.download_button(
                    label="Download Report",
                    data=f"Disease: {result['disease']}\nConfidence: {result['confidence']}%\n\nRecommendations:\n{result['recommendation']}",
                    file_name="plant_disease_report.txt",
                    mime="text/plain",
                    use_container_width=True
                )
        else:
            st.markdown("""
            <div class="upload-container">
                <h3 style="font-size: 1.25rem; font-weight: 600; color: #49423D; margin-bottom: 1rem;">
                    How It Works
                </h3>
                <div style="font-size: 0.9375rem; color: #605A57; line-height: 1.7;">
                    <p><strong>1. Upload:</strong> Select a clear image of your plant leaf</p>
                    <p><strong>2. Analyze:</strong> Our AI model processes the image using deep learning</p>
                    <p><strong>3. Results:</strong> Get instant disease classification with confidence scores</p>
                    <p><strong>4. Recommendations:</strong> Receive personalized treatment advice from AI</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="recommendation-box" style="margin-top: 1.5rem; margin-bottom: 1.5rem;">
                <div class="recommendation-title">Why Choose Our AI?</div>
                <ul style="font-size: 0.875rem; color: #605A57; line-height: 1.8; margin: 0; padding-left: 1.25rem;">
                    <li>85%+ accuracy rate on disease detection</li>
                    <li>Instant analysis in under seconds</li>
                    <li>AI-powered treatment recommendations</li>
                    <li>Trained on thousands of plant disease images</li>
                    <li>Using modern deep learning techinque</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)


def main():
    if st.session_state.current_page == 'landing':
        render_header()
        render_hero()
        render_feature_cards()
        render_social_proof()
        render_metrics()
        render_faq()
        render_cta()
        render_footer()
    elif st.session_state.current_page == 'upload':
        render_upload_page()

if __name__ == "__main__":
    main()
