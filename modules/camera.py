import cv2
from config.settings import CAMERA_INDEX

def start_camera():
    cap = cv2.VideoCapture(CAMERA_INDEX)

    if not cap.isOpened():
        raise Exception("Camera not accessible")

    return cap