import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load the image
B = np.array(Image.open('khayyam.jpg'))

# Normalize the image to float values between 0 and 1
I = B.astype(float) / 255.0

# List of ranks for approximation
ks = [10, 40, 160]

# Plotting setup
fig, axes = plt.subplots(1, len(ks) + 1, figsize=(15, 5))
axes[0].imshow(I)
axes[0].set_title("Original")
axes[0].axis('off')

# Perform SVD and approximation for each rank
for idx, k in enumerate(ks):
    A = np.zeros_like(I)
    for i in range(3):  # Loop over color channels (R, G, B)
        U, S, V = np.linalg.svd(I[:, :, i])
        A[:, :, i] = U[:, :k] @ np.diag(S[:k]) @ V[:k, :]
    
    # Clip values to stay in valid range
    A = np.clip(A, 0, 1)

    # Display the approximated image
    axes[idx + 1].imshow(A)
    axes[idx + 1].set_title(f"k = {k}")
    axes[idx + 1].axis('off')

# Show the plots
plt.tight_layout()
plt.show()
