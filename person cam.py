import os
import cv2
import time
import numpy as np


capture = cv2.VideoCapture("http://192.168.0.91:5001/mjpg/video.mjpg")

fgbg = cv2.createBackgroundSubtractorMOG2(300, 400, True)

frameCount = 0

while True:
	ret, frame = capture.read()

	fgmask = fgbg.apply(frame)

	count = np.count_nonzero(fgmask)

	print('Pixel Count: %d' % (count))

	if (count > 1900):
	    print('Bezoeker')
	    os.system('start "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://192.168.0.91:5001/mjpg/video.mjpg')

	k = cv2.waitKey(1) & 0xff
	if k == 27:
		break

capture.release()
cv2.destroyAllWindows()