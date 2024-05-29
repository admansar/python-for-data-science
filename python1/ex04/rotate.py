import numpy as np
import cv2

def transpose(matrix):
    """
    Transposes the given 2D matrix (list of lists).
    """
    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    # Create a new matrix with the dimensions swapped
    transposed_matrix = []
    for col in range(num_cols):
        new_row = []
        for row in range(num_rows):
            new_row.append(matrix[row][col])
        transposed_matrix.append(new_row)
    
    return transposed_matrix

def main():
    image = cv2.imread('animal.jpeg')
    image = cv2.cvtColor(image[100:500, 400:800], cv2.COLOR_BGR2GRAY)
    print("The shape of the image is:", image.shape)
    image_reshaped = image.reshape(image.shape[0], image.shape[1], 1)
    print(image_reshaped)
    image_transposed = np.array(transpose(image))
    print("The new shape after Transpose:", image_transposed.shape)
    print(image_transposed)
    cv2.imshow('Transposed Image', image_transposed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

