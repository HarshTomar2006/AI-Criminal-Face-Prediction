import sys
import os
import torch
import numpy as np
from PIL import Image

# Add path to stylegan2-ada-pytorch (adjust this if needed)
stylegan_path = os.path.join(os.getcwd(), "stylegan2-ada-pytorch")
sys.path.append(stylegan_path)

# Suppress Streamlit and Torch warnings
os.environ["STREAMLIT_DISABLE_WATCHDOG_WARNINGS"] = "true"
os.environ["PYTORCH_JIT"] = "0"

# Import StyleGAN2-ADA modules
try:
    import dnnlib
    import legacy
except ImportError as e:
    raise ImportError(f"❌ Failed to import StyleGAN modules: {e}")

# Device config
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# --- Load StyleGAN2-ADA Model ---
print("✅ Loading StyleGAN2-ADA model...")

model_dir = "models"
model_path = os.path.join(model_dir, "ffhq.pkl")
model_url = "https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada-pytorch/pretrained/ffhq.pkl"

if not os.path.exists(model_path):
    print("⬇️ ffhq.pkl not found, downloading...")
    os.makedirs(model_dir, exist_ok=True)
    import requests
    response = requests.get(model_url, stream=True)
    with open(model_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print("✅ Download complete!")

with open(model_path, 'rb') as f:
    G = legacy.load_network_pkl(f)['G_ema'].to(device)

print("✅ Model loaded successfully!")

# --- Main Generate Face Function ---
def generate_face(dna_data):
    """
    Generate a face image from DNA-like input vector.

    Parameters:
        dna_data (np.ndarray): 1D array with 5 float values (0-1)

    Returns:
        PIL.Image: Generated face image
    """
    try:
        latent = np.random.randn(512) * 0.5
        latent[:5] = dna_data  # Overwrite with DNA traits

        z = torch.from_numpy(latent).unsqueeze(0).to(device).float()

        with torch.no_grad():
            img_tensor = G(z, None, truncation_psi=0.7, noise_mode='const')[0]
            img_array = (img_tensor.permute(1, 2, 0).cpu().numpy() * 127.5 + 128).clip(0, 255).astype(np.uint8)
            img_pil = Image.fromarray(img_array, 'RGB')
            return img_pil

    except Exception as e:
        print(f"❌ Error in generate_face: {e}")
        return Image.new("RGB", (512, 512), (255, 0, 0))  # Red fallback

# --- Test Generation Block ---
if __name__ == "__main__":
    print("🔍 Running test generation...")
    sample_dna = np.array([0.1, 0.5, 0.8, 0.3, 0.9], dtype=np.float32)
    face = generate_face(sample_dna)
    face.save("test_output.jpg")
    print("✅ Face generated and saved as 'test_output.jpg'")
