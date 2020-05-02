import cv2

def detect():
    face_cascade = cv2.CascadeClassifier('face.xml')
    palm_cascade = cv2.CascadeClassifier('palm.xml')
    fist_cascade = cv2.CascadeClassifier('fist.xml')
    cap = cv2.VideoCapture(0)
    face = 0
    palm = 0
    fist = 0
    while True:

        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = 1
        cv2.imshow('Hi', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27 or face == 1:
            break

    while True:

        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = palm_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            palm = 1
        cv2.imshow('Hi', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27 or palm == 1:
            break

    while True:

        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = fist_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            fist = 1
        cv2.imshow('Hi', img)
        cv2.imwrite("lastSeen.jpeg",img)
        k = cv2.waitKey(30) & 0xff
        if k == 27 or fist == 1:
            break

    print("Tamamlandı")
    cap.release()
    return face == palm == fist
