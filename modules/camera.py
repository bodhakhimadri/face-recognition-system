import cv2

def start_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Camera not found!")
        return None
    return cap