import cv2 as cv

img = cv.imread("Photos/2.jpg")
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    #Images,Videos and Live Video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image=rescaleFrame(img, 0.5)
cv.imshow('Image',resized_image)

#Changing Resolution
def changeRes(width,height):
    #Only Works for Live Video
    capture.set(3,width)
    capture.set(4,height)
    
# Reading Video
capture = cv.VideoCapture('Videos/1.mp4')

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
