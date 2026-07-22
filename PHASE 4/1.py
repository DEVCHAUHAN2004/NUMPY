import numpy as np
import matplotlib.pyplot as plt

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.random.rand(3,3)
arr3 = np.zeros((4,4))

np.save('array1.npy',arr1)
np.save('array2.npy',arr2)
np.save('array3.npy',arr3)

loaded_array = np.load('array1.npy')
print(loaded_array)


# import numpy as np
# import matplotlib.pyplot as plt

try:
    logo = plt.imread('numpy-logo.npy.jpg')

    plt.figure(figsize=(10, 6))

    # Original image
    plt.subplot(1, 2, 2)
    plt.imshow(logo)
    plt.title("NumPy Logo")
    plt.axis('off')

    # Dark / inverted image
    dark_logo = 1 - logo

    plt.subplot(1, 2, 1)
    plt.imshow(dark_logo)
    plt.title("Dark NumPy Logo")
    plt.axis('off')

    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("File not found!")