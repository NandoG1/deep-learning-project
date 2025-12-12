import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Brillance - Effortless Custom Contract Billing",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state for navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'landing'

# Custom CSS for styling
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
        background-color: #F7F5F3;
    }
    
    /* Hero section styling */
    .hero-title {
        font-family: 'Georgia', serif;
        font-size: 3.5rem;
        font-weight: 400;
        color: #37322F;
        text-align: center;
        line-height: 1.2;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
        color: rgba(55, 50, 47, 0.80);
        text-align: center;
        max-width: 500px;
        margin: 0 auto 2rem auto;
        line-height: 1.6;
    }
    
    /* Section headers */
    .section-badge {
        display: inline-block;
        padding: 6px 14px;
        background: white;
        border: 1px solid rgba(2, 6, 23, 0.08);
        border-radius: 90px;
        font-size: 0.75rem;
        font-weight: 500;
        color: #37322F;
        margin-bottom: 1rem;
    }
    
    .section-title {
        font-size: 2.5rem;
        font-weight: 600;
        color: #49423D;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    
    .section-description {
        font-size: 1rem;
        color: #605A57;
        text-align: center;
        line-height: 1.7;
        max-width: 500px;
        margin: 0 auto;
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
        font-size: 0.875rem;
        font-weight: 600;
        color: #49423D;
        margin-bottom: 0.5rem;
    }
    
    .feature-card p {
        font-size: 0.875rem;
        color: #605A57;
        line-height: 1.5;
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
        color: #49423D;
    }
    
    .faq-answer {
        font-size: 0.875rem;
        color: #605A57;
        line-height: 1.6;
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
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 0.75rem 3rem !important;
        font-weight: 500 !important;
    }
    
    .stButton > button:hover {
        background-color: #49423D !important;
    }
    
    /* Metric styling */
    .metric-value {
        font-family: 'Georgia', serif;
        font-size: 3rem;
        font-weight: 500;
        color: #37322F;
    }
    
    .metric-label {
        font-size: 0.875rem;
        color: #605A57;
    }
    
    /* Divider styling */
    hr {
        border: none;
        border-top: 1px solid rgba(55, 50, 47, 0.12);
        margin: 2rem 0;
    }
    
    /* Logo cloud */
    .logo-placeholder {
        background: rgba(55, 50, 47, 0.08);
        border-radius: 4px;
        padding: 1rem 2rem;
        text-align: center;
        color: #605A57;
        font-weight: 500;
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
        font-size: 2rem;
        font-weight: 600;
        color: #49423D;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    
    .upload-subheader {
        font-size: 1rem;
        color: #605A57;
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    
    .result-container {
        background: #F7F5F3;
        border: 1px solid #E0DEDB;
        border-radius: 12px;
        padding: 2rem;
        margin-top: 2rem;
    }
    
    .result-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #37322F;
        margin-bottom: 1.5rem;
    }
    
    .classification-box {
        background: white;
        border: 1px solid #E0DEDB;
        border-radius: 8px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    
    .classification-label {
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
        font-size: 1.125rem;
        font-weight: 600;
        color: #49423D;
        margin-bottom: 1rem;
    }
    
    .recommendation-text {
        font-size: 0.9375rem;
        color: #605A57;
        line-height: 1.7;
    }
    
    /* File uploader styling */
    [data-testid="stFileUploader"] {
        background: #F7F5F3;
        border: 2px dashed #E0DEDB;
        border-radius: 8px;
        padding: 2rem;
    }
    
    [data-testid="stFileUploader"]:hover {
        border-color: #37322F;
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
</style>
""", unsafe_allow_html=True)


# ============== HEADER ==============
def render_header():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.markdown("### Brillance")
    with col2:
        header_cols = st.columns(3)
        with header_cols[0]:
            st.markdown("<p style='text-align: center; color: rgba(49, 45, 43, 0.80); font-size: 0.875rem;'>Products</p>", unsafe_allow_html=True)
        with header_cols[1]:
            st.markdown("<p style='text-align: center; color: rgba(49, 45, 43, 0.80); font-size: 0.875rem;'>Pricing</p>", unsafe_allow_html=True)
        with header_cols[2]:
            st.markdown("<p style='text-align: center; color: rgba(49, 45, 43, 0.80); font-size: 0.875rem;'>Docs</p>", unsafe_allow_html=True)
    with col3:
        st.button("Log in", key="login_btn")
    
    st.markdown("<hr>", unsafe_allow_html=True)


# ============== HERO SECTION ==============
def render_hero():
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown("""
    <h1 class="hero-title">
        Effortless custom contract<br>billing by Brillance
    </h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <p class="hero-subtitle">
        Streamline your billing process with seamless automation
        for every custom contract, tailored by Brillance.
    </p>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Start for free", key="hero_cta", use_container_width=True):
            st.session_state.current_page = 'upload'
            st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Dashboard preview placeholder
    st.image("images/dsadsadsa.jpeg", 
             caption="", use_container_width=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)


# ============== FEATURE CARDS ==============
def render_feature_cards():
    st.markdown("<br>", unsafe_allow_html=True)
    
    features = [
        {
            "title": "Plan your schedules",
            "description": "Streamline customer subscriptions and billing with automated scheduling tools."
        },
        {
            "title": "Analytics & insights",
            "description": "Transform your business data into actionable insights with real-time analytics."
        },
        {
            "title": "Collaborate seamlessly",
            "description": "Keep your team aligned with shared dashboards and collaborative workflows."
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


# ============== SOCIAL PROOF ==============
def render_social_proof():
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown('<div style="text-align: center;"><span class="section-badge">Social Proof</span></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Confidence backed by results</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-description">Our customers achieve more each day because their tools are simple, powerful, and clear.</p>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Logo cloud
    logo_cols = st.columns(4)
    companies = ["Acme Corp", "TechFlow", "InnovateCo", "DataSync"]
    for i, company in enumerate(companies):
        with logo_cols[i]:
            st.markdown(f'<div class="logo-placeholder">{company}</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    logo_cols2 = st.columns(4)
    companies2 = ["CloudBase", "Nexus AI", "Quantum", "Horizon"]
    for i, company in enumerate(companies2):
        with logo_cols2[i]:
            st.markdown(f'<div class="logo-placeholder">{company}</div>', unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)


# ============== METRICS ==============
def render_metrics():
    st.markdown("<br>", unsafe_allow_html=True)
    
    metrics = [
        {"value": "99.9%", "label": "Uptime guaranteed"},
        {"value": "50K+", "label": "Active users"},
        {"value": "150+", "label": "Integrations"},
        {"value": "24/7", "label": "Support available"}
    ]
    
    cols = st.columns(4)
    for i, metric in enumerate(metrics):
        with cols[i]:
            st.markdown(f"""
            <div style="text-align: center; padding: 1.5rem;">
                <div class="metric-value">{metric['value']}</div>
                <div class="metric-label">{metric['label']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)


# ============== TESTIMONIALS ==============
def render_testimonials():
    st.markdown("<br>", unsafe_allow_html=True)
    
    testimonials = [
        {
            "quote": "In just a few minutes, we transformed our data into actionable insights. The process was seamless and incredibly efficient!",
            "name": "Jamie Marshall",
            "company": "Co-founder, Exponent",
            "image": "images/chatgpt-20image-20sep-2011-2c-202025-2c-2011-35-19-20am.png"
        },
        {
            "quote": "Brillance has revolutionized how we handle custom contracts. The automation saves us hours every week and eliminates errors completely.",
            "name": "Sarah Chen",
            "company": "VP Operations, TechFlow",
            "image": "images/chatgpt-20image-20sep-2011-2c-202025-2c-2010-54-18-20am.png"
        },
        {
            "quote": "The billing automation is a game-changer. What used to take our team days now happens automatically with perfect accuracy.",
            "name": "Marcus Rodriguez",
            "company": "Finance Director, InnovateCorp",
            "image": "images/chatgpt-20image-20sep-2011-2c-202025-2c-2011-01-05-20am.png"
        }
    ]
    
    # Use session state to track active testimonial
    if 'active_testimonial' not in st.session_state:
        st.session_state.active_testimonial = 0
    
    testimonial = testimonials[st.session_state.active_testimonial]
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(testimonial["image"], width=200)
    
    with col2:
        st.markdown(f'<p class="testimonial-quote">"{testimonial["quote"]}"</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="testimonial-author">{testimonial["name"]}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="testimonial-company">{testimonial["company"]}</p>', unsafe_allow_html=True)
    
    # Navigation buttons
    nav_col1, nav_col2, nav_col3 = st.columns([2, 1, 2])
    with nav_col2:
        btn_cols = st.columns(2)
        with btn_cols[0]:
            if st.button("←", key="prev_testimonial"):
                st.session_state.active_testimonial = (st.session_state.active_testimonial - 1) % len(testimonials)
                st.rerun()
        with btn_cols[1]:
            if st.button("→", key="next_testimonial"):
                st.session_state.active_testimonial = (st.session_state.active_testimonial + 1) % len(testimonials)
                st.rerun()
    
    st.markdown("<hr>", unsafe_allow_html=True)


# ============== PRICING ==============
def render_pricing():
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown('<div style="text-align: center;"><span class="section-badge">Plans & Pricing</span></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Choose the perfect plan for your business</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-description">Scale your operations with flexible pricing that grows with your team. Start free, upgrade when you\'re ready.</p>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Billing toggle
    billing_col1, billing_col2, billing_col3 = st.columns([1, 1, 1])
    with billing_col2:
        billing_period = st.radio(
            "Billing Period",
            ["Annually", "Monthly"],
            horizontal=True,
            label_visibility="collapsed"
        )
    
    is_annual = billing_period == "Annually"
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    pricing_data = {
        "starter": {"monthly": 0, "annually": 0},
        "professional": {"monthly": 20, "annually": 16},
        "enterprise": {"monthly": 200, "annually": 160}
    }
    
    col1, col2, col3 = st.columns(3)
    
    # Starter Plan
    with col1:
        price = pricing_data["starter"]["annually" if is_annual else "monthly"]
        st.markdown(f"""
        <div class="pricing-card">
            <h3>Starter</h3>
            <p style="color: rgba(41, 37, 35, 0.70); font-size: 0.875rem;">Perfect for individuals and small teams getting started.</p>
            <div class="price">${price}</div>
            <p style="color: #847971; font-size: 0.875rem;">per {'year' if is_annual else 'month'}, per user.</p>
            <ul class="features">
                <li>✓ Up to 3 projects</li>
                <li>✓ Basic documentation tools</li>
                <li>✓ Community support</li>
                <li>✓ Standard templates</li>
                <li>✓ Basic analytics</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.button("Start for free", key="starter_btn", use_container_width=True)
    
    # Professional Plan
    with col2:
        price = pricing_data["professional"]["annually" if is_annual else "monthly"]
        st.markdown(f"""
        <div class="pricing-card featured">
            <h3>Professional</h3>
            <p style="color: #B2AEA9; font-size: 0.875rem;">Advanced features for growing teams and businesses.</p>
            <div class="price">${price}</div>
            <p style="color: #D2C6BF; font-size: 0.875rem;">per {'year' if is_annual else 'month'}, per user.</p>
            <ul class="features">
                <li>✓ Unlimited projects</li>
                <li>✓ Advanced documentation tools</li>
                <li>✓ Priority support</li>
                <li>✓ Custom templates</li>
                <li>✓ Advanced analytics</li>
                <li>✓ Team collaboration</li>
                <li>✓ API access</li>
                <li>✓ Custom integrations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.button("Get started", key="pro_btn", use_container_width=True)
    
    # Enterprise Plan
    with col3:
        price = pricing_data["enterprise"]["annually" if is_annual else "monthly"]
        st.markdown(f"""
        <div class="pricing-card">
            <h3>Enterprise</h3>
            <p style="color: rgba(41, 37, 35, 0.70); font-size: 0.875rem;">Complete solution for large organizations and enterprises.</p>
            <div class="price">${price}</div>
            <p style="color: #847971; font-size: 0.875rem;">per {'year' if is_annual else 'month'}, per user.</p>
            <ul class="features">
                <li>✓ Everything in Professional</li>
                <li>✓ Dedicated account manager</li>
                <li>✓ 24/7 phone support</li>
                <li>✓ Custom onboarding</li>
                <li>✓ Advanced security features</li>
                <li>✓ SSO integration</li>
                <li>✓ Custom contracts</li>
                <li>✓ White-label options</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.button("Contact sales", key="enterprise_btn", use_container_width=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)


# ============== FAQ ==============
def render_faq():
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<h2 style="font-size: 2rem; font-weight: 600; color: #49423D; letter-spacing: -0.02em;">Frequently Asked Questions</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color: #605A57; font-size: 1rem;">Explore your data, build your dashboard, bring your team together.</p>', unsafe_allow_html=True)
    
    with col2:
        faq_data = [
            {
                "question": "What is Brillance and who is it for?",
                "answer": "Brillance is a comprehensive billing automation platform designed for businesses that need custom contract management. It's perfect for SaaS companies, service providers, and enterprises looking to streamline their billing processes."
            },
            {
                "question": "How does the custom contract billing work?",
                "answer": "Our platform automatically processes your custom contracts, calculates billing amounts based on your specific terms, and generates invoices. You can set up complex pricing structures, usage-based billing, and custom billing cycles."
            },
            {
                "question": "Can I integrate Brillance with my existing tools?",
                "answer": "Yes! Brillance integrates seamlessly with popular CRM systems, accounting software, and payment processors. We support APIs and webhooks for custom integrations with your existing workflow."
            },
            {
                "question": "What kind of support do you provide?",
                "answer": "We offer 24/7 customer support, dedicated account managers for enterprise clients, comprehensive documentation, and onboarding assistance to help you get started quickly."
            },
            {
                "question": "Is my data secure with Brillance?",
                "answer": "Absolutely. We use enterprise-grade security measures including end-to-end encryption, SOC 2 compliance, and regular security audits. Your data is stored in secure, redundant data centers."
            },
            {
                "question": "How do I get started with Brillance?",
                "answer": "Getting started is simple! Sign up for our free trial, connect your existing systems, and our onboarding team will help you set up your first custom billing workflow within 24 hours."
            }
        ]
        
        for faq in faq_data:
            with st.expander(faq["question"]):
                st.markdown(f'<p class="faq-answer">{faq["answer"]}</p>', unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)


# ============== CTA SECTION ==============
def render_cta():
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; padding: 3rem 0;">
        <h2 style="font-size: 2.5rem; font-weight: 600; color: #49423D; margin-bottom: 1rem; letter-spacing: -0.02em;">
            Ready to transform your billing?
        </h2>
        <p style="color: #605A57; font-size: 1.1rem; max-width: 500px; margin: 0 auto 2rem auto;">
            Join thousands of businesses that trust Brillance for their custom contract billing needs.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    cta_col1, cta_col2, cta_col3 = st.columns([1, 1, 1])
    with cta_col2:
        if st.button("Get started today", key="cta_btn", use_container_width=True):
            st.session_state.current_page = 'upload'
            st.rerun()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)


# ============== FOOTER ==============
def render_footer():
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns([1.5, 1, 1, 1])
    
    with col1:
        st.markdown('<p class="footer-brand">Brillance</p>', unsafe_allow_html=True)
        st.markdown('<p class="footer-tagline">Coding made effortless</p>', unsafe_allow_html=True)
        st.markdown("""
        <div style="display: flex; gap: 1rem; margin-top: 1rem;">
            <span style="color: #49423D;">𝕏</span>
            <span style="color: #49423D;">in</span>
            <span style="color: #49423D;">⌘</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<p class="footer-heading">Product</p>', unsafe_allow_html=True)
        for link in ["Features", "Pricing", "Integrations", "Real-time Previews", "Multi-Agent Coding"]:
            st.markdown(f'<a href="#" class="footer-link">{link}</a>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<p class="footer-heading">Company</p>', unsafe_allow_html=True)
        for link in ["About us", "Our team", "Careers", "Brand", "Contact"]:
            st.markdown(f'<a href="#" class="footer-link">{link}</a>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<p class="footer-heading">Resources</p>', unsafe_allow_html=True)
        for link in ["Terms of use", "API Reference", "Documentation", "Community", "Support"]:
            st.markdown(f'<a href="#" class="footer-link">{link}</a>', unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)


# ============== UPLOAD & PREDICTION PAGE ==============
def render_upload_page():
    # Back button
    if st.button("← Back to Home", key="back_btn"):
        st.session_state.current_page = 'landing'
        st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Header section
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
    
    # Main content
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
            
            # Guidelines
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
                with st.spinner("Analyzing your image..."):
                    # TODO: Add actual model prediction here
                    import time
                    time.sleep(2)
                    
                    # Store results in session state
                    st.session_state.prediction_result = {
                        "disease": "Apple Scab",
                        "confidence": 94.5,
                        "severity": "Moderate",
                        "recommendation": """Based on the analysis, your plant shows signs of Apple Scab, a fungal disease. Here are the recommended steps:

**Immediate Actions:**
• Remove and destroy all infected leaves to prevent spread
• Improve air circulation around the plant by pruning dense foliage
• Avoid overhead watering; water at the base of the plant instead

**Treatment Plan:**
• Apply a fungicide containing captan or mancozeb every 7-10 days
• Continue treatment for 3-4 weeks or until symptoms improve
• Ensure proper spacing between plants for better air flow

**Prevention:**
• Remove fallen leaves and debris regularly
• Apply preventive fungicide spray in early spring
• Choose disease-resistant varieties for future plantings
• Maintain consistent watering schedule

**When to Seek Expert Help:**
If the condition worsens despite treatment or spreads to other plants, consult a local agricultural extension office or plant pathologist for specialized assistance."""
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
            
            # Classification Result
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
            
            # Recommendations
            st.markdown(f"""
            <div class="recommendation-box">
                <div class="recommendation-title">Treatment Recommendations</div>
                <div class="recommendation-text">{result['recommendation']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Action buttons
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
            <div class="recommendation-box" style="margin-top: 1.5rem;">
                <div class="recommendation-title">Why Choose Our AI?</div>
                <ul style="font-size: 0.875rem; color: #605A57; line-height: 1.8; margin: 0; padding-left: 1.25rem;">
                    <li>95%+ accuracy rate on disease detection</li>
                    <li>Instant analysis in under 3 seconds</li>
                    <li>AI-powered treatment recommendations</li>
                    <li>Trained on thousands of plant disease images</li>
                    <li>Regular model updates for improved accuracy</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)


# ============== MAIN APP ==============
def main():
    if st.session_state.current_page == 'landing':
        render_header()
        render_hero()
        render_feature_cards()
        render_social_proof()
        render_metrics()
        render_testimonials()
        render_pricing()
        render_faq()
        render_cta()
        render_footer()
    elif st.session_state.current_page == 'upload':
        render_upload_page()


if __name__ == "__main__":
    main()
