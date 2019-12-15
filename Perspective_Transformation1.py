# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:51:16 2019

@author: Aniruddha
"""

import cv2
import numpy as np                           #support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.


def pi_camera(conti_display=False):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if conti_display:
            
            
            cv2.circle(img, (460, 266), 5, (0, 255, 0), -1)            #parameters:(image name, position{(left to right; top to bottom; radius in pixles); color (B, G, R); thickness)}

            cv2.circle(img, (180, 266), 5, (0, 255, 0), -1)
            cv2.circle(img, (620, 436), 5, (0, 255, 0), -1)
            cv2.circle(img, (10, 436), 5, (0, 255, 0), -1)
            
            actual_positions = np.float32([[460, 266], [180, 266], [620, 436], [10, 436]])   #Original
#             actual_positions = np.float32([[470, 56], [470, 356], [170, 106], [170, 356]])   #Experimental
#             birdeye_view_position = np.float32([[0, 0], [400, 0], [0, 600], [400, 600]])
            birdeye_view_position = np.float32([ [400, 0], [0, 0], [400, 600], [0, 600]])
            matrix = cv2.getPerspectiveTransform(actual_positions, birdeye_view_position)
            result =cv2.warpPerspective(img, matrix, (400, 600))
             
            img = cv2.flip(img, 1)
            cv2.imshow('Vehicle camera', img)
            cv2.imshow('Perspective Transformation', result)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    pi_camera(conti_display=True)


if __name__ == '__main__':
    main()