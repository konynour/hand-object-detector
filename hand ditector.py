import cv2
from cvzone.HandTrackingModule import HandDetector
import controller as cnt

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=2)
while True:

    success, img = cap.read()
    fingers1 = []
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, draw=True, flipType=False)

    if hands:

        hand1 = hands[0]
        lmList1 = hand1

        fingers1 = detector.fingersUp(lmList1)
        print(fingers1)
        cnt.led(fingers1)

        if fingers1 == [1, 0, 0, 0, 0]:
            cv2.putText(img, 'Finger count:0', (200, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingers1 == [1, 1, 0, 0, 0]:
            cv2.putText(img, 'Finger count:1', (200, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingers1 == [1, 1, 1, 0, 0]:
            cv2.putText(img, 'Finger count:2', (200, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingers1 == [1, 1, 1, 1, 0]:
            cv2.putText(img, 'Finger count:3', (200, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingers1 == [1, 1, 1, 1, 1]:
            cv2.putText(img, 'Finger count:4', (200, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingers1 == [0, 1, 1, 1, 1]:
            cv2.putText(img, 'Finger count:5', (200, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow("tracker", img)
    k = cv2.waitKey(1)
    if k == ord("k"):
        break

cap.release()
cv2.destroyAllWindows()
