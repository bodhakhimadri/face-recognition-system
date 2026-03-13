import face_recognition
import cv2
import numpy as np

def detect_faces(frame):
    if frame is None or frame.size == 0:
        return []

    try:
        # Force 8-bit conversion and BGR to RGB
        frame_8bit = cv2.convertScaleAbs(frame)
        rgb = cv2.cvtColor(frame_8bit, cv2.COLOR_BGR2RGB)
        
        # Ensure memory alignment for dlib
        rgb_final = np.ascontiguousarray(rgb, dtype=np.uint8)
        
        return face_recognition.face_locations(rgb_final)
    except Exception as e:
        print(f"[DEBUG] Detector Error: {e}")
        return []