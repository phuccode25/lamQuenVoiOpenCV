import cv2 as cv
import numpy as np
img = cv.imread('photos/Screenshot 2025-10-28 203200.png')
cv.imshow('siuu',img)
#averaging  
average  = cv.blur(img,(7,7))
cv.imshow('average_blur',average)

# Gaussion Blur
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussion Blur',gauss)

#Median Blur
median = cv.medianBlur(img,7)
cv.imshow("median blur",median)

#bilateral
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('bilateral',bilateral)
cv.waitKey(0)

