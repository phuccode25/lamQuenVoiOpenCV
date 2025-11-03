import cv2 as cv

img = cv.imread('photos/Screenshot 2025-10-28 203200.png')
cv.imshow('siuu',img)
#Converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#Blur
blur =cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edge Cascode
canny = cv.Canny(img,threshold1=125,threshold2=175)
cv.imshow('canny',canny)


#Dilating the images
dilated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow('dialate',dilated)

#Eroding
eroded = cv.erode(dilated,(3,3),iterations=1)
cv.imshow('eroded',eroded)

#Resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resized',resized)

#cropping
cropped = img[50:200,200:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)