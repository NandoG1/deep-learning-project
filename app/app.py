import streamlit as st
from PIL import Image
import io

# Page configuration
st.set_page_config(
    page_title="LensFolia - Deteksi Penyakit Daun",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Dark theme with cyan accent like in the image
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    /* Dark theme */
    .stApp {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Navigation bar */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 3rem;
        background-color: #2a2a2a;
        border-bottom: 1px solid #333;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 999;
    }
    
    .navbar-brand {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 1.25rem;
        font-weight: 600;
        color: #ffffff;
    }
    
    .navbar-menu {
        display: flex;
        gap: 2rem;
        align-items: center;
    }
    
    .nav-link {
        color: #a0a0a0;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s;
        cursor: pointer;
    }
    
    .nav-link:hover {
        color: #00d9ff;
    }
    
    .nav-link.active {
        color: #ffffff;
    }
    
    .btn-primary {
        background-color: #00d9ff;
        color: #1a1a1a;
        padding: 0.625rem 1.5rem;
        border-radius: 6px;
        font-weight: 600;
        text-decoration: none;
        border: none;
        cursor: pointer;
        transition: all 0.3s;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .btn-primary:hover {
        background-color: #00c4e6;
        transform: translateY(-1px);
    }
    
    /* Theme toggle */
    .theme-toggle {
        background: transparent;
        border: 1px solid #444;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        color: #a0a0a0;
        transition: all 0.3s;
    }
    
    .theme-toggle:hover {
        border-color: #00d9ff;
        color: #00d9ff;
    }
    
    /* Main content */
    .main-content {
        margin-top: 80px;
        padding: 3rem;
    }
    
    /* Hero section */
    .hero-section {
        text-align: center;
        padding: 4rem 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .intro-badge {
        background-color: #2a2a2a;
        border: 1px solid #333;
        color: #a0a0a0;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 2rem;
        font-size: 0.875rem;
    }
    
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        color: #ffffff;
        line-height: 1.2;
        margin: 1rem 0;
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Feature cards */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
        gap: 1.5rem;
        margin: 3rem 0;
        max-width: 1200px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .feature-card {
        background: linear-gradient(135deg, #2a2a2a 0%, #252525 100%);
        border: 1px solid #333;
        border-radius: 12px;
        padding: 2rem;
        transition: all 0.3s;
    }
    
    .feature-card:hover {
        border-color: #00d9ff;
        transform: translateY(-4px);
        box-shadow: 0 8px 24px rgba(0, 217, 255, 0.1);
    }
    
    .feature-icon {
        width: 50px;
        height: 50px;
        background-color: #1a1a1a;
        border: 1px solid #333;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1.5rem;
        color: #00d9ff;
        font-size: 1.5rem;
    }
    
    .feature-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 0.75rem;
    }
    
    .feature-description {
        color: #a0a0a0;
        line-height: 1.6;
        font-size: 0.9375rem;
    }
    
    /* Stats section */
    .stats-section {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.5rem;
        margin: 3rem auto;
        max-width: 1200px;
        background: linear-gradient(135deg, #2a2a2a 0%, #252525 100%);
        border: 1px solid #333;
        border-radius: 12px;
        padding: 2rem;
    }
    
    .stat-item {
        text-align: center;
        padding: 1.5rem 1rem;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #00d9ff;
        margin-bottom: 0.5rem;
        font-family: 'Courier New', monospace;
    }
    
    .stat-label {
        color: #a0a0a0;
        font-size: 0.875rem;
        text-transform: lowercase;
    }
    
    .stat-item:not(:last-child) {
        border-right: 1px solid #333;
    }
    
    /* Upload section */
    .upload-section {
        background: linear-gradient(135deg, #2a2a2a 0%, #252525 100%);
        border: 1px solid #333;
        border-radius: 12px;
        padding: 2.5rem;
        max-width: 800px;
        margin: 3rem auto;
    }
    
    .upload-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    /* Result card */
    .result-card {
        background: linear-gradient(135deg, #1a3a3a 0%, #1a2a2a 100%);
        border: 1px solid #00d9ff;
        border-radius: 12px;
        padding: 2rem;
        margin-top: 2rem;
    }
    
    .result-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #00d9ff;
        margin-bottom: 1.5rem;
    }
    
    .result-item {
        display: flex;
        justify-content: space-between;
        padding: 1rem 0;
        border-bottom: 1px solid #333;
    }
    
    .result-item:last-child {
        border-bottom: none;
    }
    
    .result-label {
        color: #a0a0a0;
        font-weight: 500;
    }
    
    .result-value {
        color: #ffffff;
        font-weight: 600;
    }
    
    /* Streamlit overrides */
    .stButton>button {
        background-color: #00d9ff;
        color: #1a1a1a;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 6px;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s;
        font-size: 1rem;
    }
    
    .stButton>button:hover {
        background-color: #00c4e6;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 217, 255, 0.3);
    }
    
    [data-testid="stFileUploader"] {
        background-color: #1a1a1a;
        border: 2px dashed #444;
        border-radius: 8px;
        padding: 2rem;
    }
    
    [data-testid="stFileUploader"]:hover {
        border-color: #00d9ff;
    }
    
    /* Footer note */
    .footer-note {
        text-align: center;
        color: #666;
        font-size: 0.875rem;
        margin-top: 4rem;
        padding-bottom: 2rem;
    }
    
    /* Adjust spacing */
    .block-container {
        padding-top: 0 !important;
        max-width: 100% !important;
    }
    
    /* FAQ Section */
    .faq-section {
        max-width: 900px;
        margin: 4rem auto;
        padding: 0 2rem;
    }
    
    .faq-badge {
        background-color: #2a2a2a;
        border: 1px solid #333;
        color: #a0a0a0;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 2rem;
        font-size: 0.875rem;
    }
    
    .faq-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .faq-item {
        background: linear-gradient(135deg, #2a2a2a 0%, #252525 100%);
        border: 1px solid #333;
        border-radius: 12px;
        margin-bottom: 1rem;
        overflow: hidden;
        transition: all 0.3s;
    }
    
    .faq-item:hover {
        border-color: #444;
    }
    
    .faq-question {
        padding: 1.5rem;
        font-size: 1rem;
        font-weight: 600;
        color: #ffffff;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: all 0.3s;
    }
    
    .faq-question:hover {
        color: #00d9ff;
    }
    
    .faq-arrow {
        color: #00d9ff;
        transition: transform 0.3s;
        font-size: 1.2rem;
    }
    
    .faq-arrow.open {
        transform: rotate(180deg);
    }
    
    .faq-answer {
        padding: 0 1.5rem 1.5rem 1.5rem;
        color: #a0a0a0;
        line-height: 1.6;
        font-size: 0.9375rem;
    }
    
    /* Footer */
    .footer {
        background-color: #1a1a1a;
        border-top: 1px solid #333;
        padding: 2rem;
        text-align: center;
        margin-top: 4rem;
    }
    
    .footer-text {
        color: #666;
        font-size: 0.875rem;
    }
    
    /* Deep Learning Hero Section */
    .dl-hero-section {
        background: linear-gradient(135deg, #1a3a3a 0%, #1a2a2a 100%);
        padding: 5rem 2rem;
        text-align: center;
        margin-top: 80px;
        position: relative;
        overflow: hidden;
    }
    
    .dl-hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 50% 50%, rgba(0, 217, 255, 0.1) 0%, transparent 70%);
        pointer-events: none;
    }
    
    .dl-badge {
        background-color: rgba(42, 42, 42, 0.8);
        border: 1px solid #333;
        color: #a0a0a0;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 2rem;
        font-size: 0.875rem;
    }
    
    .dl-hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        color: #ffffff;
        line-height: 1.2;
        margin: 1rem auto 1.5rem auto;
        max-width: 1000px;
    }
    
    .dl-hero-description {
        font-size: 1.125rem;
        color: #a0a0a0;
        line-height: 1.6;
        max-width: 800px;
        margin: 0 auto 2.5rem auto;
    }
    
    .dl-button-group {
        display: flex;
        gap: 1rem;
        justify-content: center;
        align-items: center;
        margin-bottom: 3rem;
    }
    
    .btn-cyan {
        background-color: #00d9ff;
        color: #1a1a1a;
        padding: 0.875rem 2rem;
        border-radius: 6px;
        font-weight: 600;
        text-decoration: none;
        border: none;
        cursor: pointer;
        transition: all 0.3s;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 1rem;
    }
    
    .btn-cyan:hover {
        background-color: #00c4e6;
        transform: translateY(-2px);
        box-shadow: 0 4px 16px rgba(0, 217, 255, 0.3);
    }
    
    .btn-secondary {
        background-color: transparent;
        color: #ffffff;
        padding: 0.875rem 2rem;
        border-radius: 6px;
        font-weight: 600;
        text-decoration: none;
        border: 1px solid #444;
        cursor: pointer;
        transition: all 0.3s;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 1rem;
    }
    
    .btn-secondary:hover {
        border-color: #00d9ff;
        color: #00d9ff;
        transform: translateY(-2px);
    }
    
    .dl-image-container {
        max-width: 900px;
        margin: 0 auto;
        position: relative;
        z-index: 1;
    }
    
    .dl-laptop-mockup {
        width: 100%;
        border-radius: 12px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
        border: 1px solid #333;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation bar
st.markdown("""
    <div class="navbar">
        <div class="navbar-brand">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="10" stroke="#00d9ff" stroke-width="2"/>
                <path d="M12 6v12M6 12h12" stroke="#00d9ff" stroke-width="2" stroke-linecap="round"/>
            </svg>
            <span>LensFolia</span>
        </div>
        <div class="navbar-menu">
            <a href="#intro" class="nav-link active">Intro</a>
            <a href="#fitur" class="nav-link">Fitur</a>
            <a href="#cara-kerja" class="nav-link">Cara Kerja</a>
            <a href="#faq" class="nav-link">FAQ</a>
            <div class="theme-toggle">🌙</div>
            <a href="#mulai" class="btn-primary">
                Mulai →
            </a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Main content
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Deep Learning Hero Section
st.markdown("""
    <div class="dl-hero-section">
        <div class="dl-badge">
            <span>✨</span>
            <span>Deep Learning</span>
        </div>
        <h1 class="dl-hero-title">
            Deteksi Penyakit Tanaman Melalui Daun dalam Sekejap dengan AI menggunakan LensFolia!
        </h1>
        <p class="dl-hero-description">
            Gunakan teknologi kecerdasan buatan untuk menganalisis kondisi daun tanaman Anda—cepat, 
            akurat, dan mudah digunakan oleh siapa saja.
        </p>
        <div class="dl-button-group">
            <a href="#mulai" class="btn-cyan">Coba Sekarang</a>
            <a href="#fitur" class="btn-secondary">Pelajari Lebih</a>
        </div>
        <div class="dl-image-container">
            <img src="https://images.unsplash.com/photo-1530836369250-ef72a3f5cda8?w=900&h=500&fit=crop" 
                 class="dl-laptop-mockup" 
                 alt="Disease Detection Demo">
        </div>
    </div>
""", unsafe_allow_html=True)

# Hero section
st.markdown("""
    <div class="hero-section">
        <div class="intro-badge">
            <span>✨</span>
            <span>Intro</span>
        </div>
        <h1 class="hero-title">
            Mengapa Menggunakan LensFolia untuk Deteksi Dini Pada Tanaman Anda itu Penting?
        </h1>
    </div>
""", unsafe_allow_html=True)

# Feature cards
st.markdown("""
    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">🌿</div>
            <div class="feature-title">Pentingnya Kesehatan Daun bagi Tanaman</div>
            <div class="feature-description">
                Kesehatan daun mencerminkan kondisi tanaman secara keseluruhan. 
                Dengan deteksi dini, Anda dapat mencegah kerusakan dan meningkatkan hasil panen.
            </div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🧬</div>
            <div class="feature-title">Solusi AI untuk Diagnosis Penyakit Daun</div>
            <div class="feature-description">
                Kami menghadirkan solusi AI yang menganalisis gambar daun secara otomatis. 
                Teknologi ini mengenali penyakit dan memberikan rekomendasi perawatan yang tepat.
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Stats section
st.markdown("""
    <div class="stats-section">
        <div class="stat-item">
            <div class="stat-number">92.1%</div>
            <div class="stat-label">Tingkat akurasi*</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">< 1 menit</div>
            <div class="stat-label">Hasil cepat*</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">100+</div>
            <div class="stat-label">Jenis penyakit*</div>
        </div>
    </div>
    <div class="footer-note">*Berdasarkan pengujian internal</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Classification section
st.markdown('<div id="mulai"></div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("""
        <div class="upload-section">
            <div class="upload-title">Upload Gambar Daun</div>
        </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Pilih gambar daun untuk dianalisis", 
        type=['jpg', 'jpeg', 'png'],
        label_visibility="collapsed"
    )
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)
        
        if st.button("Analisis Gambar"):
            with st.spinner('Menganalisis...'):
                # TODO: Replace with actual model prediction
                import time
                time.sleep(1)
                
                st.session_state.prediction_done = True
                st.session_state.disease = "Apple Scab"
                st.session_state.confidence = 92.1
                st.session_state.severity = "Sedang"

with col2:
    if 'prediction_done' in st.session_state and st.session_state.prediction_done:
        st.markdown(f"""
            <div class="result-card">
                <div class="result-title">Hasil Analisis</div>
                <div class="result-item">
                    <span class="result-label">Penyakit Terdeteksi</span>
                    <span class="result-value">{st.session_state.disease}</span>
                </div>
                <div class="result-item">
                    <span class="result-label">Tingkat Keyakinan</span>
                    <span class="result-value">{st.session_state.confidence}%</span>
                </div>
                <div class="result-item">
                    <span class="result-label">Tingkat Keparahan</span>
                    <span class="result-value">{st.session_state.severity}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### Rekomendasi Perawatan")
        st.markdown("""
            <div class="feature-card">
                <ul style="color: #a0a0a0; line-height: 1.8;">
                    <li>Buang dan musnahkan bagian tanaman yang terinfeksi</li>
                    <li>Tingkatkan sirkulasi udara di sekitar tanaman</li>
                    <li>Aplikasikan fungisida sesuai anjuran</li>
                    <li>Monitor tanaman sekitar untuk mencegah penyebaran</li>
                    <li>Konsultasikan dengan ahli pertanian untuk kasus parah</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-title">Cara Menggunakan</div>
                <div class="feature-description">
                    <ol style="line-height: 1.8;">
                        <li>Upload gambar daun yang ingin dianalisis</li>
                        <li>Pastikan gambar jelas dan fokus pada daun</li>
                        <li>Klik tombol "Analisis Gambar"</li>
                        <li>Lihat hasil diagnosis dan rekomendasi</li>
                    </ol>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="feature-card" style="margin-top: 1rem;">
                <div class="feature-title">Tips untuk Hasil Terbaik</div>
                <div class="feature-description">
                    <ul style="line-height: 1.8;">
                        <li>Gunakan pencahayaan yang baik</li>
                        <li>Foto dari jarak dekat</li>
                        <li>Pastikan daun terlihat jelas</li>
                        <li>Hindari bayangan yang berlebihan</li>
                    </ul>
                </div>
            </div>
        """, unsafe_allow_html=True)

# FAQ Section
st.markdown('<div id="faq"></div>', unsafe_allow_html=True)

st.markdown("""
    <div class="faq-section">
        <div style="text-align: center;">
            <div class="faq-badge">
                <span>✨</span>
                <span>Frequently Asked Questions</span>
            </div>
        </div>
        <h2 class="faq-title">Pertanyaan yang Sering Diajukan</h2>
    </div>
""", unsafe_allow_html=True)

# FAQ items with expandable sections
with st.container():
    st.markdown('<div style="max-width: 900px; margin: 0 auto; padding: 0 2rem;">', unsafe_allow_html=True)
    
    # FAQ 1
    with st.expander("Apakah aplikasi ini dapat digunakan untuk semua jenis tanaman?", expanded=True):
        st.markdown("""
        <div style="color: #a0a0a0; line-height: 1.6;">
        Aplikasi ini dirancang untuk mendeteksi penyakit pada berbagai jenis tanaman umum. Namun, kami terus 
        memperbarui data untuk mendukung lebih banyak jenis tanaman di masa depan.
        </div>
        """, unsafe_allow_html=True)
    
    # FAQ 2
    with st.expander("Bagaimana cara menggunakan aplikasi ini untuk mendiagnosa penyakit tanaman?"):
        st.markdown("""
        <div style="color: #a0a0a0; line-height: 1.6;">
        Cukup upload foto daun tanaman yang ingin Anda periksa, kemudian sistem AI kami akan menganalisis 
        gambar tersebut dan memberikan diagnosis beserta rekomendasi perawatan dalam hitungan detik.
        </div>
        """, unsafe_allow_html=True)
    
    # FAQ 3
    with st.expander("Apakah aplikasi ini membutuhkan koneksi internet?"):
        st.markdown("""
        <div style="color: #a0a0a0; line-height: 1.6;">
        Ya, aplikasi ini memerlukan koneksi internet untuk dapat mengakses model AI dan memberikan hasil 
        diagnosis yang akurat. Pastikan Anda terhubung ke internet saat menggunakan aplikasi.
        </div>
        """, unsafe_allow_html=True)
    
    # FAQ 4
    with st.expander("Apakah data tanaman saya aman saat menggunakan aplikasi ini?"):
        st.markdown("""
        <div style="color: #a0a0a0; line-height: 1.6;">
        Privasi Anda adalah prioritas kami. Gambar yang Anda upload hanya digunakan untuk proses analisis 
        dan tidak disimpan secara permanen di server kami. Data Anda aman dan terlindungi.
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <div class="footer-text">Copyright © ReaksiJS 2025</div>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
