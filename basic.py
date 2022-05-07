import cv2 as cv

img = cv.imread('Photos/1.jpg')
cv.imshow('Cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# Blurring an image
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blurred', blur)
# here the image is blurred with a kernel size of 3x3 which is odd

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# Dilating the umage

dilated = cv.dilate(canny, (3, 3), iterations=3)
cv.imshow('Dilate', dilated)

# Eroding the image
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
