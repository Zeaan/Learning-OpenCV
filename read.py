import cv2 as cv

img = cv.imread('Photos/Pittsburgh.jpg')
cv.imshow('Pittsburgh',img)
cv.waitKey(0)
print(img)