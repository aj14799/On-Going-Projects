from tkinter import*
from tkinter import ttk
from tkinter import messagebox, filedialog
#from PIL import ImageTk, Image
import os
import pandas as pd
import time
import smtplib
from email.message import EmailMessage
import PyPDF2
from wand.image import Image as wi
from pdf2image import convert_from_path
import cv2
import numpy as np
import matplotlib.pyplot as plt



class color_detector():
    def __init__(self, root):
        self.root = root
        self.root.title("Pdf_mainupulator and Color Checker".center(280))
        self.root.geometry("1000x580+200+75")
        self.root.resizable(False, False)
        self.root.config(bg="black")

# =================Icons==============================
# =================Icons==============================
# =================Icons==============================
# =================Icons==============================


        #self.email_icon = ImageTk.PhotoImage(file="Pics\Email.jpg")
        #self.setting_icon = ImageTk.PhotoImage(file="Pics\Settings.jpg")
        #self.show_icon = ImageTk.PhotoImage(file="Pics\show-password.png")
        #self.file_icon = ImageTk.PhotoImage(file="Pics\images (1).png")
        #self.image_icon = ImageTk.PhotoImage(file="Pics\images.png")

# ======================TOP Frame ===============================
# ======================TOP Frame ===============================
# ======================TOP Frame ===============================
# ======================TOP Frame ===============================


        self.TopFrame = LabelFrame(self.root, bd = 10, text="Pdf Mainupulator and Color Checker", fg="gold",relief=GROOVE, font=("times new roman",20,"bold"), bg = "#081923")
        self.TopFrame.place(x=0, y=0, height=140, relwidth=1)
        
        self.lbl_hr = Label(self.TopFrame,text="12" , font = ("times new roman", 30,"bold"),bg="#0B7587",fg="white")
        self.lbl_hr.place(x=10, y=5, height=50, width=80)
       
        self.lbl_hr2 = Label(self.TopFrame,text="Hours" , font = ("times new roman", 12,"bold"),bg="#0B7587",fg="white")
        self.lbl_hr2.place(x=10, y=60, height=20, width=80)

        self.lbl_min = Label(self.TopFrame,text="12" , font = ("times new roman", 30,"bold"),bg="#3CA59D",fg="white")
        self.lbl_min.place(x=100, y=5, height=50, width=80)
       
        self.lbl_min2 = Label(self.TopFrame,text="MINITUES" , font = ("times new roman", 10,"bold"),bg="#3CA59D",fg="white")
        self.lbl_min2.place(x=100, y=60, height=20, width=80)

        self.lbl_sec = Label(self.TopFrame,text="12" , font = ("times new roman", 30,"bold"),bg="#F62217",fg="white")
        self.lbl_sec.place(x=190, y=5, height=50, width=80)
       
        self.lbl_sec2 = Label(self.TopFrame,text="SECONDS" , font = ("times new roman", 10,"bold"),bg="#F62217",fg="white")
        self.lbl_sec2.place(x=190, y=60, height=20, width=80)
       
        self.lbl_abv = Label(self.TopFrame,text="AM" , font = ("times new roman", 30,"bold"),bg="#F62217",fg="white")
        self.lbl_abv.place(x=280, y=5, height=50, width=80)
       
        self.lbl_abv2 = Label(self.TopFrame,text="MORNING" , font = ("times new roman", 10,"bold"),bg="#F62217",fg="white")
        self.lbl_abv2.place(x=280, y=60, height=20, width=80)

