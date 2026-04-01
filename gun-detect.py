import cv2
import imutils
import datetime
import os

cascade_path = 'cascade.xml'
if not os.path.exists(cascade_path):
    print(f"Error: {cascade_path} not found.")
    exit()

gun_cascade = cv2.CascadeClassifier(cascade_path)
camera = cv2.VideoCapture(0)

# --- NEW: Filter Variables ---
detection_buffer = 0 
BUFFER_THRESHOLD = 5 # Must see weapon for 5 frames in a row
gun_detected_session = False

while True:
    ret, frame = camera.read()
    if not ret: break

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use 1.15 and 25 for even stricter detection
    guns = gun_cascade.detectMultiScale(gray, 1.15, 25, minSize=(100, 100))
    
    if len(guns) > 0:
        detection_buffer += 1 # Increase count if something is seen
    else:
        detection_buffer = max(0, detection_buffer - 1) # Decrease if nothing is seen

    if detection_buffer >= BUFFER_THRESHOLD:
        gun_detected_session = True
        for (x, y, w, h) in guns:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, "WEAPON CONFIRMED", (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    cv2.imshow("Security Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

camera.release()
cv2.destroyAllWindows()
