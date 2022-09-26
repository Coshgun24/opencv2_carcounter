import cv2
import numpy as np

background = cv2.createBackgroundSubtractorMOG2()
capture = cv2.VideoCapture('video.avi')
i = 0
minArea = 2600
while True:
    ret, frame = capture.read()
    fgmask = background.apply(frame, None, 0.02)
    erode1 = cv2.erode(fgmask,None,iterations=4)
    moments = cv2.moments(erode1, True)
    area=moments['m00']
    #horizontal top
    cv2.line(frame, (40, 0), (40, 176), (255, 0, 0), 2)
    cv2.line(frame, (55, 0), (55, 176), (255, 0, 0), 2)
    #vertical top
    cv2.line(frame, (0, 50), (320, 50), (255, 0, 0), 2)
    cv2.line(frame, (0, 65), (320, 65), (255, 0, 0), 2)
    #horizontal bottom
    cv2.line(frame, (100, 0), (100, 176), (0, 255, 255), 2)
    cv2.line(frame, (115, 0), (115, 176), (0, 255, 255), 2)
    #vertical bottom
    cv2.line(frame, (0, 105), (320, 105), (0, 255, 255), 2)
    cv2.line(frame, (0, 130), (320, 130), (0, 255, 255), 2)

    if moments['m00'] >= minArea:
        x = int(moments['m10'] / moments['m00'])
        y = int(moments['m01'] / moments['m00'])

        print('moment: '+str(moments['m00'])+" x : "+str(x)+" y : "+str(y))
        if x > 40 and x < 50 and y > 50 and y < 65:
            i=i+1
            print("above: "+str(i))
        elif x > 102 and x < 110 and y > 105 and y < 130:
            i=i+1
            print("below: " + str(i))

    cv2.putText(frame, 'Count:%r' % i, (200, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('frame', frame)
    cv2.imshow('fgmask', fgmask)
    key = cv2.waitKey(25)
    if key == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()