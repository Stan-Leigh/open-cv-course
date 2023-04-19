import cv2 as cv
import mediapipe as mp

img = cv.imread('Photos/lady.jpg')

# def rescaleFrame(frame, scale=0.75):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)

#     dimensions = (width, height)

#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# img = rescaleFrame(img, scale=0.2)

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.75)

# convert BGR image to RGB for the mediapipe library to use
imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

results = faceDetection.process(imgRGB)

if results.detections:
    for id, detection in enumerate(results.detections):
        # identify the image that was detected. This is the default function. We want to do our own
        # mpDraw.draw_detection(img, detection) 

        # print(id, detection)

        # print(detection.score)
        # print(detection.location_data.relative_bounding_box)

        bboxC = detection.location_data.relative_bounding_box
        ih, iw, ic = img.shape
        bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
            int(bboxC.width * iw), int(bboxC.height * ih)
        cv.rectangle(img, bbox, (255, 0, 255), 2)
        cv.putText(img, f'{int(detection.score[0] * 100)}%', 
                (bbox[0], bbox[1] - 20), cv.FONT_HERSHEY_PLAIN, 2, (255,0,255), 2)
        
else:
    print('Nothing detected!')

cv.imshow('Image', img)

cv.waitKey(0)
