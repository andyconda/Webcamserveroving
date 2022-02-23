from tpk4128.client import SocketClient
import time
import cv2
import numpy as np


def main():

    client = SocketClient('192.168.105.175', 50007)

    firstTime = 0;
    while True:
        #if firstTime == 0:#sørger for at den kun printer hello world en gang
          #  client.sendall(b'Hello World!') # b kaster stringen til byte
         #   firstTime = 1
        # Så jeg kan ikke sende "hello world" bare en gang med denne koden. Da får jeg bare en frame. Koden er avhengig av å holde sendall gående,
        # hvis ikke kommer det bare et bilde. MÅ FINNE UT AV

        client.sendall(b'Hello World!')  # b kaster stringen til byte
        # Tip: len(img.tostring())
        size, data = client.recv(921600)
        if not data:
            break

        # Tip: img.dtype, img.shape
        imgunflipped = np.frombuffer(data, "uint8").reshape(480, 640, 3)

        img = cv2.rotate(imgunflipped, cv2.ROTATE_180) # Flipper kameraet, siden kameraet på RPien min er foreløpig opp ned hehe


        cv2.imshow('img', img)
        if cv2.waitKey(20) == 27:  # Esc: 27
            break


if __name__ == '__main__':
    main()
