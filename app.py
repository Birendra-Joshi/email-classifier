import streamlit as st
import joblib
from pathlib import Path

# ----------------------------------------------------------------------------
# Page configuration
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Mail Guard | AI Spam Detection",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------------
# Asset loading
# ----------------------------------------------------------------------------
@st.cache_resource(show_spinner=False)
def load_assets():
    """Load the trained model and vectorizer, failing gracefully if missing."""
    model_path = Path("spam_model.pkl")
    vectorizer_path = Path("vectorizer.pkl")

    if not model_path.exists() or not vectorizer_path.exists():
        return None, None

    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    return model, vectorizer


model, vectorizer = load_assets()

# ----------------------------------------------------------------------------
# Styling
# ----------------------------------------------------------------------------
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    .stApp {
        background-color: #f9fafb;
    }

    .block-container {
        padding-top: 2.5rem;
        max-width: 720px;
    }

    /* Header */
    .app-title {
        font-size: 2.4rem;
        font-weight: 800;
        color: #111827;
        text-align: center;
        letter-spacing: -0.02em;
        margin-bottom: 0.25rem;
    }
    .app-title span {
        color: #2563eb;
    }
    .app-subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 1rem;
        margin-bottom: 2rem;
    }

    /* Section labels */
    .section-label {
        font-size: 0.85rem;
        font-weight: 700;
        color: #374151;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin: 1.5rem 0 0.6rem 0;
    }

    /* Card */
    .card {
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 20px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
        margin-top: 1rem;
    }

    /* Text area */
    textarea {
        border-radius: 10px !important;
        border: 1px solid #d1d5db !important;
        font-family: 'DM Sans', sans-serif !important;
    }

    /* Primary button */
    .stButton > button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        font-weight: 600;
        border-radius: 10px;
        padding: 10px;
        border: none;
        transition: background-color 0.15s ease;
    }
    .stButton > button:hover {
        background-color: #1d4ed8;
        color: white;
    }

    /* Result banners */
    .result-banner {
        padding: 18px;
        border-radius: 12px;
        text-align: center;
        margin-top: 0.5rem;
    }
    .result-banner h3 {
        margin: 0 0 4px 0;
        font-size: 1.15rem;
    }
    .result-banner p {
        margin: 0;
        font-size: 0.95rem;
        opacity: 0.85;
    }
    .spam {
        background-color: #fef2f2;
        border: 1px solid #fecaca;
        color: #b91c1c;
    }
    .ham {
        background-color: #ecfdf5;
        border: 1px solid #a7f3d0;
        color: #166534;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e5e7eb;
    }
    .sidebar-stat {
        background-color: #f9fafb;
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        padding: 12px 14px;
        margin-bottom: 10px;
    }
    .sidebar-stat .label {
        font-size: 0.75rem;
        color: #6b7280;
        text-transform: uppercase;
        letter-spacing: 0.03em;
    }
    .sidebar-stat .value {
        font-size: 1.1rem;
        font-weight: 700;
        color: #111827;
    }

    /* Footer */
    .custom-footer {
        text-align: center;
        padding: 25px 10px;
        color: #9ca3af;
        font-size: 0.82rem;
        border-top: 1px solid #e5e7eb;
        margin-top: 40px;
    }
    .social-icons a {
        margin: 0 10px;
        text-decoration: none;
        font-size: 0.85rem;
        color: #2563eb;
        font-weight: 500;
    }
    .social-icons a:hover {
        color: #1d4ed8;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# Sidebar — model info
# ----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🛡️ Mail Guard")
    st.caption("AI-powered spam detection")
    st.markdown("---")
    st.markdown("**Model details**")

    st.markdown(
        """
        <div class="sidebar-stat">
            <div class="label">Algorithm</div>
            <div class="value">Naive Bayes</div>
        </div>
        <div class="sidebar-stat">
            <div class="label">Feature Extraction</div>
            <div class="value">TF-IDF Vectorizer</div>
        </div>
        <div class="sidebar-stat">
            <div class="label">Status</div>
            <div class="value">{}</div>
        </div>
        """.format("Model loaded ✅" if model is not None else "Model not found ⚠️"),
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.caption("Enter or paste email content in the main panel to check whether it's spam or legitimate.")

# ----------------------------------------------------------------------------
# Header
# ----------------------------------------------------------------------------
st.markdown('<div class="app-title">Mail <span>Guard</span></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="app-subtitle">Detect spam emails instantly using Machine Learning (Naive Bayes + TF-IDF)</div>',
    unsafe_allow_html=True,
)

if model is None or vectorizer is None:
    st.error(
        "Model files (`spam_model.pkl`, `vectorizer.pkl`) were not found. "
        "Please make sure they're in the app's working directory."
    )
    st.stop()

# ----------------------------------------------------------------------------
# Example emails
# ----------------------------------------------------------------------------
st.markdown('<div class="section-label">Try an example</div>', unsafe_allow_html=True)

examples = {
    "Spam offer": "Congratulations! You won a $1000 gift card. Click here to claim now!",
    "Phishing email": "Your bank account is locked. Please login immediately to verify your identity.",
    "Normal email": "Hey, I will send the report by tomorrow. Let me know if any changes are needed.",
}

cols = st.columns(len(examples))
for col, (title, text) in zip(cols, examples.items()):
    if col.button(title, use_container_width=True):
        st.session_state.email_input = text

# ----------------------------------------------------------------------------
# Input
# ----------------------------------------------------------------------------
st.markdown('<div class="section-label">Email content</div>', unsafe_allow_html=True)

email = st.text_area(
    "Enter email content",
    value=st.session_state.get("email_input", ""),
    height=200,
    placeholder="Type or paste email content here...",
    label_visibility="collapsed",
)

word_count = len(email.split()) if email else 0
st.caption(f"Word count: {word_count}")

if 0 < word_count < 10:
    st.warning("Very short input — results may be less accurate.")

# ----------------------------------------------------------------------------
# Prediction
# ----------------------------------------------------------------------------
if st.button("Analyze Email"):
    if not email.strip():
        st.warning("Please enter email content.")
    else:
        X = vectorizer.transform([email])
        pred = model.predict(X)[0]
        prob = model.predict_proba(X)[0]

        spam_conf = prob[1]
        ham_conf = prob[0]

        st.markdown('<div class="card">', unsafe_allow_html=True)

        if pred == 1:
            st.markdown(f"""
            <div class="result-banner spam">
                <h3>⚠️ Spam Detected</h3>
                <p>Confidence: {spam_conf:.1%}</p>
            </div>
            """, unsafe_allow_html=True)
            st.progress(float(spam_conf))
        else:
            st.markdown(f"""
            <div class="result-banner ham">
                <h3>✅ Not Spam (Ham)</h3>
                <p>Confidence: {ham_conf:.1%}</p>
            </div>
            """, unsafe_allow_html=True)
            st.progress(float(ham_conf))

        st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# Footer
# ----------------------------------------------------------------------------
st.markdown("""
<div class="custom-footer">
    <div>Built with ❤️ by <b>Birendra Joshi</b></div>
    <div class="social-icons">
        <a href="https://github.com/Birendra-Joshi" target="_blank">GitHub</a>
        <a href="https://www.linkedin.com/in/birendra-joshi-96087136b" target="_blank">LinkedIn</a>
        <a href="https://www.instagram.com/stm_no_mercy" target="_blank">Instagram</a>
        <a href="https://www.facebook.com/dev.birendra1/" target="_blank">Facebook</a>
    </div>
    <p style="margin-top: 10px;">Mail Guard • Spam Email Detection using Machine Learning</p>
</div>
""", unsafe_allow_html=True)
