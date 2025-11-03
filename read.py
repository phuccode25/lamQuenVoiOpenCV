import cv2 as cv

# img = cv.imread('photos/Screenshot 2025-10-28 203200.png')
# cv.imshow('xxxx',img)
#reading cv2

# capture = cv.VideoCapture('videos/Recording 2025-10-31 003743.mp4')
# while True:
#     isTrue,frame = capture.read()
#     cv.imshow('Video',frame)
    
#     if cv.waitKey(30) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()


def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
    