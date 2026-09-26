from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img_pil = Image.open("image.jpg").convert("RGB")
img = np.array(img_pil)

# Brightness adjustments
bright20 = np.clip(
    img.astype(np.int16) + 20,
    0,
    255
).astype(np.uint8)

bright40 = np.clip(
    img.astype(np.int16) + 40,
    0,
    255
).astype(np.uint8)

bright80 = np.clip(
    img.astype(np.int16) + 80,
    0,
    255
).astype(np.uint8)

dark40 = np.clip(
    img.astype(np.int16) - 40,
    0,
    255
).astype(np.uint8)

# Display results
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(bright20)
plt.axis("off")
plt.title("Brightness +20")

plt.subplot(2, 2, 2)
plt.imshow(bright40)
plt.axis("off")
plt.title("Brightness +40")

plt.subplot(2, 2, 3)
plt.imshow(bright80)
plt.axis("off")
plt.title("Brightness +80")

plt.subplot(2, 2, 4)
plt.imshow(dark40)
plt.axis("off")
plt.title("Brightness -40")

plt.tight_layout()
plt.show()
