
from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2

def eye_aspect_ratio(eye):
	
	dist_ver1 = dist.euclidean(eye[1], eye[5])
	dist_ver2 = dist.euclidean(eye[2], eye[4])

	dist_hor = dist.euclidean(eye[0], eye[3])

	eratio = (dist_ver1 + dist_ver2) / (2.0 * dist_hor)

	
	return eratio

teratio1= 0.25
teratio2=0.4
maxframes = 3
fcount = 0
total = 0
bcount =0 

#print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]


#print("[INFO] starting video stream thread...")
vs = VideoStream(src=0).start()


fileStream = False
time.sleep(0.5)
def slide_count():
        Count=1
        return Count

while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=450)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

     
        rects = detector(gray, 0)

      
        for rect in rects:
               
                shape = predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)

          
                leftEye = shape[lStart:lEnd]
                rightEye = shape[rStart:rEnd]
                leftEAR = eye_aspect_ratio(leftEye)
                rightEAR = eye_aspect_ratio(rightEye)

                eratio = (leftEAR + rightEAR) / 2.0
                leftEyeHull = cv2.convexHull(leftEye)
                rightEyeHull = cv2.convexHull(rightEye)
                cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
                cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

         
                if (eratio > teratio1 and eratio <= teratio2):
                        fcount += 1


                else:
                       
                        if fcount >=maxframes:
                                total += 1
                                slide_count()
                                file=open("connection.txt","w")
                                file.write('1')
                                file.close()


                      
                        fcount = 0

                cv2.putText(frame, "Blinks: {}".format(total), (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "EAR: {:.2f}".format(eratio), (300, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                time.sleep(0.2)

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(25) & 0xFF

       
        if key == ord("q"):
                break


cv2.destroyAllWindows()
vs.stop()

