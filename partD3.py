from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load image
img_pil = Image.open("image.jpg").convert("RGB")
img = np.array(img_pil)

# Convert to grayscale
gray_cv = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Sharpening kernel
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# Apply sharpening
sharpened = cv2.filter2D(gray_cv, -1, kernel)

# Display original and sharpened images
plt.figure(figsize=(6, 5))
plt.imshow(gray_cv, cmap="gray")
plt.axis("off")
plt.title("Original Grayscale Image")
plt.show()

plt.figure(figsize=(6, 5))
plt.imshow(sharpened, cmap="gray")
plt.axis("off")
plt.title("Sharpened Image")
plt.show()