# ======================Left Frame ===============================
# ======================Left Frame ===============================
# ======================Left Frame ===============================
# ======================Left Frame ===============================

        self.LeftFrame = Frame(self.root, bd = 10,relief=GROOVE, bg = "#081923")
        self.LeftFrame.place(x=0, y=140, width=160, height=440)

        self.Button1 = Button(self.LeftFrame, bd = 5,relief=GROOVE, text = "Add Single\n PDF", fg = "white",bg = "#081923")
        self.Button1.place(x=0, y=0, width=140, height=70)

        self.Button2 = Button(self.LeftFrame, bd = 5,relief=GROOVE, text = "Add Multiple\n PDF", fg = "white",bg = "#081923")
        self.Button2.place(x=0, y=70, width=140, height=70)

        self.Button3 = Button(self.LeftFrame, bd = 5,relief=GROOVE, text = "Show PDF", fg = "white",bg = "#081923")
        self.Button3.place(x=0, y=140, width=140, height=70)

        self.Button4 = Button(self.LeftFrame, bd = 5,relief=GROOVE, text = "Get PDF Pages separated\ninto Image form", fg = "white",bg = "#081923")
        self.Button4.place(x=0, y=210, width=140, height=70)

        self.Button5 = Button(self.LeftFrame, bd = 5,relief=GROOVE, text = "Color Detection in Pdf", fg = "white",bg = "#081923", command=self.color_detection)
        self.Button5.place(x=0, y=280, width=140, height=70)

        self.Button5 = Button(self.LeftFrame, bd = 5,relief=GROOVE, text = "Decrypt Pdf", fg = "white",bg = "#081923")
        self.Button5.place(x=0, y=350, width=140, height=70)
        
#=====================Clock Called===============================
#=====================Clock Called===============================
#=====================Clock Called===============================
#=====================Clock Called===============================

        self.clock()

    def clock(self):
        self.h = str(time.strftime("%H"))
        self.m = str(time.strftime("%M"))
        self.s = str(time.strftime("%S"))

        if int(self.h)>=12 and int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")
            self.lbl_abv2.config(text="AFTERNOON")

        if int(self.h)>=15 and int(self.h)<20 and int(self.m)>0:
            self.lbl_abv.config(text="PM")
            self.lbl_abv2.config(text="EVENING")
        
        if int(self.h)>=20 and int(self.h)<24 and int(self.m)>0:
            self.lbl_abv.config(text="PM")
            self.lbl_abv2.config(text="NIGHT")

        if int(self.h)>12 and int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")
            self.lbl_abv2.config(text="AFTERNOON")

        if int(self.h)>12:
            self.h=str(int(self.h)%12)
         
        self.lbl_hr.config(text = self.h)
        self.lbl_min.config(text = self.m)
        self.lbl_sec.config(text = self.s)
        self.lbl_hr.after(200,self.clock)


    def color_detection(self):
        self.f = filedialog.askopenfilename(initialdir='/', title="Choose Document to attach", filetype=(("PDF","*pdf"),("All Files","*.*")))
        self.pdf = wi(filename=self.f, resolution=700)
        self.pdfImage = self.pdf.convert("jpg")
        i=1
        j=0
        for img in self.pdfImage.sequence:
            page = wi(image=img)
            page.save(filename=str(i)+".jpg")
            #time.sleep(20)
            image = cv2.imread(str(i)+".jpg")
            plt.figure(figsize=(20,8))
            rbg_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            hsv_img = cv2.cvtColor(rbg_img, cv2.COLOR_RGB2HSV)
            
            lower = np.array([25, 150, 50])
            upper = np.array([35, 255, 255])
            mask = cv2.inRange(hsv_img,lower,upper)
            #plt.imshow(mask)
            raw_data = {'Page No': [i],'Cyan': ["Yes"],'Magenta': ["Yes"],'Yellow': ["Yes"],'Black': ["Yes"]}
            df = pd.DataFrame(raw_data, columns = ['Page No', 'Cyan','Magenta','Yellow','Black'])
            df.to_csv('data.csv')
            i+=1
            file = pd.ExcelWriter('demo.xlsx',engine='xlsxwriter')
            df = pd.DataFrame({'Page No.':[i],'Cyan':['No']})


root = Tk()
obj = color_detector(root)
root.mainloop()
