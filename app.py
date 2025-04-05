import streamlit as st
import numpy as np
import random
import os
os.environ["STREAMLIT_DISABLE_WATCHDOG_WARNINGS"] = "true"
os.environ["PYTORCH_JIT"] = "0"  # Optional, for torch scripting


from PIL import Image
from model import generate_face  # Now uses real GAN
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
from auth import login
from dashboard import show_dashboard
from history import save_history
from chatbot import chatbot_ui

# Initialize session
if "user" not in st.session_state:
    st.session_state["user"] = None

# Login required
if not st.session_state["user"]:
    login()
    chatbot_ui()  # Show chatbot even on login page
    st.stop()

# Show chatbot always after login
chatbot_ui()

# --- PDF Report Generator ---
def generate_pdf(face_image, traits):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "AI Face Prediction Report")

    img_path = "face_temp.png"
    face_image.save(img_path)
    c.drawImage(img_path, 50, height - 300, width=200, height=200)

    c.setFont("Helvetica", 12)
    y = height - 320
    for trait, value in traits.items():
        c.drawString(270, y, f"{trait}: {value:.2f}")
        y -= 20

    c.save()
    buffer.seek(0)
    return buffer

# --- Session Setup ---
if "history" not in st.session_state:
    st.session_state["history"] = []

# --- Holi Styling ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap');
body {
    font-family: 'Poppins', sans-serif;
    background: url('https://img.freepik.com/premium-photo/abstract-watercolor-texture-holi-painting_920302-417.jpg');
    background-size: cover;
    background-attachment: fixed;
    text-align: center;
    margin: 0;
    padding: 0;
}
h1 {
    font-size: 50px;
    color: #ff0055;
    text-shadow: 3px 3px 5px yellow;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

st.title("\U0001F3A8 Holi Special AI Criminal Face Prediction \U0001F9EC")
st.image("https://www.shutterstock.com/image-vector/happy-holi-festival-colors-background-600nw-2142910233.jpg", width=600)
st.audio("https://www.fesliyanstudios.com/play-mp3/387", format="audio/mp3")

# --- Trait Legend ---
st.markdown("""
### \U0001F3AF Trait Legend (Simulated Genetic Markers)
| Gene     | Trait         | 0 = Min | 1 = Max |
|----------|---------------|--------|--------|
| OCA2     | Eye Color     | Blue   | Brown  |
| HERC2    | Eye Enhancer  | Low    | High   |
| MC1R     | Hair/Skin     | Blonde/Fair | Black/Dark |
| SLC24A5  | Skin Tone     | Light  | Dark   |
| EDAR     | Face Shape    | Round  | Angular |
""", unsafe_allow_html=True)

# --- Input DNA ---
if st.checkbox("\U0001F4A1 Load Sample DNA"):
    dna_samples = [
        [0.2, 0.3, 0.9, 0.8, 0.4],
        [0.9, 0.8, 0.1, 0.3, 0.7],
        [0.5, 0.5, 0.5, 0.5, 0.5],
    ]
    sample = random.choice(dna_samples)
    oca2, herc2, mc1r, slc24a5, edar = sample
    st.success(f"\U0001F52C Loaded Sample DNA: {sample}")
else:
    oca2 = st.slider("OCA2 (Eye Color)", 0.0, 1.0, 0.7)
    herc2 = st.slider("HERC2 (Eye Enhancer)", 0.0, 1.0, 0.4)
    mc1r = st.slider("MC1R (Hair/Skin)", 0.0, 1.0, 0.6)
    slc24a5 = st.slider("SLC24A5 (Skin Tone)", 0.0, 1.0, 0.8)
    edar = st.slider("EDAR (Face Shape)", 0.0, 1.0, 0.5)

dna_data = np.array([oca2, herc2, mc1r, slc24a5, edar])

# --- Generate Face ---
print("\U0001F9EC Calling generate_face with:", dna_data)

if st.button("\U0001F389 Generate Face \U0001F3AD"):
    try:
        st.info("\U0001F9E0 Generating Face from DNA...")
        face = generate_face(dna_data)
        st.image(face, caption="\U0001F31F Predicted Face \U0001F31F", use_column_width=True)

        traits_dict = {
            "OCA2 (Eye Color)": oca2,
            "HERC2 (Eye Enhancer)": herc2,
            "MC1R (Hair/Skin)": mc1r,
            "SLC24A5 (Skin Tone)": slc24a5,
            "EDAR (Face Shape)": edar,
        }

        st.subheader("\U0001F9EC Trait Summary")
        for trait, val in traits_dict.items():
            st.markdown(f"**{trait}:** {val:.2f}")

        # Save to history
        st.session_state["history"].append((face, traits_dict))

        # Save to persistent history with username
        save_history(st.session_state["user"], dna_data.tolist())

        # PDF download
        pdf = generate_pdf(face, traits_dict)
        st.download_button(
            label="\U0001F4C4 Download PDF Report",
            data=pdf,
            file_name="face_report.pdf",
            mime="application/pdf"
        )

    except Exception as e:
        st.error(f"\u274C Error generating face: {e}")

# --- History ---
if st.checkbox("\U0001F553 Show History"):
    for idx, (img, traits) in enumerate(st.session_state["history"]):
        st.markdown(f"### \U0001F539 Face #{idx + 1}")
        st.image(img, width=300)
        for k, v in traits.items():
            st.markdown(f"- **{k}:** {v:.2f}")

# --- Dashboard Link ---
if st.sidebar.button("\U0001F4C1 View Dashboard"):
    show_dashboard(st.session_state["user"])
