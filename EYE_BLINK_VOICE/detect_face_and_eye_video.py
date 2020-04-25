import cv2

# Including xml file for detecting face and eye
fcascade = cv2.CascadeClassifier('haarcascade.xml')
ecascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Capturing video continuously through webcam 
videocapture = cv2.VideoCapture(0)


while True:
    # Accessing frames from captured video
    _, image = videocapture.read()

    # Convertion to grayscale
    gscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detection of faces
    faces = fcascade.detectMultiScale(gscale, 1.1, 4)

    # Drawing region of interest(ROI)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        rgray = gscale[y:y+h, x:x+w]
        rcolor = image[y:y+h, x:x+w]
        #Detection of eyes
        eyedetect = ecascade.detectMultiScale(rgray)
        for (x1, y1, w1, h1) in eyedetect :
            cv2.rectangle(rcolor, (x1, y1), (x1+w1, y1+h1), (0, 255, 0), 2)

    # Displaying faces and eyes with ROI
    cv2.imshow('image', image)

    # Quitting the video when spacebar key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==32:
        break
        
# Releasing the captured object
videocapture.release()
