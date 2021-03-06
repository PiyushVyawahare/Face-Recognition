import cv2
import numpy as np
image = cv2.imread("goku.jpg")

kernel = np.float32([[1, 0, 0],
                    [0, 1, 1],
                    [1, 1, -5]])

conv_image = cv2.filter2D(image, -1, kernel)

cv2.imshow("Conv", conv_image)
cv2.waitKey(0) 