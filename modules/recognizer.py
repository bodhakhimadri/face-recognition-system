import face_recognition
from modules.database_handler import load_known_faces
from config.settings import TOLERANCE

def recognize_face(current_encoding):
    data = load_known_faces()
    if not data["encodings"]:
        return None

    # Compare current face against all saved encodings
    matches = face_recognition.compare_faces(data["encodings"], current_encoding, tolerance=TOLERANCE)
    
    if True in matches:
        first_match_index = matches.index(True)
        return data["ids"][first_match_index]
    
    return None