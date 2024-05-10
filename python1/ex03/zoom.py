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
    new_slice = image[200:600, 200:600]
    print("New shape after slicing: ", new_slice.shape)
    print(new_slice.reshape(-1, 1))
    if is_display() is not True:
        print ("Error: no display found")
        return
    cv2.startWindowThread()
    cv2.imshow('Image', new_slice)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    ft_zoom('animal.jpg')

if __name__ == "__main__":
    main()
