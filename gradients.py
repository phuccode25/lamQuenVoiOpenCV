import cv2 as cv
import numpy as np
img = cv.imread('photos/OIP.jpg')
cv.imshow('siuu',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Lapcian',lap)
#Sobel
sobelX =cv.Sobel(gray,cv.CV_64F,1,0)
sobelY =cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelX,sobelY)
cv.imshow('sobelX',sobelX)
cv.imshow('sobely',sobelY)
cv.imshow('combine_sobel',combined_sobel)

canny = cv.Canny(gray,150,175)
cv.imshow('Canny',canny)
cv.waitKey(0)