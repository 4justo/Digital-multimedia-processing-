import cv2

# Open video
cap = cv2.VideoCapture("input.mp4")

if not cap.isOpened():
    print("Error: Could not open input.mp4")
    exit()

frame_number = 0
saved = 0

while True:
    ok, frame = cap.read()

    if not ok:
        break

    # Process every 30th frame
    if frame_number % 30 == 0 and saved < 5:

        # Convert frame from BGR to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Save grayscale frame
        filename = f"gray_frame_{saved}.jpg"
        cv2.imwrite(filename, gray)

        print("Saved:", filename)

        saved += 1

    frame_number += 1

cap.release()

print("Frames read:", frame_number)
print("Processed frames saved:", saved)
