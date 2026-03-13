import cv2
import os
from modules.camera import start_camera
from modules.face_detector import detect_faces
from modules.face_encoder import encode_faces
from modules.recognizer import recognize_face
from modules.register_user import register_face

def main():
    cap = start_camera()
    if cap is None: return

    print("[SYSTEM] Camera Started. Looking for faces...")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Blank frame captured")
            continue

        # 1. Detection
        face_locations = detect_faces(frame)
        
        # DEBUG: Tell us if a face is even seen
        if len(face_locations) > 0:
            print(f"[DEBUG] Found {len(face_locations)} face(s). Encoding now...")
            
            # 2. Encoding
            face_encodings = encode_faces(frame, face_locations)
            
            for loc, encoding in zip(face_locations, face_encodings):
                # 3. Recognition
                user_id = recognize_face(encoding)
                
                top, right, bottom, left = loc
                
                if user_id:
                    print(f"[MATCH] User ID: {user_id} recognized.")
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv2.putText(frame, f"ID: {user_id}", (left, top-10), 0, 0.8, (0, 255, 0), 2)
                else:
                    print("[ALERT] Face not in database.")
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.imshow("Face Recognition", frame)
                    cv2.waitKey(1)
                    
                    choice = input("\nNot Recognized. Register this person? (y/n): ").lower()
                    if choice == 'y':
                        new_id = input("Enter New ID: ")
                        register_face(new_id, frame, encoding)
                        print(f"[SUCCESS] {new_id} added to database.")

        # Show the frame
        cv2.imshow("Face Recognition", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()