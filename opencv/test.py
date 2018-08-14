#-*-coding:utf8-*-

import os
import numpy as np
import cv2 as cv


img = cv.imread("image/test.jpg")
cv.imshow("iamge", img)
cv.waitKey()
cv.destroyAllWindows()
