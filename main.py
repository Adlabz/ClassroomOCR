# Python code to detect an arrow (seven-sided shape) from an image.
import numpy as np
import imutils
import cv2

while True:
    page_in_frame = False
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()
    cv2.imwrite('stack.jpg', frame)
    image = cv2.imread('stack.jpg',-1)
    paper = cv2.resize(image,(500,500))
    ret, thresh_gray = cv2.threshold(cv2.cvtColor(paper, cv2.COLOR_BGR2GRAY),
                            200, 255, cv2.THRESH_BINARY)
    contours, hier = cv2.findContours(thresh_gray, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    if len(contours) < 10:
        page_in_frame = True #probably
        for c in contours:
            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            # convert all coordinates floating point values to int
            box = np.int0(box)
            # draw a green 'nghien' rectangle
            cv2.drawContours(paper, [box], 0, (0, 255, 0),1)

    cv2.imshow('paper', paper)
    #cv2.imwrite('paper.jpg',paper)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
