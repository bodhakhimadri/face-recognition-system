import pickle
import os
from config.settings import ENCODINGS_PATH

def load_known_faces():
    # Ensure the directory exists
    os.makedirs(os.path.dirname(ENCODINGS_PATH), exist_ok=True)
    
    if os.path.exists(ENCODINGS_PATH):
        try:
            with open(ENCODINGS_PATH, 'rb') as f:
                return pickle.load(f)
        except EOFError:
            return {"ids": [], "encodings": []}
    return {"ids": [], "encodings": []}

def save_known_faces(data):
    with open(ENCODINGS_PATH, 'wb') as f:
        pickle.dump(data, f)