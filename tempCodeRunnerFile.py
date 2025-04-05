import streamlit as st
import torch
import numpy as np
import matplotlib.pyplot as plt
from model import generate_face  
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap');

# 🎨 Add Holi Colors Effect
st.markdown(
    """
    <style>
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

.container {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(8px);
    border-radius: 25px;
    padding: 30px;
    margin: 40px auto;
    width: 90%;
    max-width: 600px;
    box-shadow: 0 8px 32px rgba(31, 38, 135, 0.3);
    color: #fff;
}

input[type="text"] {
    width: 80%;
    padding: 12px;
    margin-top: 20px;
    border-radius: 10px;
    border: none;
    outline: none;
    font-size: 18px;
}

button,
.stButton>button {
    background-color: #ff0055;
    color: white;
    font-size: 20px;
    padding: 12px 30px;
    border-radius: 15px;
    border: none;
    cursor: pointer;
    margin-top: 20px;
    transition: 0.3s;
    box-shadow: 0 0 10px #ff0055, 0 0 20px #ff55a1;
}

button:hover,
.stButton>button:hover {
    background-color: yellow;
    color: black;
    box-shadow: 0 0 15px yellow, 0 0 25px #ffe600;
}

img.generated-face {
    margin-top: 30px;
    width: 100%;
    max-width: 400px;
    border-radius: 20px;
    animation: fadeIn 2s ease-in-out;
}

@keyframes fadeIn {
    0% { opacity: 0; transform: scale(0.9); }
    100% { opacity: 1; transform: scale(1); }
}

/* Optional loader */
.loader {
    border: 6px solid #f3f3f3;
    border-top: 6px solid #ff0055;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    animation: spin 1s linear infinite;
    margin: 20px auto;
}
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

</style>
    """,
    unsafe_allow_html=True
)

st.title("🎨 Holi Special AI Criminal Face Prediction 🧬")

# Holi Banner
st.image("https://www.shutterstock.com/image-vector/happy-holi-festival-colors-background-600nw-2142910233.jpg", width=600)

# DNA Input
dna_input = st.text_input("🎭 Enter DNA Sequence (comma-separated values)", "0.7,0.4,0.6,0.8")

# Add Holi Sound Effect
st.audio("https://www.fesliyanstudios.com/play-mp3/387", format="audio/mp3")

if st.button("🎉 Generate Face 🎭"):
    try:
        dna_data = np.array([float(x) for x in dna_input.split(",")])
        generated_face = generate_face(dna_data)  
        st.image(generated_face, caption="🌟 Predicted Face 🌟", use_column_width=True)
    except:
        st.error("⚠ Invalid input! Please enter numeric values separated by commas.")
