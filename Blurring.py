import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging
# Computes the pixel of one window as the average of all the windows surrounding it. 
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
# Uses weights of each window instead of pixel values as in average. 
# It is normally less blurred as compared to average when you use the same kernel size. 
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
# Uses median instead of average. More effective in reducing noise in an image as compared to the previous two.
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
# The most effecctive. Applies blurring but retains the edges in the image unlike the other three.
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)