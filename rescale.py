import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Reading images
img = cv.imread('Photos/cat.jpg')

# show the image
cv.imshow('Cat', img)

resized_image = rescaleFrame(img, scale=0.5)
cv.imshow('Cat Resized', resized_image)

cv.waitKey(0)

# # Reading Videos
# capture = cv.VideoCapture('Videos/dog.mp4')

# # we read videos frame by frame with a loop
# while True:
#     isTrue, frame = capture.read() 
#     # isTrue checks that a frame has been read in successfully.
#     # This parameter being false could mean that the video could not be loaded or we are at the end of the video.

#     if isTrue:
#         frame_resized = rescaleFrame(frame, scale=0.2)

#         cv.imshow('Video', frame)
#         cv.imshow('Video Resized', frame_resized)

#         if cv.waitKey(20) and 0xFF == ord('d'): # if letter 'd' is pressed, break out of the loop
#             break

#     else:
#         break

# capture.release()
# cv.destroyAllWindows()
