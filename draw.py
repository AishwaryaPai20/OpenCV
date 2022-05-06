import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
cv.imshow('Blank', blank)
# img =cv.imread('Photos/3.jpg')
# cv.imshow('Cat',img)

# Paint the image a certain color
# blank[:]=0,255,0
# cv.imshow('Green',blank)

# blank[200:300,300:400] = 0, 0,255
# cv.imshow('Red', blank)

# Draw a rectangle
# cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=2)
# To fill the rectangle
cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness=cv.FILLED)
# or set thickness as -1

# Other way to form a Rectangle
cv.rectangle(blank, (0, 0),
             (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=-1)
cv.imshow('Rectangle', blank)

# Draw a circle
cv.circle(blank, (blank.shape[1]//2,
          blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)
cv.imshow('Circle', blank)

# Draw a  line
cv.line(blank, (0, 0), (blank.shape[1]//2,
                        blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)

# Writing Text
cv.putText(blank, 'Hello', (255, 255), cv.FONT_HERSHEY_TRIPLEX,
           1.0, (0, 0, 255), thickness=2)
cv.imshow('Text', blank)
cv.waitKey(0)

# Drawing Shapes and Adding Text
