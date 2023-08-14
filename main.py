import urllib.request
import cv2
import numpy as np

# from ultralytics.yolo.v8.detect.predict import DetectionPredictor
url = 'http://100.83.126.26:8080/shot.jpg'

while True:
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    

    results = model(url)
    cv2.imshow('Image Recognition', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

