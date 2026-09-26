import cv2

# Open video
cap = cv2.VideoCapture("input.mp4")

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open input.mp4")
    exit()

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Calculate duration
duration = frame_count / fps if fps else 0

# Calculate pixels per frame
pixels_per_frame = width * height

print("FPS:", fps)
print("Resolution:", width, "x", height)
print("Frame count:", frame_count)
print("Approx. duration:", duration, "seconds")
print("Pixels per frame:", pixels_per_frame)

cap.release()
