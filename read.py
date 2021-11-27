import cv2 as cv

img = cv.imread('Photos/Photo.jpg')
cv.imshow('Zeaan',img)
cv.waitKey(0)
print(img)