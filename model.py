import sys
import os
import torch
import numpy as np
from PIL import Image

# Add path to stylegan2-ada-pytorch
sys.path.append(os.path.join(os.path.dirname(__file__), 'stylegan2-ada-pytorch'))
import dnnlib
import legacy

# Suppress Streamlit and Torch warnings
os.environ["STREAMLIT_DISABLE_WATCHDOG_WARNINGS"] = "true"
os.environ["PYTORCH_JIT"] = "0"

# Device config
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load StyleGAN2-ADA model
model_path = os.path.join("models", "ffhq.pkl")
if not os.path.exists(model_path):
    raise FileNotFoundError(f"❌ Model not found at path: {model_path}")

# Load once globally
with open(model_path, 'rb') as f:
    G = legacy.load_network_pkl(f)['G_ema'].to(device)

def generate_face(dna_data):
    """
    Generate a face image from DNA-like input vector.

    Parameters:
        dna_data (np.ndarray): 1D array with 5 float values (0-1)

    Returns:
        PIL.Image: Generated face image
    """
    try:
        # Create 512-d latent vector, inject DNA traits
        latent = np.random.randn(512) * 0.5
        latent[:5] = dna_data  # Overwrite first 5 components

        z = torch.from_numpy(latent).unsqueeze(0).to(device).float()

        with torch.no_grad():
            img_tensor = G(z, None, truncation_psi=0.7, noise_mode='const')[0]
            img_array = (img_tensor.permute(1, 2, 0).cpu().numpy() * 127.5 + 128).clip(0, 255).astype(np.uint8)
            img_pil = Image.fromarray(img_array, 'RGB')
            return img_pil

    except Exception as e:
        print(f"❌ Error in generate_face: {e}")
        # Return fallback dummy image
        fallback = Image.new("RGB", (512, 512), (255, 0, 0))  # Red dummy
        return fallback
