#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:33:19 2017

@author: ding
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
import time
from HorizonLine import HorizonLine
from Cloud import Clouds
WIDTH = 600

def drawCanvas(canvas, sprite, xPos, yPos, sourceXPos, sourceYPos, width, height):
    """
    canvas: 600X150的画布，x坐标范围0-600
    sprite: 1233X68的sprite图
    xPos: 部件在canvas坐标系下的x坐标
    yPos: 部件在canvas坐标系下的y坐标
    sourceXPos: 部件在sprite中的位置
    width: 部件的长度
    height: 部件的高度
    """
    if xPos < 0:
        canvas[yPos: yPos+height, 0:xPos+width] = \
            sprite[sourceYPos: sourceYPos+height, sourceXPos-xPos: sourceXPos+width]
        return canvas
    if xPos + width > 600:
        canvas[yPos: yPos+height, xPos:600] = \
            sprite[sourceYPos: sourceYPos+height, sourceXPos: sourceXPos+600-xPos]
        return canvas
    canvas[yPos: yPos+height, xPos:xPos+width] = \
        sprite[sourceYPos: sourceYPos+height, sourceXPos: sourceXPos+width]
    return canvas      



if __name__ == '__main__':
           
    sprite = cv2.imread('/home/ding/Downloads/t-rex.png')
    canvas = np.ones((150,600,3), np.uint8) * 255
    
    #cv2.namedWindow('b', cv2.WINDOW_NORMAL)
    #cv2.imshow('b',sprite)
    speed = 1/2
    
    ground = HorizonLine()
    clouds = Clouds()
    clouds.addCloud()
    canvas = clouds.draw(canvas,sprite)
    canvas = ground.draw(canvas, sprite)
    cv2.imshow('t-rex',canvas)
            
    while True:
        canvas = np.ones((150,600,3), np.uint8) * 255
        st = time.time()
        canvas = ground.draw(canvas, sprite)
        canvas = clouds.draw(canvas, sprite)
        cv2.imshow('t-rex',canvas)
        time.sleep(0.01)
        ground.update(time.time()-st, speed)
        clouds.update(time.time()-st, speed)
        ch = cv2.waitKey(1)
        if ch == 27:
            break
    cv2.destroyAllWindows()
