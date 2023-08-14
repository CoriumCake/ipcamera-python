import urllib.request
import cv2
import numpy as np

url = 'http://<local_ip:port>/shot.jpg'

while True:
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    

    results = model(url)
    cv2.imshow('Image Recognition', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

