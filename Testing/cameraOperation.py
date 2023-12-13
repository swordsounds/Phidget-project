import cv2 as cv
import numpy as np
import logging as lg

def main():
    lg.info("Initializing Camera Start")
    cap = cv.VideoCapture(0, cv.CAP_DSHOW)
    cv.namedWindow("Info", cv.WINDOW_NORMAL)
    cv.resizeWindow("Info", 540, 540)
   
   
    while(1):
        try:
            _, frame = cap.read()
            frame = cv.resize(frame, (540, 540))
            cv.imshow('Video',frame)
            k = cv.waitKey(5) & 0xFF
        except Exception:
            break
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()