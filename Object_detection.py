# import the necessary packages##
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import mycar_1_led_motor
import turn
import mycar_0_led

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)

#For yellow ball which is our object
lightYellow = (29, 8, 93)
brightYellow = (36, 255, 247)

mycar_0_led.setup()  
#Read and display video frames until video is completed or 
#user quits by pressing ESC
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
  
    frameR = frame.array
    output = frameR.copy()
    hsv_frame = cv2.cvtColor(frameR, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, lightYellow, brightYellow)
    
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
    im2, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    #cv2.drawContours(frameR,contours,-1,(0,255,0), 3)
    
    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    if(len(contour_sizes) > 0):
        biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
        #cv2.drawContours(frameR,biggest_contour,-1,(0,255,0), 3)
        topLeft_X_value, topLeft_Y_value, width, height = cv2.boundingRect(biggest_contour)
        #comment while deploying
        cv2.rectangle(frameR,(topLeft_X_value,topLeft_Y_value),(topLeft_X_value+width,topLeft_Y_value+height),(0,255,0), 3)                        #Let (x,y) be the top-left coordinate of the rectangle and (w,h) be its width and height
        
        closeness_of_object = topLeft_Y_value
#         print("topLeft_X_value",topLeft_X_value)
#         print("width",width)
#         print("topLeft_Y_value",topLeft_Y_value)
#         print("height",topLeft_Y_value)
        print("Centre",closeness_of_object)
        cv2.imshow("Cont", frameR)
        cv2.imshow("MASK", mask) 
        turn.ahead()
#         mycar_1_led_motor.motor_forward()
        if(closeness_of_object>230):
#                 print("closeness_of_object=",closeness_of_object)
                print("Stop")
#                 mycar_1_led_motor.motorStop()
#                 time.sleep(2)
                
# #                 turn.right()
# #                 mycar_1_led_motor.motor_forward()
# #                 turn.middle()
# #                 mycar_1_led_motor.motor_forward()
# #                 turn.left()
# #                 mycar_1_led_motor.motor_forward()
# #                 turn.middle()
# #                 mycar_1_led_motor.motor_forward()
                
                
#                 time.sleep(1)
#                 turn.right()
#                 mycar_1_led_motor.motor_forward()
#                 time.sleep(1)
#                 
#                 turn.middle()
#                 mycar_1_led_motor.motor_forward()
#                 time.sleep(1)
#                 
#                 turn.left()
#                 mycar_1_led_motor.motor_forward()
#                 time.sleep(2)
#                 
#                 turn.middle()
#                 mycar_1_led_motor.motor_forward()
#                 time.sleep(1)
#                 mycar_1_led_motor.motorStop()
#                 time.sleep(2)
#                 mycar_1_led_motor.motor_motor_forward_obstacle_avoidance()
        else:
##                mycar_1_led_motor.motor_forward()
                print("closeness_of_object=",closeness_of_object)
#                 mycar_0_led.right_on()
#                 mycar_1_led_motor.motor_forward()
#                 time.sleep(1)
#                 mycar_1_led_motor.motorStop()
#                 time.sleep(5)
                
#                 mycar_1_led_motor.motor_right(1,1,50)
#                 
#                 mycar_1_led_motor.motorStop()
#                 time.sleep(1)
           #now lets see how far it is from center of camera
    #comment while deploying
#     cv2.imshow("Cont", frameR)
#     cv2.imshow("MASK", mask) 
    
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
    elif key == ord("s"):
        cv2.imwrite('BallImage.jpg',frameR)
    
        
# Closes all the frames
cv2.destroyAllWindows()