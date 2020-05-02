import cv2
def detect():
    found = 0
    face_cascade = cv2.CascadeClassifier('haarcascade-frontalface-default.xml')
    cap = cv2.VideoCapture(0)
    while True:
        _,img = cap.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.1,4)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            found = 1
            cv2.imwrite('lastSeen.jpeg',img)
        cv2.imshow('SCAN YOUR FACE',img)
        k= cv2.waitKey(30) & 0xFF
        if k == 27 or found == 1:
            break
    cap.release()
    return found
