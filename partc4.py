from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img_pil = Image.open("image.jpg").convert("RGB")
img = np.array(img_pil)

# Convert RGB image to grayscale
gray = np.array(img_pil.convert("L"))

print("Original image shape:", img.shape)
print("Grayscale image shape:", gray.shape)
print("Grayscale minimum:", gray.min())
print("Grayscale maximum:", gray.max())

# Display grayscale image
plt.figure(figsize=(6, 5))
plt.imshow(gray, cmap="gray")
plt.axis("off")
plt.title("Grayscale Image")
plt.show()


# Thresholding at 80, 128 and 180
thresholds = [80, 128, 180]

plt.figure(figsize=(15, 5))

for i, T in enumerate(thresholds):

    binary = np.where(
        gray >= T,
        255,
        0
    ).astype(np.uint8)

    # Display binary image
    plt.subplot(1, 3, i + 1)
    plt.imshow(binary, cmap="gray")
    plt.axis("off")
    plt.title(f"Threshold T = {T}")

plt.tight_layout()
plt.show()


# Calculate black and white proportions
print("\nThreshold Analysis")

for T in thresholds:

    binary = np.where(
        gray >= T,
        255,
        0
    ).astype(np.uint8)

    white_pixels = np.sum(binary == 255)
    black_pixels = np.sum(binary == 0)
    total_pixels = binary.size

    white_percentage = (white_pixels / total_pixels) * 100
    black_percentage = (black_pixels / total_pixels) * 100

    print(f"\nThreshold = {T}")
    print("White pixels:", white_pixels)
    print("Black pixels:", black_pixels)
    print(f"White percentage: {white_percentage:.2f}%")
    print(f"Black percentage: {black_percentage:.2f}%")
