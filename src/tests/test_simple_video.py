""" simple test script to load and display a video with OpenCV

* 25.10.2017 - Oli Moser (https://twitter.com/moseroli)
"""

import cv2

cap = cv2.VideoCapture("../resources/videos/sonnenbrillen_test.mp4")

while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)

    key = cv2.waitKey(1) & 0xff

