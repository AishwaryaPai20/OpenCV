import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/2.jpg')
cv.imshow('Cats', img)
blank = np.zeros(img.shape[:2], dtype="uint8")

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', circle)

mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Mask', mask)

# Colors Histogram
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.waitkey(0)
