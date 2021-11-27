import cv2 as cv

#This is reading and showing image
img = cv.imread("Photos/Pittsburgh.jpg")
cv.imshow("Pittsburgh",img)
cv.waitKey(0)
#This is converting an image to Grayscale and showing the image
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray image",gray)
cv.waitKey(0)
#This is blurring and showing an image
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
cv.imshow("Blur image",blur)
cv.waitKey(0)
#Finding all the edges in the image and dsiplaying it. Personal Favourite :)
edges = cv.Canny(img,175,250)
cv.imshow("Edges image",edges)
cv.waitKey(0)
#Dilating the image and displaying it
dilated = cv.dilate(edges,(7,7),iterations=3)
cv.imshow("Dilated image",dilated)
cv.waitKey(0)
#Eroding the image and displaying it
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow("Erroded image",eroded)
cv.waitKey(0)
#Cropping the image and displaying it
cropped = img[50:200,200:400]
cv.imshow("Cropped image",cropped)
cv.waitKey(0)