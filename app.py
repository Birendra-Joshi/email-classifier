import streamlit as st
import joblib
import math
from pathlib import Path

# ==============================================================================
# CONCEPT: MAIL::GUARD reimagined as a signal-intelligence console.
# Every inbound email is treated as an intercepted "transmission" that gets
# scanned, classified, and logged — like a SIGINT terminal, not a form.
# ==============================================================================

st.set_page_config(
    page_title="MAIL::GUARD — Transmission Scanner",
    page_icon="📡",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ------------------------------------------------------------------------------
# Assets
# ------------------------------------------------------------------------------
@st.cache_resource(show_spinner=False)
def load_assets():
    model_path = Path("spam_model.pkl")
    vectorizer_path = Path("vectorizer.pkl")
    if not model_path.exists() or not vectorizer_path.exists():
        return None, None
    return joblib.load(model_path), joblib.load(vectorizer_path)


model, vectorizer = load_assets()


def threat_level(conf: float):
    """Bucket spam confidence into an escalation ladder — real signal, not decoration."""
    if conf >= 0.95:
        return "CRITICAL", "#f87171", "immediate malicious intent detected"
    elif conf >= 0.80:
        return "HIGH", "#fb923c", "strong spam signature match"
    else:
        return "ELEVATED", "#fbbf24", "suspicious pattern, low certainty"


def waveform_svg(confidence: float, color: str, seed: int = 7):
    """Amplitude of the waveform is driven by the actual confidence score."""
    width, height, mid = 620, 90, 45
    amplitude = 6 + confidence * 34
    points = []
    n = 90
    for i in range(n + 1):
        x = width * i / n
        # layered sine for an organic "signal" look, damped at the edges
        edge_damp = math.sin(math.pi * i / n)
        y = mid + edge_damp * amplitude * math.sin(i * 0.9 + seed) * math.sin(i * 0.17)
        points.append(f"{x:.1f},{y:.1f}")
    path = " ".join(points)
    return f"""
    <svg viewBox="0 0 {width} {height}" width="100%" height="{height}" preserveAspectRatio="none">
        <polyline points="{path}" fill="none" stroke="{color}" stroke-width="2"
            stroke-linecap="round" stroke-linejoin="round" opacity="0.9"/>
        <line x1="0" y1="{mid}" x2="{width}" y2="{mid}" stroke="{color}" stroke-width="0.5" opacity="0.15"/>
    </svg>
    """


# ------------------------------------------------------------------------------
# Style system
# ------------------------------------------------------------------------------
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>

:root {
    --bg: #0a0e0c;
    --panel: #101613;
    --border: #22302a;
    --text: #d8e6df;
    --dim: #6b8177;
    --amber: #fbbf24;
    --green: #4ade80;
    --red: #f87171;
}

html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif; }
code, .mono, .app-title, .cmd-line, .stButton>button, textarea,
.sidebar-row, .example-tag, .banner-title, .banner-conf, .footer-cmd {
    font-family: 'JetBrains Mono', monospace !important;
}

.stApp {
    background-color: var(--bg);
    background-image:
        repeating-linear-gradient(180deg, rgba(255,255,255,0.015) 0px, rgba(255,255,255,0.015) 1px, transparent 1px, transparent 3px);
    color: var(--text);
}

.block-container { padding-top: 2.2rem; max-width: 700px; }

/* Header */
.app-title {
    font-size: 2rem;
    font-weight: 700;
    letter-spacing: 0.03em;
    color: var(--green);
    text-shadow: 0 0 18px rgba(74, 222, 128, 0.35);
    margin-bottom: 0.3rem;
}
.app-title .sep { color: var(--dim); }
.cmd-line {
    color: var(--dim);
    font-size: 0.85rem;
    margin-bottom: 1.8rem;
}
.cmd-line::after {
    content: "▊";
    animation: blink 1.1s steps(1) infinite;
    margin-left: 2px;
}
@keyframes blink { 50% { opacity: 0; } }

/* Section eyebrows */
.eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    color: var(--dim);
    margin: 1.6rem 0 0.6rem 0;
    text-transform: uppercase;
}
.eyebrow::before { content: "// "; color: var(--border); }

