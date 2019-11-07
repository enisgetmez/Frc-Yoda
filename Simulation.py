import cv2
import numpy as np
import imutils
import serial
import pyautogui



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
    #print("Algilanan Obje : " , x) # x kordinatını yazdırıyoruz
    
    #ekranda gosteriyoruz
    cv2.imshow('Yuz detect', frame)
    #q tusu cikis
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    ########El Tanima Bitis##########

    ########kas algilama Baslangic##########
    data=ser.readline()
    data=int(data.decode('utf-8', errors='ignore').strip())
    #print("Kas Datasi : ",data)
    ########kas algilama Bitis##########

    ########Simülasyon Baslangic##########
    if(data > 200):
        pyautogui.press("w")
        print("ileri gidiliyor")
    else:
        print("Veri algılanmadı", data)


    if(w > 90 and w < 400): #elimiz disindaki seyleri algilamamasi icin
        if(x == 0):
            print("Deger yok")
        elif(x < 400):
            pyautogui.press("d") #d tusuna bas saga don
            print("dye basiliyor")
            print(x)
        elif(x > 600):
            pyautogui.press("a") #a tusuna bas sol don
            print("a'ya basiliyor")
            print(x)
        x = 0
    ########Simülasyon Bitis##########




cap.release()
cv2.destroyAllWindows()
