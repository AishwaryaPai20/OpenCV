import cv2 as cv

img = cv.imread('Photos/1.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blurred', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

canny1 = cv.Canny(blur, 125, 175)
cv.imshow('Canny1', canny1)

contours, hierarchies = cv.findContours(
    canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')
# 775 contours found! -> Before blurring

contours, hierarchies = cv.findContours(
    canny1, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')
# 74 contours found! -> After blurring


cv.waitKey(0)
