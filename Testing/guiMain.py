import cv2
# read two images
img_1 = cv2.imread('karsten_1.jpg', 1)
img_2 = cv2.imread('karsten_2.jpg', 1)

# create a window
cv2.namedWindow("My Pet")

# define a null callback function
def null(x):
    pass

# create a trackbar 
# arguments: trackbar_name, window_name, default_value, max_value, callback_fn
cv2.createTrackbar("Switch_Image", "My Pet", 0, 1, null)
while True:
    # get Trackbar position
    pos = cv2.getTrackbarPos("Switch_Image", "My Pet")
    if pos == 0:
        cv2.imshow("My Pet", img_1)
    elif pos == 1:
        cv2.imshow("My Pet", img_2)
    key = cv2.waitKey(1) & 0xFF
    # press 'q' to quit the window
    if key == ord('q'):
        break
cv2.destroyAllWindows()