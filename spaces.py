import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/1.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV conversion
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

plt.imshow(img)
plt.show()

#BGR to RGB conversion
rgb=cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV_BGR', hsv_bgr)

cv.waitKey(0)
