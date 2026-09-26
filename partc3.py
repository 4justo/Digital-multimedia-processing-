from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img_pil = Image.open("image.jpg").convert("RGB")
img = np.array(img_pil)

# Generate image negative
negative = 255 - img

# Display the negative image
plt.imshow(negative)
plt.axis("off")
plt.title("Image Negative")
plt.show()

# Calculations
value1 = 50
negative1 = 255 - value1

value2 = 200
negative2 = 255 - value2

print("Negative of 50:", negative1)
print("Negative of 200:", negative2)
