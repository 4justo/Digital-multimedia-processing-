from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load image
img_pil = Image.open("image.jpg").convert("RGB")
img = np.array(img_pil)

# Convert RGB to grayscale
gray_cv = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Apply mean filters
smooth3 = cv2.blur(gray_cv, (3, 3))
smooth5 = cv2.blur(gray_cv, (5, 5))

# Display original grayscale
plt.figure(figsize=(6, 5))
plt.imshow(gray_cv, cmap="gray")
plt.axis("off")
plt.title("Original Grayscale Image")
plt.show()

# Display 3 x 3 result
plt.figure(figsize=(6, 5))
plt.imshow(smooth3, cmap="gray")
plt.axis("off")
plt.title("3 x 3 Mean Filter")
plt.show()

# Display 5 x 5 result
plt.figure(figsize=(6, 5))
plt.imshow(smooth5, cmap="gray")
plt.axis("off")
plt.title("5 x 5 Mean Filter")
plt.show()
