import cv2
import numpy as np
import imutils
import serial
from networktables import NetworkTables
########Roborio ile haberleşme#########
NetworkTables.initialize(server='roborio-6025-frc.local') # Roborio ile iletişim kuruyoruz
table = NetworkTables.getTable("Vision") # table oluşturuyoruz
########Roborio ile haberleşme#########

########kas algilama Baslangic##########
ser = serial.Serial('COM11',9600,timeout=1)
########kas algilama Bitis##########

########El Tanima Baslangic##########
x = 0 #algilanan nesnenin x kordinati
y = 0 #algilanan nesnenin x kordinati
w = 0 #algilanan nesnenin x kordinati
h = 0 #algilanan nesnenin x kordinati
cap = cv2.VideoCapture(0)#goruntuyu aliyoruz
yumruk_cascade = cv2.CascadeClassifier('C:\\Users\\menta\\Desktop\\Artificam\\features\\cascades\\yumruk.xml') #cascademizi cagiriyoruz
########El Tanima Bitis##########


while True:
    ########El Tanima Baslangic##########
    ret, frame = cap.read()#goruntuyu yakaliyoruz
    frame = imutils.resize(frame, width=1200 ,height=500) # görüntü genişliğini 1200p yapıyoruz
    frame = imutils.rotate(frame, angle=0) # görüntüyü sabitliyoruz
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#videoyu griye ceviriyoruz
    yumruks = yumruk_cascade.detectMultiScale(gray, 2.0, 2)# eli tespit ediyoruz

    for (x,y,w,h) in yumruks:
        cv2.rectangle(frame,(x+5,y+5),(x+w-5,y+h-5),(0,255,0),2)    #tespit edilen elin etrafini ciziyoruz 
    print("Algilanan Obje : " , x) # x kordinatını yazdırıyoruz
    x = 0
    #ekranda gosteriyoruz
    cv2.imshow('hand detect', frame)
    #q tusu cikis
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    ########El Tanima Bitis##########

    ########kas algilama Baslangic##########
    data=ser.readline()
    data=int(data.decode('utf-8', errors='ignore').strip())
    print("Kas Datasi : ",data)
    ########kas algilama Bitis##########

    ########Roborio İle Haberlesme######
    table.putNumber("X", x) # roborioya değeri göndermek
    table.putNumber("kas", data)
    ########Roborio İle Haberlesme######



cap.release()
cv2.destroyAllWindows()
