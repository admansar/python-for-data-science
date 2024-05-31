import cv2


def ft_load(path: str):
    """
    ft_load(path: str) -> numpy.ndarray
    this function that loads an image given as a argument,
    and  prints its format, and its pixels content in RGB format.
    """
    image = cv2.imread(path)
    print("The shape of the image is", image.shape)
    print(image)
    return image
