import cv2
from load_image import ft_load

def check_display():
    """
    check_display(None) -> bool
    this function check if there is a display or not
    """
    build_info = cv2.getBuildInformation()
    if 'highgui' not in build_info:
        return True
    else:
        return False


def ft_zoom(path :str):
    """
    ft_zoom(path :str)
    this function takes the path of the image to zoom into it !
    """
    print(ft_load(path)) 
    image = cv2.imread(path)
    w, h = image.shape[:2]
    new_slice = image[int(w / 10):w - int(w / 10), int(h / 10): h - int(h / 10)]
    if check_display() is not True:
        print ("Error: no display found")
        return
    cv2.startWindowThread()
    cv2.imshow('Image', new_slice)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    ft_zoom("website.jpg")


if __name__ == "__main__":
    main()
