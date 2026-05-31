import streamlit as st
import joblib

# Load the trained model and vectorizer
@st.cache_resource
def load_assets():
    model = joblib.load("spam_model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_assets()

#page config 
st.set_page_config(
    page_title="Mail Guard",
    page_icon="📧",
    layout="centered",
)

#ui
st.markdown("""
<style>
    body {
        background-color: #fff !important;
        color: #102a43 !important;
    }
    .main, .block-container {
        background-color: #fff !important;
        color: #102a43 !important;
    }
    .title {
        font-size: 2.6rem;
        font-weight: 800;
        color: #102a43;
        margin-block-start: 20px;
    }   
    .subtitle {
        text-align: center;
        color: #2563eb;
        margin-block-end:25px;
        font-size: 1rem;
    }
.title {
    font-size: 2.6rem;
    font-weight: 800;
    color: #2563eb;
    text-align: center;
    margin-block-start: 20px;
}

.subtitle {
text-align: center;
color: #6b7280;
margin-block-end:25px;
font-size: 1rem;
}

.card {
background-color: white;
border: 1px solid #e5e7eb;
border-radius: 14px;
padding: 18px;
box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
margin-block-start: 15px;
}

textarea {
border-radius : 10px !important;
border: 1px solid #d1d5db !important;
}

/* Button */
.stButton > button {
    inline-size: 100%;
    background-color: #2563eb;
    color: white;
    font-weight: 600;
    border-radius: 10px;
    padding: 10px;
    border: none;
}

.spam {
    background-color: #fee2e2;
    border: 1px solid #ef4444;
    color: #b91c1c;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    font-weight: 700;
}
.ham {
    background-color: #ecfdf5;
    border: 1px solid #22c55e;
    color: #166534;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    font-weight: 700;
}

.example-btn {
margin: 5px;
}
</style>
""", unsafe_allow_html=True)

# header
st.markdown('<div class="title">Mail Guard</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Detect Spam Emails instantly using Machine Learning (Naive Bayes + TF-IDF)</div>',
    unsafe_allow_html=True
)

#examples 
st.markdown("###  Try Example Emails")

examples = {
    "Spam Offer": "Congratulations! You won a $1000 gift card. Click here to claim now!",
    "Phishing Email": "Your bank account is locked. Please login immediately to verify your identity.",
    "Normal Email": "Hey, I will send the report by tomorrow. Let me know if any changes are needed."
}
cols = st.columns(len(examples))
for col, (title, text) in zip(cols, examples.items()):
    if col.button(title):
        st.session_state.email_input = text

#input 
email = st.text_area("Enter email content",
value=st.session_state.get("email_input", ""),
height=200,
placeholder="Type or paste email content here...")

#word count 
word_count = len(email.split()) if email else 0

st.markdown(f"**Word Count:** {word_count}")

if word_count > 0 and word_count < 10:
    st.warning("very short input. results may be less accurate.")

#predict 
if st.button("analyze email"):
    if not email.strip():
        st.warning("please enter email content")
    else:
        X = vectorizer.transform([email])
        pred = model.predict(X)[0]
        prob = model.predict_proba(X)[0]
        
        spam_conf = prob[1]
        ham_conf = prob[0]

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        if pred == 1:
            st.markdown(f"""
            <div class="spam">
            <h3>Spam Detected</h3>
            <p>Confidence: {spam_conf:.2%}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="ham">
            <h3>Not Spam (Ham)</h3>
            <p>Confidence: {ham_conf:.2%}</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)


# --- FOOTER SECTION (FIXED) ---

# १. CSS लाई छुट्टै राख्ने (यसमा कुनै स्पेसको लफडा हुँदैन)
footer_css = """
<style>
.custom-footer {
    text-align: center;
    padding: 25px 10px;
    color: #6b7280;
    font-size: 0.85rem;
    border-block-start: 1px solid #e5e7eb !important;
    margin-block-start: 40px !important;
    display: block !important;
}
.social-icons {
    margin-block-start: 10px !important;
}
.social-icons a {
    margin: 0 10px;
    text-decoration: none;
    font-size: 1rem;
    color: #2563eb;
    transition: 0.2s;
}
.social-icons a:hover {
    color: #1d4ed8;
}
</style>
"""

# २. HTML स्ट्रक्चर मात्र छुट्टै राख्ने
footer_html = """
<div class="custom-footer">
    <div>Built with ❤️ by <b>Birendra Joshi</b></div>
    <div class="social-icons">
        <a href="https://github.com/Birendra-Joshi" target="_blank">GitHub</a>
        <a href="https://www.linkedin.com/in/birendra-joshi-96087136b" target="_blank">LinkedIn</a>
        <a href="https://www.instagram.com/stm_no_mercy" target="_blank">Instagram</a>
        <a href="https://www.facebook.com/dev.birendra1/" target="_blank">Facebook</a>
    </div>
    <p style="margin-block-start: 10px;">Mail Guard • Spam Email Detection using Machine Learning</p>
</div>
"""

# ३. यसरी रन गर्ने (कुनै पनि लाइनको अगाडि space/tab नराख्नुहोला)
st.markdown(footer_css, unsafe_allow_html=True)
st.markdown(footer_html, unsafe_allow_html=True)