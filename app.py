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
st.app{
background-color: #f7f9fc;
color: #111827;
}
.title {
font-size: 2.6rem;
font-weight: 800;
color: #2563eb;
margin-block-start: 20px;
}   

.subtitle {
text-align: center;
color: #6b7280;
margin-block-end:25px;
fonrt-size: 1rem;
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
    border: 1px solid #f;
}











# Simple UI
st.markdown('<div class="title">Mail Guard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Detect whether an email is spam or not</div>', unsafe_allow_html=True)

with st.container():
    st.text_area('Enter email text', key='email_text', height=200)
    if st.button('Predict'):
        text = st.session_state.email_text
        X = vectorizer.transform([text])
        pred = model.predict(X)[0]
        label = 'SPAM' if pred == 1 else 'HAM'
        st.success(f'Prediction: {label}')
