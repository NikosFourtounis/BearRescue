# import the necessary packages
from gpiozero import LED, Button
from time import sleep
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import time
import numpy as np
from cv2 import countNonZero
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (592, 432)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(592, 432))


led1 = LED(4)
led2 = LED(21)
 
time.sleep(0.05)
boundaries = [
	([20, 20, 50], [62, 45, 120])
]
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
##    led2.on()
    image = frame.array
    image2 = image[200:432, 133:399]
##    image =image[0:432,100:400]
    counter=0
    
##    print(frame.array[290,215])
    for (lower, upper) in boundaries:
       lower = np.array(lower, dtype = "uint8")
       upper = np.array(upper, dtype = "uint8")
       mask = cv2.inRange(image, lower, upper)
       mask2 = cv2.inRange(image2,lower, upper)
       print("mask 1",countNonZero(mask ),"mask 2",countNonZero(mask2 ))
       if countNonZero(mask2)>4000:
           led1.off()
           print('sent led2')
           led2.off()
       elif countNonZero(mask)>1000:
           led1.on()
       else:
           led2.on()
           led1.off()
       output = cv2.bitwise_and(image, image, mask = mask)
       cv2.imshow("images", np.hstack([image, output]))
             
    key = cv2.waitKey(1) & 0xFF
##    cv2.imshow("Frame", image)
    rawCapture.truncate(0)
    if key == ord("q"):
        break
        
        
