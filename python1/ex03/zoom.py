import cv2
from load_image import ft_load


def ft_zoom(path :str, weight : int, height : int):
    """
    ft_zoom(path :str, weight :int, height :int)
    this function takes the path of the image and the dimensions
    of the image after zooming into it !
    """
    print(weight, height)
    print(ft_load(path)) 
    image = cv2.imread(path)
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    ft_zoom("website.jpg", 400, 400)


if __name__ == "__main__":
    main()
