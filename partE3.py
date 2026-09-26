import cv2

# Open video
cap = cv2.VideoCapture("input.mp4")

if not cap.isOpened():
    print("Error: Could not open input.mp4")
    exit()

# Read first frame
ok, frame = cap.read()

cap.release()

if ok:

    # Resize to 1280 x 720
    resized = cv2.resize(frame, (1280, 720))

    # Save resized frame
    cv2.imwrite("resized_frame.jpg", resized)

    # Display dimensions
    print("Original:", frame.shape)
    print("Resized:", resized.shape)

    # Calculate pixel counts
    original_height, original_width = frame.shape[:2]
    resized_height, resized_width = resized.shape[:2]

    original_pixels = original_width * original_height
    resized_pixels = resized_width * resized_height

    print("Original pixel count:", original_pixels)
    print("Resized pixel count:", resized_pixels)

else:
    print("Could not read video frame.")
