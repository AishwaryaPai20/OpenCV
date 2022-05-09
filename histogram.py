import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/2.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype="uint8")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', circle)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Mask', mask)

# Grayscale histograms
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

plt.figure()
plt.title('Grayscale histogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

cv.waitkey(0)
