import cv2 as cv

# # Reading images
# img = cv.imread('Photos/cat_large.jpg')

# # show the image
# cv.imshow('Cat', img)

# ------------------------------------------------------
# Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')

# we read videos frame by frame with a loop
while True:
    isTrue, frame = capture.read() 
    # isTrue checks that a frame has been read in successfully.
    # This parameter being false could mean that the video could not be loaded or we are at the end of the video.

    if isTrue:
        cv.imshow('Video', frame)

        if cv.waitKey(20) and 0xFF == ord('d'): # if letter 'd' is pressed, break out of the loop
            break

    else:
        break

capture.release()
cv.destroyAllWindows()
