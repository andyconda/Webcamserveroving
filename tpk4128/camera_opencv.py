import numpy as np
import cv2 as cv
import time


class Camera(object):

    def __init__(self):
        # Implement this constructor that opens a webcam and stores it in self._camera
        self._camera = cv.VideoCapture(0)
        time.sleep(1.00)

    def capture(self):
        # Implement this function that grabs an image from the webcam and returns a numpy array
        ret, img = self._camera.read()
        img = cv.flip(img, 0)  # bildet må flippes foreløpig siden RPien min er opp ned hihih
        # print("Shape i camera_opencv")
        # print(img.shape)
        # Legges til for å gi windows tid til å finne kameraet. Fikset en error hvor den ikke klarte å acesse kameratet.

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            return

        return img

    def __del__(self):
        # Implement this destructor. Remember to free the camera.
        self._camera.release()
        cv.destroyAllWindows()
