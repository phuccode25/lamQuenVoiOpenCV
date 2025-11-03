import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('photos/Screenshot 2025-10-28 203200.png')
cv.imshow('siuu',img)

# plt.imshow(img)
# plt.show()

#BGR to Gray scale
gray  =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

#BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)

# #BGR to L*A*B
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("lab",lab)

#BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("rgb",rgb)


# ------------- by contrary--------------
#HSV to BGR
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV----->BGR',hsv_bgr)
#L*A*B to BGR 
lab_bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('LAB------>BGR',lab_bgr)
#RGB to BGR
rgb_bgr = cv.cvtColor(rgb,cv.COLOR_RGB2BGR)
cv.imshow('RGB---->BGR',rgb_bgr)
# Gray scale to BGR
gray_scale_bgr = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
cv.imshow('gray_scale======>BGR',gray_scale_bgr)

plt.imshow(rgb)
plt.show()
cv.waitKey(0)




# 1:21:56   