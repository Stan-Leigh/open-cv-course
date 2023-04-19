import cv2 as cv

img = cv.imread('Photos/lady.jpg')
# cv.imshow('Group of people', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray People', gray)

# Haar cascades are really sensitive to noise in an image
# Anything that looks like a face, haar cascade will detect it even if it isn't a face.
# You can fine tune haar cascade to detect faces better by changing the minNeighbors and scaleFactor parameters
haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    x1, y1 = x+w, y+h

    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    # Top left design (x,y)
    cv.line(img, (x, y), (x+30, y), (0,255,0), 5)
    cv.line(img, (x, y), (x, y+30), (0,255,0), 5)

    # Top right design (x1,y)
    cv.line(img, (x1, y), (x1-30, y), (0,255,0), 5)
    cv.line(img, (x1, y), (x1, y+30), (0,255,0), 5)

    # Bottom left design (x,y1)
    cv.line(img, (x, y1), (x+30, y1), (0,255,0), 5)
    cv.line(img, (x, y1), (x, y1-30), (0,255,0), 5)

    # Bottom right design (x1,y1)
    cv.line(img, (x1, y1), (x1-30, y1), (0,255,0), 5)
    cv.line(img, (x1, y1), (x1, y1-30), (0,255,0), 5)

cv.imshow('Detected Faces', img)

cv.waitKey(0)
