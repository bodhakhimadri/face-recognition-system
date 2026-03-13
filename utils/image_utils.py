import cv2

def draw_box(frame, top, right, bottom, left, text):

    cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)

    cv2.putText(
        frame,
        text,
        (left, top-10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,0),
        2
    )