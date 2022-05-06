import cv2 as cv

img =cv.imread("Photos/2.jpg")
cv.imshow('Cat',img)

def rescaleFrame(frame,scale=0.75):
    width=frame.shape[1]*scale
    height = frame.shape[0]*scale
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

#Reading Video
capture = cv.VideoCapture('Videos/1.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
