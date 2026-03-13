import cv2
from modules.face_detector import detect_faces
from modules.face_encoder import encode_faces
from modules.recognizer import recognize_face
from modules.register_user import register_face

def main():
    cap = cv2.VideoCapture(0)
    print("System Running... Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret: continue

        # 1. Detection
        face_locations = detect_faces(frame)
        
        # 2. Encoding & Recognition
        if face_locations:
            face_encodings = encode_faces(frame, face_locations)
            
            for loc, encoding in zip(face_locations, face_encodings):
                user_id = recognize_face(encoding)
                
                top, right, bottom, left = loc
                
                if user_id:
                    # Recognized
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv2.putText(frame, f"ID: {user_id}", (left, top-10), 0, 0.8, (0, 255, 0), 2)
                else:
                    # Not Recognized - "Another Interface" (Terminal Input)
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.imshow("Face Recognition", frame)
                    cv2.waitKey(1) # Refresh window
                    
                    print("\n[!] Face Not Recognized.")
                    choice = input("Register this person? (y/n): ").lower()
                    if choice == 'y':
                        new_id = input("Enter ID number: ")
                        register_face(new_id, frame, encoding)
                        print(f"User {new_id} saved.")

        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()