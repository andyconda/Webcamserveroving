from tpk4128.server import SocketServer
from tpk4128.camera_opencv import Camera
import cv2 as cv


def main():
    camera = Camera()
    server = SocketServer('10.53.26.72', 50007)

    while True:

        data = server.recv()
        print(data)
        if not data:
            break

        img_unflipped = camera.capture()
        cv.rotate(img_unflipped, cv.ROTATE_180, img)  # bildet må flippes foreløpig siden RPien min er opp ned hihih
        # print(img.dtype) # for å finne inputs i run_client_opencv
        # print(img.shape) # for å finne inputs i run_client_opencv
        buf = img.tobytes() # stod opprinnelig tostring() her, men fikk warning om at det var deprecated.
        # print(len(buf)) # for å finne inputs i run_client_opencv
        server.sendall(buf)


if __name__ == '__main__':
    main()
