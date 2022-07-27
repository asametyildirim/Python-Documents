import cv2
# pip install opencv-python

from pyzbar.pyzbar import decode
#pip install pyzbar

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success, img=cap.read()
    for barcode in decode(img):
       print(barcode.data)
       myData = barcode.data.decode('utf-8')
       print(myData)

    cv2.imshow('Result',img)
    cv2.waitKey(1)

