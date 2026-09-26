from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
img_pil = Image.open("image.jpg").convert("RGB")
img = np.array(img_pil)
print("Shape:", img.shape)
print("Data type:", img.dtype)
print("Minimum value:", img.min())
print("Maximum value:", img.max())
plt.imshow(img)
plt.axis("off")
plt.title("Original Image")
plt.show()
