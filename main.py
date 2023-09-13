import cv2
import handy
cap = cv2.VideoCapture(0)
hist = handy.capture_histogram(source=0)
while True:
    ret, frame = cap.read()
