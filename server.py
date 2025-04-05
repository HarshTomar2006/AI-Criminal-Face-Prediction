import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import base64

st.title("🔬 AI-Based Criminal Face Prediction from DNA")

# User input for DNA sequence
dna_input = st.text_input("Enter DNA Sequence (comma-separated values)", "0.7,0.4,0.6,0.8")

if st.button("🔍 Generate Face"):
    response = requests.post("http://127.0.0.1:5000/predict", json={"dna_sequence": dna_input})
    
    if response.status_code == 200:
        # Convert Base64 image to displayable format
        image_data = base64.b64decode(response.json()["image"])
        img = Image.open(BytesIO(image_data))
        st.image(img, caption="Predicted Face", use_column_width=True)
    else:
        st.error("⚠ Error generating image!")
