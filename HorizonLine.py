#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 10:25:53 2017

@author: ding
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
import time

WIDTH = 600
class HorizonLine:
    def __init__(self):
        self.spriteXPos = 2
        self.spriteYPos = 54
        self.width = 600
        self.height = 12
        self.xPos = [0, 600]
        self.yPos = 127
        self.bumpThreshold = 0.5
        self.sourceXPos = [2, 602]


    def draw(self, canvas, sprite):
        canvas = drawCanvas(canvas, sprite, self.xPos[0], self.yPos,
                            self.sourceXPos[0], self.spriteYPos,
                            self.width, self.height)
        canvas = drawCanvas(canvas, sprite, self.xPos[1], self.yPos,
                            self.sourceXPos[1], self.spriteYPos,
                            self.width, self.height)
        return canvas

    def update(self, deltaTime, speed):
        movement = int(speed * deltaTime * 1000)

        self.xPos[0] -= movement
        self.xPos[1] -= movement

        if self.xPos[0] < -600:
            self.xPos[0] = self.xPos[1]
            self.sourceXPos[0] = self.sourceXPos[1]
            self.xPos[1] = self.xPos[0] + 600
            self.sourceXPos[1] = self.getRandom() + self.spriteXPos


    def getRandom(self):
        if random.random() > self.bumpThreshold:
            return 600
        else:
            return 0

def drawCanvas(canvas, sprite, xPos, yPos, sourceXPos, sourceYPos, width, height):
    """
    canvas: 600X150的画布，x坐标范围0-600
    sprite: 1233X68的sprite图
    xPos: 部件在canvas坐标系下的坐标
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

    ground = HorizonLine()

    canvas = ground.draw(canvas, sprite)
    cv2.imshow('t-rex',canvas)

    while True:
        st = time.time()
        canvas = ground.draw(canvas, sprite)
        cv2.imshow('t-rex',canvas)
        time.sleep(0.01)
        speed = 1/3
        ground.update(time.time()-st, speed)
        ch = cv2.waitKey(1)
        if ch == 27:
            break
    cv2.destroyAllWindows()
