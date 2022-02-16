#import numpy as np
import cv2 as cv


class Camera(object):

    def __init__(self):
        # Implement this constructor that opens a webcam and stores it in self._camera
        self._camera = cv.VideoCapture(0)

    def capture(self):
        # Implement this function that grabs an image from the webcam and returns a numpy array
        ret, img = self._camera.read()

        # Bruteforcer bildestørrelsen slik at jeg kan vite hvilken stringlength jeg mottar i klienten. Er det en måte å ikke måtte gjøre det sånn?
        self._camera.set(cv.CAP_PROP_FRAME_WIDTH, 640)
        self._camera.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            return

        return img

    def __del__(self):
        # Implement this destructor. Remember to free the camera.
        self._camera.release()
        cv.destroyAllWindows()
