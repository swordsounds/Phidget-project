import cv2 as cv
import numpy as np


def main():
    cap = cv.VideoCapture(0)
    while(1):
        try:
            _, frame = cap.read()
            cv.imshow('frame',frame)
            k = cv.waitKey(5) & 0xFF
        except Exception:
            break
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()