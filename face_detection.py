import cv2
import keyboard

face_cascade = cv2.CascadeClassifier(r'C:\Users\catal\OneDrive\Desktop\MAP\DumitruCatalania.xml')

#webcam
cap =cv2.VideoCapture(0)
#de pe img
#cap=cv2.VideoCapture...

while not keyboard.is_pressed('esc'):
    #citim frame-urile camereei 
    _, img = cap.read()
    #conversie i gri 
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #detecta fetele
    faces= face_cascade.detectMultiScale(gray, 1.1,4)
    #Desenam patratele
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y), (x+w,y+h),(255,0,0),2)
    #afisam rezultatul 
    cv2.imshow('img',img)
    #oprim programul daca se apasa pe esc
    k=cv2.waitKey(30)& 0xff
    if k==27:
            break
#ii dam release camerei WED
cap.release()