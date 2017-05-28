import numpy
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import time
camera = PiCamera()
camera.resolution = (592, 432)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(592, 432))
time.sleep(0.1)
for x in (0,100):
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        img = frame.array
        img = img[200:432, 100:300]
        cv2.imshow("Frame",img)
        key = cv2.waitKey(1) & 0xFF
        rawCapture.truncate(0)
        if key == ord("q"):
            break
    '''if key == ord("1"):
        img = frame.array
        average_color_per_row = numpy.average(img, axis=0)
        average_color = numpy.average(average_color_per_row, axis=0)
        average_color = numpy.uint8(average_color)
        average_color_img = numpy.array([[average_color]*100]*100, numpy.uint8)
        cv2.imwrite( "average_color.png", average_color_img )
        print(average_color)

    elif key == ord("2"):
        img = frame.array
        average_color_per_row = numpy.average(img, axis=0)
        average_color = numpy.average(average_color_per_row, axis=0)
        average_color = numpy.uint8(average_color)
        average_color_img = numpy.array([[average_color]*100]*100, numpy.uint8)
        cv2.imwrite( "average_color.png", average_color_img )
        print(average_color)
    elif key == ord("3"):
        img = frame.array
        average_color_per_row = numpy.average(img, axis=0)
        average_color = numpy.average(average_color_per_row, axis=0)
        average_color = numpy.uint8(average_color)
        average_color_img = numpy.array([[average_color]*100]*100, numpy.uint8)
        cv2.imwrite( "average_color.png", average_color_img )
        print(average_color)
    elif key == ord("4"):
        img = frame.array
        average_color_per_row = numpy.average(img, axis=0)
        average_color = numpy.average(average_color_per_row, axis=0)
        average_color = numpy.uint8(average_color)
        average_color_img = numpy.array([[average_color]*100]*100, numpy.uint8)
        cv2.imwrite( "average_color.png", average_color_img )
        print(average_color)
    if key == ord("q"):
        break'''
    average_color_per_row = numpy.average(img, axis=0)
    average_color = numpy.average(average_color_per_row, axis=0)
    average_color = numpy.uint8(average_color)
    average_color_img = numpy.array([[average_color]*100]*100, numpy.uint8)
    cv2.imwrite( "average_color.png", average_color_img )

    print(average_color)
