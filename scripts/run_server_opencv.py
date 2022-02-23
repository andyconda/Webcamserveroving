from tpk4128.server import SocketServer
from tpk4128.camera_opencv import Camera


def main():
    camera = Camera()
    server = SocketServer('10.53.26.72', 50007)

    while True:

        data = server.recv()
        print(data)
        if not data:
            break

        img = camera.capture()
        # print(img.dtype) # for å finne inputs i run_client_opencv
        # print(img.shape) # for å finne inputs i run_client_opencv
        buf = img.tobytes() # stod opprinnelig tostring() her, men fikk warning om at det var deprecated.
        # print(len(buf)) # for å finne inputs i run_client_opencv
        server.sendall(buf)


if __name__ == '__main__':
    main()
