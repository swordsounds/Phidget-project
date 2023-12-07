import cv2 as cv
import numpy as np
import logging as lg

def main():
    lg.info("Initializing Camera Start")
    cap = cv.VideoCapture(0, cv.CAP_DSHOW)
    # cv.resizeWindow(cap, 10, 10	)
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