import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)
img = cv.imread('photos/Screenshot 2025-10-29 134215.png')
cv.imshow('..',img)
# !.Paint the image a certain colour

blank[200:300,300:400]= 0,0,255
# Ve tam giac
s= cv.rectangle(blank,(0,0),(240,230),(0,255,0),thickness=2)
cv.imshow('rectangle',s)

#Draw a circle
cv.circle(blank.shape[1]//2,blank.shape[0]//2,40,(0,0,255),thickness=-1)
cv.imshow('circle',blank)
cv.imshow('green',blank)
cv.waitKey(0)