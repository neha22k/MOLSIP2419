import cv2

# Load Haar cascades
face_cascade = cv2.CascadeClassifier('C:/Users/prasa/Desktop/micrOrbitals/detection authentication system/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/Users/prasa/Desktop/micrOrbitals/detection authentication system/haarcascade_eye.xml')

# Initialize video capture
cap = cv2.VideoCapture(0)

EYE_AR_THRESH = 0.25
EYE_AR_CONSEC_FRAMES = 3

COUNTER = 0
TOTAL = 0

def detect_eyes(frame, face):
    gray_face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray_face, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return eyes

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        eyes = detect_eyes(frame, face)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        if len(eyes) == 0:
            COUNTER += 1
        else:
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                TOTAL += 1
            COUNTER = 0

        cv2.putText(frame, f"Blinks: {TOTAL}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
