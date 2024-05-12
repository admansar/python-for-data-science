import numpy as np
import cv2


def transpose(matrix):
    ligne = len(matrix)
    colone =  len(matrix[0])
    tmatrix = matrix[:]
    for i in range(ligne):
        for j in range(colone):
            tmatrix[i][j] = matrix[j][i]
    return tmatrix


def main():
    image = cv2.imread('animal.jpeg')
    image = cv2.cvtColor(image[100:500, 400:800], cv2.COLOR_BGR2GRAY)
    print("The shape of the image is", image.shape)
    everything = []
    for it in image:
       everything.append(it.reshape(-1, 1))
    full_pic = np.array(everything)
    print(full_pic)
    full_pic = transpose(full_pic).T
    print("the new shape after Transpose :", image.shape)
    print(full_pic) 
    cv2.startWindowThread()
    cv2.imshow('Image', full_pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
