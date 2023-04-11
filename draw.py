import cv2 as cv
import numpy as np

# we can create a blank image to draw on
blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# # 1. Paint the image a particular color
# blank[:] = 0,255,0
# cv.imshow('Green', blank)

# # 2. Paint a portion of the image
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Part Red', blank)

# # 3. Draw a Rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
# # fill the shape with 'thickness=-1' or 'thickness=cv.FILLED'
# cv.imshow('Rectangle', blank)

# # 4. Draw a Circle
# cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0,0,255), thickness=-1)
# cv.imshow('Circle', blank)

# # 5. Draw a line
# cv.line(blank, (0,0), (250,250), (255,255,255), thickness=3)
# cv.imshow('Line', blank)

# 6. Write text
cv.putText(blank, 'Hello, my name is Stanley!', (1, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
cv.putText(blank, 'I\'m an Engineering Student', (1, 300), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
