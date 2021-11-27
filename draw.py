import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
blank[:] = 0,0,255
cv.imshow("Test",blank)
cv.waitKey(0)