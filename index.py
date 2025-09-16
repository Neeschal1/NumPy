import qrcode
import numpy as np
import matplotlib.pyplot as plt

# Create real QR image
qr_img = qrcode.make("https://pulu.com.np")

# Convert to NumPy array (0 = white, 255 = black)
qr_np = np.array(qr_img.convert('L'))

# Show using matplotlib
plt.imshow(qr_np, cmap='gray')
plt.axis('off')
plt.title("Scannable QR Code from NumPy")
plt.show()