/* Sample transmission tags */
.stButton > button {
    background-color: var(--panel);
    color: var(--text);
    border: 1px solid var(--border);
    border-radius: 4px;
    font-size: 0.78rem;
    padding: 8px 10px;
    transition: all 0.15s ease;
}
.stButton > button:hover {
    border-color: var(--green);
    color: var(--green);
    background-color: rgba(74, 222, 128, 0.06);
}

/* Text area = terminal input */
textarea {
    background-color: var(--panel) !important;
    color: var(--green) !important;
    border: 1px solid var(--border) !important;
    border-radius: 4px !important;
    font-size: 0.9rem !important;
}
textarea:focus {
    border-color: var(--green) !important;
    box-shadow: 0 0 0 1px rgba(74, 222, 128, 0.3) !important;
}

/* Scan button — primary action, distinct from sample tags */
div[data-testid="stButton"]:has(button[kind="primary"]) button,
button[kind="primary"] {
    background-color: rgba(74, 222, 128, 0.08) !important;
    border: 1px solid var(--green) !important;
    color: var(--green) !important;
    font-weight: 600 !important;
    letter-spacing: 0.05em;
}
button[kind="primary"]:hover {
    background-color: rgba(74, 222, 128, 0.18) !important;
    box-shadow: 0 0 20px rgba(74, 222, 128, 0.25) !important;
}

/* Result panel */
.report-card {
    background-color: var(--panel);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 22px;
    margin-top: 1rem;
}
.banner-title {
    font-size: 1.3rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    margin-bottom: 2px;
}
.banner-sub {
    font-size: 0.82rem;
    color: var(--dim);
    margin-bottom: 14px;
}
.banner-conf {
    font-size: 0.85rem;
    color: var(--text);
    margin-top: 10px;
}
.led {
    display: inline-block;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    margin-right: 8px;
    box-shadow: 0 0 8px currentColor;
    animation: pulse 1.6s ease-in-out infinite;
}
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.35; } }

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0c1210;
    border-right: 1px solid var(--border);
}
.sidebar-title {
    font-family: 'JetBrains Mono', monospace;
    color: var(--green);
    font-size: 0.95rem;
    letter-spacing: 0.05em;
    margin-bottom: 2px;
}
.sidebar-sub { color: var(--dim); font-size: 0.75rem; margin-bottom: 14px; }
.sidebar-row {
    display: flex;
    justify-content: space-between;
    font-size: 0.78rem;
    padding: 7px 0;
    border-bottom: 1px dashed var(--border);
}
.sidebar-row .k { color: var(--dim); }
.sidebar-row .v { color: var(--text); }

/* Footer */
.footer {
    margin-top: 46px;
    padding-top: 18px;
    border-top: 1px solid var(--border);
    text-align: center;
    color: var(--dim);
    font-size: 0.78rem;
}
.footer-cmd a {
    color: var(--dim);
    text-decoration: none;
    margin: 0 8px;
}
.footer-cmd a:hover { color: var(--green); }

