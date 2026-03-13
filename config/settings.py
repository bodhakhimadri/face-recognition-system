import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(BASE_DIR, "database", "face_db.db")
ENCODINGS_PATH = os.path.join(BASE_DIR, "database", "encodings.pkl")
IMAGE_DATASET = os.path.join(BASE_DIR, "dataset", "images")

TOLERANCE = 0.6  # Lower is stricter (0.4-0.5), higher is loos