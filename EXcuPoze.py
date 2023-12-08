import cv2
#calea fisierului text.xml
face_cascade = cv2.CascadeClassifier(r"C:\Users\catal\OneDrive\Desktop\MAP\DumitruCatalania.xml")
#calea pozei
img = cv2.imread(r'C:\Users\catal\OneDrive\Desktop\MAP\MAP\pozaMama.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for(x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey()