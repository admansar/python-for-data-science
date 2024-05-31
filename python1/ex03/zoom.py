import cv2
from load_image import ft_load


def ft_zoom(path: str):
    """
    ft_zoom(path :str) -> None
    this function takes the path of the image to zoom into it !
    """
    print(ft_load(path))
    image = cv2.imread(path)
    new_slice = image[100:500, 400:800]
    gray_image = cv2.cvtColor(new_slice, cv2.COLOR_BGR2GRAY)
    print("New shape after slicing: ", gray_image.shape)
    print(gray_image.reshape(-1, 1))
    cv2.startWindowThread()
    cv2.imshow('Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    try:
        ft_zoom('animal.jpeg')
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
