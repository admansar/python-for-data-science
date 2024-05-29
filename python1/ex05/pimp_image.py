import numpy as np
import cv2
from load_image import ft_load

def ft_grey(image):
    """
    Inverts the blue channel of the given color image.
    """
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('grey', grey_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return grey_image


def ft_blue(image):
    """
    Inverts the blue channel of the given color image.
    """
    b, g, r = cv2.split(image)
    g[:] = 0
    r[:] = 0
    blue_image = cv2.merge([b, g, r])
    cv2.imshow('blue', blue_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return blue_image

def ft_green(image):
    """
    Inverts the green channel of the given color image.
    """
    b, g, r = cv2.split(image)
    b[:] = 0
    r[:] = 0
    green_image = cv2.merge([b, g, r])
    cv2.imshow('green', green_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return green_image

def ft_red(image):
    """
    Inverts the red channel of the given color image.
    """
    b, g, r = cv2.split(image)
    b[:] = 0
    g[:] = 0
    red_image = cv2.merge([b, g, r])
    cv2.imshow('red', red_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return red_image


def ft_invert(image):
   cv2.imshow('Invert', 255 - image)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   return image;


def main():
    image = ft_load('landscape.jpg')
    ft_green(image)
    ft_invert(image)
    ft_red(image)
    ft_blue(image)
    ft_grey(image)
if __name__ == "__main__":
    main()
