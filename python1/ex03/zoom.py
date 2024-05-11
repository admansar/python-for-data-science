import cv2
import os
from load_image import ft_load

def is_display():
    """
    check_display(None) -> bool
    this function check if there is a display or not
    """
    build_info = cv2.getBuildInformation()
    return "DISPLAY" in os.environ


def ft_zoom(path :str):
    """
    ft_zoom(path :str)
    this function takes the path of the image to zoom into it !
    """
    print(ft_load(path)) 
    image = cv2.imread(path)
    w, h = image.shape[:2]
    for i in range(w): 
        for j in range(h): 
            img[i, j] = sum(img[i, j]) * 0.33
    new_slice = image[100:500, 400:800]
    gray_image = cv2.cvtColor(new_slice, cv2.COLOR_BGR2GRAY)
    print("New shape after slicing: ", gray_image.shape)
    print(gray_image.reshape(-1, 1))
    if is_display() is not True:
        print ("Error: no display found")
        return
    cv2.startWindowThread()
    cv2.imshow('Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    ft_zoom('animal.jpeg')

if __name__ == "__main__":
    main()
