import cv2 as cv

img = cv.imread('Photos/2.jpg')

cv.imshow('image', img)

cv.waitKey(0)

# capture=cv.VideoCapture('Videos/1.mp4')

# while True:
#     isTrue,frame=capture.read()
#     cv.imshow('Video',frame)
    
#     if cv.waitKey(20) & 0xFF == ord('q'):
#         break
    
# capture.release()
# cv.destroyAllWindows()
    
