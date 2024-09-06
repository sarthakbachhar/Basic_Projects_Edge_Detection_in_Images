import cv2
from matplotlib import pyplot as plt 

# Load the image
image = cv2.imread('C:/Users/Acer/Desktop/nobi.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded correctly
if image is None:
    print("Unable to load the image.")
else:
    # Apply Canny edge detection
    edges = cv2.Canny(image, threshold1=100, threshold2=200)

    # Display the original and edge-detected images
    plt.figure(figsize=(10, 5))

    # For original image
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image, cmap='gray')

    # For processed image
    plt.subplot(1, 2, 2)
    plt.title("Canny Edge Detection")
    plt.imshow(edges, cmap='gray')

    # Display both images 
    plt.show()
