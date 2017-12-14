#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 19:16:04 2017

@author: ding
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
import json
import cv2
import numpy as np
from multiprocessing import Process  

def grovel(driver, t):
    action = ActionChains(driver)
    action.key_down(Keys.DOWN).pause(t).key_up(Keys.DOWN).perform()

def jump(driver):
    action = ActionChains(driver)
    action.send_keys(Keys.SPACE).perform()
    
    
driver = webdriver.Firefox()
driver.get("http://127.0.0.1/t-rex-runner")

time.sleep(0.5)
#browser.maximize_window()
#browser.quit()

jump(driver)

time.sleep(2)


#obj.send_keys(Keys.SPACE)
#time.sleep(2)
#obj.send_keys(Keys.SPACE)


#jump(driver)
#time.sleep(0.5)
#grovel(driver, 1)

def catchScreen():
    obj = driver.find_element_by_class_name("runner-container")
    #obj = driver.find_element_by_id("main-content")
    img = obj.screenshot_as_png
    nparr = np.fromstring(img, np.uint8)
    # CV_LOAD_IMAGE_COLOR
    img_np = cv2.imdecode(nparr, 1) 
    cv2.imshow('a',img_np)

while(1):
    st = time.time()
    obj = driver.find_element_by_class_name("runner-container")
    #obj = driver.find_element_by_id("main-content")
    img = obj.screenshot_as_png
    nparr = np.fromstring(img, np.uint8)
    # CV_LOAD_IMAGE_COLOR
    img_np = cv2.imdecode(nparr, 1)
    print(time.time()-st)    
    cv2.imshow('a',img_np)

    if cv2.waitKey(1) & 0xFF == ord('q'):    
        driver.quit()
        break


img=cv2.imread('/home/ding/Documents/code/nginx/t-rex-runner/T-rex.png')
cv2.imshow('b',img)





