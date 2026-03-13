import pickle
import os
from config.settings import ENCODINGS_PATH

def load_known_faces():
    if os.path.exists(ENCODINGS_PATH):
        with open(ENCODINGS_PATH, 'rb') as f:
            return pickle.load(f)
    return {"ids": [], "encodings": []}

def save_known_faces(data):
    with open(ENCODINGS_PATH, 'wb') as f:
        pickle.dump(data, f)