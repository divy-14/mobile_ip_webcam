import cv2
import numpy as np
import requests
import io

ip = input("Enter the ipv4 address for your ip webcam: ")
url = ip + "/shot.jpg"

while True:

    img_request = requests.get(url)
    img_arrint = np.array(bytearray(img_request.content), dtype=np.uint8)
    img = cv2.imdecode(img_arrint, -1)
    cv2.imshow("video-stream", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
