import cv2
import os
from config.settings import IMAGE_DATASET
from modules.database_handler import load_known_faces, save_known_faces

def register_face(new_id, frame, encoding):
    # Save the image
    img_name = f"{new_id}.jpg"
    cv2.imwrite(os.path.join(IMAGE_DATASET, img_name), frame)

    # Update the pickle database
    data = load_known_faces()
    data["ids"].append(new_id)
    data["encodings"].append(encoding)
    save_known_faces(data)