#importing libraries

import cv2
import os
from pathlib import Path
import tkinter as tk
import tkinter.font as tkFont
import glob
import shutil
import subprocess
import numpy as np
from matplotlib import pyplot as plt

#implements cascade classifier 

face_cascade = cv2.CascadeClassifier('C:/Users/confi/OneDrive/Documents/Senior Project/Photo_reg/cascade_face.xml')

#Making folders
images_dir = "C:/Users/confi/OneDrive/Documents/Senior Project/Photo_reg/Images"
photo_face = "C:/Users/confi/OneDrive/Documents/Senior Project/Photo_reg/photo_neg"
photo_neg = "C:/Users/confi/OneDrive/Documents/Senior Project/Photo_reg/photo_face"

# Image processing
def image_pro(face_cascade,images_dir):
    for image in glob.iglob(f'{images_dir}/*'):    
        
        img = cv2.imread(image)
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray_image,1.1,2)
    
        
        if len(faces) == 0:
            shutil.move(image, photo_face)
        else: 
            shutil.move(image, photo_neg)
        
# image_pro(face_cascade, images_dir)

def main():
        root = tk.Tk()

    #setting title
        root.title("Face Detection")
        #setting window size
        width=500
        height=310
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        title_butt=tk.Message(root)
        ft = tkFont.Font(family='Times',size=20)
        title_butt["font"] = ft
        title_butt["fg"] = "#f82222"
        title_butt["justify"] = "center"
        title_butt["text"] = "Face Detection"
        title_butt.place(x=130,y=30,width=210,height=77)

        Insert_butt=tk.Button(root)
        Insert_butt["bg"] = "#280100"
        ft = tkFont.Font(family='Times',size=10)
        Insert_butt["font"] = ft
        Insert_butt["fg"] = "#f82222"
        Insert_butt["justify"] = "center"
        Insert_butt["text"] = "Insert"
        Insert_butt.place(x=130,y=110,width=70,height=25)
        Insert_butt.command = Insert_butt_command

        Faces_butt=tk.Button(root)
        Faces_butt["bg"] = "#280100"
        ft = tkFont.Font(family='Times',size=10)
        Faces_butt["font"] = ft
        Faces_butt["fg"] = "#f82222"
        Faces_butt["justify"] = "center"
        Faces_butt["text"] = "Faces"
        Faces_butt.place(x=270,y=110,width=70,height=25)
        Faces_butt.command = Faces_butt_command

        No_Faces_butt=tk.Button(root)
        No_Faces_butt["bg"] = "#280100"
        ft = tkFont.Font(family='Times',size=10)
        No_Faces_butt["font"] = ft
        No_Faces_butt["fg"] = "#f82222"
        No_Faces_butt["justify"] = "center"
        No_Faces_butt["text"] = "No Faces"
        No_Faces_butt.place(x=270,y=160,width=70,height=25)
        No_Faces_butt.command = No_Faces_butt_command

        process_butt=tk.Button(root)
        process_butt["bg"] = "#280100"
        ft = tkFont.Font(family='Times',size=10)
        process_butt["font"] = ft
        process_butt["fg"] = "#f82222"
        process_butt["justify"] = "center"
        process_butt["text"] = "Process"
        process_butt.place(x=130,y=160,width=70,height=25)
        process_butt.command = process_butt_command()
        
        root.mainloop()


def Insert_butt_command():
    subprocess.Popen(r'explorer "C:/Users/confi/OneDrive/Documents/Senior Project/Photo_reg/Images"')


def Faces_butt_command():
    subprocess.Popen(r'explorer "C:/Users/confi/OneDrive/Documents/Senior Project/Photo_reg/photo_face"')
    


def No_Faces_butt_command():
    subprocess.Popen(r'explorer "C:/Users/confi/OneDrive/Documents/Senior Project/Photo_reg/photo_neg"')


def process_butt_command():
    image_pro(face_cascade, images_dir )



main()



