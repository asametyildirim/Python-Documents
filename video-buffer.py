import threading, time
import cv2
import queue

imput_buffer = queue.Queue()

def proceessing():
    while True:
        print("get")
        frame = imput_buffer.get()
        cv2.imshow("Video",frame)
        time.sleep(0.025)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        return

cap = cv2.VideoCapture('cats.mp4')
t = threading.Thread(target=proceessing())
t.start()

while True:
    ret , frame = cap.read()
    input_buffer.put