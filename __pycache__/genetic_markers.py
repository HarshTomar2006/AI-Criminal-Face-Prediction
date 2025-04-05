# genetic_markers.py

# A dictionary that maps genes to a normalized trait value
def get_dna_vector(user_traits):
    """
    user_traits: dict containing keys OCA2, HERC2, MC1R, SLC24A5, EDAR
    Each value should be between 0.0 and 1.0
    """
    # Order matters for input to GAN
    vector = [
        user_traits.get("OCA2", 0.5),      # Default 0.5 if not provided
        user_traits.get("HERC2", 0.5),
        user_traits.get("MC1R", 0.5),
        user_traits.get("SLC24A5", 0.5),
        user_traits.get("EDAR", 0.5)
    ]
    return vector
