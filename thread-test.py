from dronekit import connect

import threading


def komut1(degisken):
    print(degisken)

def komut2(degisken):
    print(degisken)

if __name__ == "__main__":
   t1 = threading.Thread(target=komut2, args=(degisken,))
   t2 = threading.Thread(target=komut1, args=(degisken,))
   t2.start()
   t1.start()
   print("Done!")