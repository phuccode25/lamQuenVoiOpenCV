import cv2 as cv
import numpy as np

img = cv.imread('photos/Screenshot 2025-10-28 203200.png')
cv.imshow('siuu',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

blank = np.zeros(img.shape,dtype='uint8')
cv.imshow('blank',blank)
# blur =  cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)
canny = cv.Canny(img,125,175)
cv.imshow('canny',canny)
# ret,thresh =cv.threshold(gray,125,255,cv.THRESH_BINARY)


contours, hierarchies = cv.findContours(canny
,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} countour(s) found:')
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Countours draw',blank)

cv.waitKey(0)