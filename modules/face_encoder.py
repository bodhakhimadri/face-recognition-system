import face_recognition
import cv2
import numpy as np

def encode_faces(frame, face_locations):
    if not face_locations:
        return []

    # Apply the same 8-bit RGB fix
    frame_8bit = cv2.convertScaleAbs(frame)
    rgb = cv2.cvtColor(frame_8bit, cv2.COLOR_BGR2RGB)
    rgb_final = np.ascontiguousarray(rgb, dtype=np.uint8)

    return face_recognition.face_encodings(rgb_final, face_locations)
