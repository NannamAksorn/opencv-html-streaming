from streamer import streamer
import cv2

#redis server host:port
HOST = "0.0.0.0"
PORT = 6379

#webcam ID
DEVICE = 0
WIDTH = 1280
HEIGHT = 720
QUALITY = 70

s = streamer(host=HOST, port=PORT)

cap = cv2.VideoCapture(DEVICE)
cap.set(3,WIDTH)
cap.set(4,HEIGHT)
#mjpeg
cap.set(6,1196444237.0)

while True:
    ret, frame = cap.read()
    if not ret:
        break 
# TODO function(frame) 
    cv2.imshow("client Webcam", frame)
    s.broadcast(frame, quality=QUALITY)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()