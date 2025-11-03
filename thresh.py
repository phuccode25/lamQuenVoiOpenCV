import cv2 as cv

img = cv.imread('photos/OIP.jpg')
cv.imshow('siuu',img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#simple thresholding
threshold,thresh = cv.threshold(gray,100,255,cv.THRESH_BINARY) # 100 la cuong do diem anh co trong anh
cv.imshow('Simple thresholded',thresh)

threshold,thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV) # 100 la cuong do diem anh co trong anh
cv.imshow('Simple thresholded  Inverse',thresh_inv)

#adapative Thresholding
adapative_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,3)
cv.imshow('adapative_thresh',adapative_thresh )
cv.waitKey(0)