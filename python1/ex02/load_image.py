import sys

sys.path.append('/usr/local/python/3.10.13/lib/python3.10/site-packages')
import cv2 

def ft_load(path: str):
    image = cv2.imread('project.jpg')
    print("The shape of the image is",image.shape)

import sys
print(ft_load(sys.argv[1]))
