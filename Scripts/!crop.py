# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:40:30 2017

@author: DREAM
"""

import cv2, os
from os import listdir
import numpy as np
from os.path import isfile, join

lst_file, lst_count, cwd = [],[],""

file = ""

diff_click = 100

'''sets console size'''
width = 50
lines = 40
cent_width = int(width)-1

save_dir = "Parsed"

#define cosole size and color
os.system("mode con: cols=" + str(width) + " lines=" + str(lines))
os.system("color F")
os.system("cls")
os.system("echo off")

def init_files():
    global lst_file, lst_count, cwd, item
    lst_file = []
    lst_count = []
    cwd = os.getcwd()
    
    for file in os.listdir(cwd):
        
        #print (file)
        lst_file.append(file)
        
    count = range(len(lst_file))

    for i in count:
        lst_count.append(i)

    item = input("Item to Parse: ")
    print ("Diff Value = "+str(diff_click))
    print ("Press 'ESC' to Close Windows")
    print ("Press 'Space' to Refresh Image")
    print ("Press 'E' to Change Diff Value")
    print ("Press 'Enter' to Parse Image")
       
        
def run_images():        
    #global image
   
    for file in lst_file:
        if not file.endswith('.py') and not file.endswith(".bat"):
            print(file)
    
            show_image(file) 
                           
    # close any open windows
    cv2.destroyAllWindows()
        
        
def show_image(fname):
    global image, diff_click
    
    file = fname
    #print(file)
    image = cv2.imread(file)
    cv2.namedWindow(file, cv2.WINDOW_NORMAL)

    cv2.setMouseCallback(file,draw_image)
    while(1):
        cv2.imshow(file,image)
        #cv2.moveWindow(file, 0, 0)
        if cv2.waitKey(0) & 0xFF == 27: #esc key
            break
        elif cv2.waitKey(5) & 0xFF == 32: #space bar
            print ("Refreshing Image - " + file)
            cv2.destroyWindow(file)
            show_image(file)
        elif cv2.waitKey(5) & 0xFF == 61: #Up - Chage Diff 10
            diff_click+=10
            print ("Diff Value = "+str(diff_click))
        elif cv2.waitKey(5) & 0xFF == 45: #Down - Chage Diff 10
            diff_click-=10
            print ("Diff Value = "+str(diff_click))            
        elif cv2.waitKey(5) & 0xFF == 101 or cv2.waitKey(20) & 0xFF == 69: #e - Chage Diff
            print ("Diff Value = "+str(diff_click))            
            diff_click = int(input("Change Diff Value to: "))
        elif cv2.waitKey(5) & 0xFF == 13:#Enter - Crop
            if mouse_x == 0 or mouse_y == 0:
                print("No Mouse Instructions")
            else:
                crop_image(file)
            
            
            
    cv2.destroyAllWindows()
    
# mouse callback function
def draw_image(event,x,y,flags,param):
    global mouse_x, mouse_y
    
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(image,(x,y),100,(255,0,0),1)

    elif event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.rectangle(image,(x-diff_click,y-diff_click),
                      (x+diff_click,y+diff_click),(0,255,0),2)        
        
        mouse_x = x
        mouse_y = y
        
        print ("Mouse Click - "+str(mouse_x)+" - "+str(mouse_y)+
               " - Diff - "+str(diff_click))
        
def crop_image(fname):
    img = cv2.imread(fname)
    crop_img = img[mouse_y-diff_click:mouse_y+diff_click, 
                   mouse_x-diff_click:mouse_x+diff_click]
                   
    #cv2.imshow((item+"-"+fname), crop_img) 
    mk_dir("..//"+save_dir)
    cv2.imwrite(("..//"+save_dir+"//"+item+" - "+fname),crop_img)  
    print ("Writing ..//"+save_dir+"//"+item+" - "+fname)                
    

'''create folder'''
def mk_dir(name):
    if not os.path.exists(name):
        os.makedirs(name)    
            
        
if __name__ == "__main__":
    init_files()
    run_images()        
        
