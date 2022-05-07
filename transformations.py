import cv2 as cv
import numpy as np

img = cv.imread('Photos/2.jpg')
cv.imshow('Park', img)

# Translation

#x and y


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# Rotation


def rotate(img, angle, rotPoint=None):
    height, width = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat =cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotated =rotate(img,45)
cv.imshow('Rotated',rotated)

rotated1 = rotate(img, -90)
cv.imshow('Rotated1', rotated1)

#Resizing
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resized',resized)

#Flipping
flipped=cv.flip(img,1)
cv.imshow('Flip',flipped)

#Cropping
cropped=img[200:400,300:400]
cv.imshow('Cropping',cropped)

cv.waitKey(0)