@media (max-width: 480px) {
    .app-title { font-size: 1.5rem; }
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# Sidebar — system diagnostics
# ------------------------------------------------------------------------------
with st.sidebar:
    st.markdown('<div class="sidebar-title">MAIL::GUARD</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-sub">signal intelligence console</div>', unsafe_allow_html=True)

    online = model is not None
    led_color = "var(--green)" if online else "var(--red)"
    status_text = "ONLINE" if online else "OFFLINE"

    st.markdown(f"""
    <div class="sidebar-row"><span class="k">LINK STATUS</span>
        <span class="v"><span class="led" style="background:{led_color};color:{led_color}"></span>{status_text}</span></div>
    <div class="sidebar-row"><span class="k">CLASSIFIER</span><span class="v">Naive Bayes</span></div>
    <div class="sidebar-row"><span class="k">FEATURE MAP</span><span class="v">TF-IDF</span></div>
    <div class="sidebar-row"><span class="k">MODE</span><span class="v">Binary / spam-ham</span></div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.caption("Paste a transmission into the console and initiate a scan to classify it.")

# ------------------------------------------------------------------------------
# Header
# ------------------------------------------------------------------------------
st.markdown('<div class="app-title">MAIL<span class="sep">::</span>GUARD</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="cmd-line">$ tail -f /var/log/inbound &#124; classify --model=naive-bayes</div>',
    unsafe_allow_html=True,
)

if model is None or vectorizer is None:
    st.error(
        "LINK OFFLINE — model artifacts (`spam_model.pkl`, `vectorizer.pkl`) were not found "
        "in the working directory."
    )
    st.stop()

# ------------------------------------------------------------------------------
# Sample transmissions
# ------------------------------------------------------------------------------
st.markdown('<div class="eyebrow">sample transmissions</div>', unsafe_allow_html=True)

examples = {
    "spam offer": "Congratulations! You won a $1000 gift card. Click here to claim now!",
    "phishing": "Your bank account is locked. Please login immediately to verify your identity.",
    "clean": "Hey, I will send the report by tomorrow. Let me know if any changes are needed.",
}

cols = st.columns(len(examples))
for col, (title, text) in zip(cols, examples.items()):
    if col.button(f"[ {title} ]", use_container_width=True):
        st.session_state.email_input = text

# ------------------------------------------------------------------------------
# Input console
# ------------------------------------------------------------------------------
st.markdown('<div class="eyebrow">incoming transmission</div>', unsafe_allow_html=True)

email = st.text_area(
    "Transmission content",
    value=st.session_state.get("email_input", ""),
    height=190,
    placeholder="// paste or type email content to intercept...",
    label_visibility="collapsed",
)

word_count = len(email.split()) if email else 0
st.markdown(f'<span class="mono" style="color:var(--dim); font-size:0.78rem;">&gt; tokens: {word_count}</span>', unsafe_allow_html=True)

if 0 < word_count < 10:
    st.warning("Signal too short — classification confidence may be degraded.")

scan = st.button("INITIATE SCAN >", type="primary", use_container_width=True)

# ------------------------------------------------------------------------------
# Scan + report
# ------------------------------------------------------------------------------
if scan:
    if not email.strip():
        st.warning("No transmission detected. Paste content before scanning.")
    else:
        with st.spinner("Decrypting payload · cross-referencing token frequencies..."):
            X = vectorizer.transform([email])
            pred = model.predict(X)[0]
            prob = model.predict_proba(X)[0]

        spam_conf = float(prob[1])
        ham_conf = float(prob[0])

        if pred == 1:
            level, color, desc = threat_level(spam_conf)
            wave = waveform_svg(spam_conf, color)
            st.markdown(f"""
            <div class="report-card" style="border-color:{color}44;">
                <div class="banner-title" style="color:{color};">
                    <span class="led" style="background:{color};color:{color};"></span>
                    THREAT LEVEL: {level}
                </div>
                <div class="banner-sub">{desc}</div>
                {wave}
                <div class="banner-conf">spam probability &nbsp;<b style="color:{color}">{spam_conf:.1%}</b></div>
            </div>
            """, unsafe_allow_html=True)
        else:
            color = "#4ade80"
            wave = waveform_svg(ham_conf, color)
            st.markdown(f"""
            <div class="report-card" style="border-color:{color}44;">
                <div class="banner-title" style="color:{color};">
                    <span class="led" style="background:{color};color:{color};"></span>
                    THREAT LEVEL: CLEAR
                </div>
                <div class="banner-sub">no spam signature detected</div>
                {wave}
                <div class="banner-conf">legitimate probability &nbsp;<b style="color:{color}">{ham_conf:.1%}</b></div>
            </div>
            """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# Footer
# ------------------------------------------------------------------------------
st.markdown("""
<div class="footer">
    <div>built by <b style="color:var(--text)">Birendra Joshi</b></div>
    <div class="footer-cmd" style="margin-top:8px;">
        <a href="https://github.com/Birendra-Joshi" target="_blank">github</a>
        <a href="https://www.linkedin.com/in/birendra-joshi-96087136b" target="_blank">linkedin</a>
        <a href="https://www.instagram.com/stm_no_mercy" target="_blank">instagram</a>
        <a href="https://www.facebook.com/dev.birendra1/" target="_blank">facebook</a>
    </div>
    <div style="margin-top:10px; opacity:0.6;">// end transmission log</div>
</div>
""", unsafe_allow_html=True)
