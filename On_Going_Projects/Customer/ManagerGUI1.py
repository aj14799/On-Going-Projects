# ====================== Importing Module ==================
# ====================== Importing Module ==================

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import colorchooser
from datetime import datetime
import time
import cv2
import pyzbar.pyzbar as pyzbar
import sqlite3



class win1:
    def __init__(self, root):

        self.root = root
        self.root.geometry("1200x1920+1370+0")
        self.root.title("Customers".center(160))

        # =================== Entry ============================================
        now = datetime.now()
        self.Ent_Time=now.strftime('%H:%M:%S')

        self.Ent_today= now.strftime("%d-%b-%Y")

        # =================== Icons and Variables ===============================

        #self.Icon1 = ImageTk.PhotoImage(file="Pics\\2.jpg")
        self.Icon1 = ImageTk.PhotoImage(file="Pics\\29662560_562856114083046_3446062735052646088_o.jpg")
        self.Icon2 = ImageTk.PhotoImage(file="Pics\\Annotation 2020-07-09 104744.png")
        self.obj = ""
        self.A1 = StringVar()
        self.A2 = StringVar()
        self.A3 = StringVar()
        self.A4 = StringVar()
        self.A5 = StringVar()
        self.Entry = StringVar()
        self.color = StringVar()
        self.EntryE3 = StringVar()

        # =================== Row 1 =============================
        # =================== Row 1 =============================
        # =================== Row 1 =============================
        # =================== Row 1 =============================

        self.lbl1 = Label(self.root, bg=defaultbg,
                          text="Total Number Visit", font=("Open Sans", 30))
        self.lbl1.place(x=140, y=160)

        self.lbl2 = Label(self.root, text="94", font=("Open Sans", 30))
        self.lbl2.place(x=520, y=160)

        self.button1 = Button(self.root, relief=GROOVE, bd=3, text="Postcode", font=(
            "Open Sans", 20), fg="#FFFFFF", activeforeground="#FFFFFF", bg="#FF1493", activebackground="#FF1493", cursor="hand2", command=self.postcode)
        self.button1.place(x=660, y=158, height=55, width=230)

        self.button2 = Button(self.root, relief=GROOVE, bd=3, text="Edit", bg="#FFFFFF", font=(
            "Open Sans", 20), activebackground="#FFFFFF", cursor="hand2", command=self.edit)
        self.button2.place(x=910, y=158, height=55, width=170)
        # ==================== Row 2 =================================
        # ==================== Row 2 =================================
        # ==================== Row 2 =================================
        # ==================== Row 2 =================================

        self.Entry1 = Entry(self.root, bg=defaultbg,
                            bd=2, font=("Open Sans", 60))
        self.Entry1.place(x=110, y=230, width=265)
        self.Entry1.insert(0, "ID: 336")
        self.Entry1.config(state=DISABLED)

        self.lbl3 = Label(self.root, text="[", font=("Open Sans", 60,))
        self.lbl3.place(x=380, y=225)

        self.Entry2 = Entry(self.root, bd=0, textvariable=self.Entry, bg=defaultbg,
                            font=("Open Sans", 37))
        self.Entry2.place(x=410, y=249, width=490)
        self.Entry2.insert(0, "Enter name if known")

        self.lbl4 = Label(self.root, text="]", font=("Open Sans", 60,))
        self.lbl4.place(x=880, y=225)

        # ======================== Row 3 =============================
        # ======================== Row 3 =============================
        # ======================== Row 3 =============================
        # ======================== Row 3 =============================

        self.lbl5 = Entry(self.root,bd=0,
                          font=("Open Sans", 35), bg = defaultbg)
        self.lbl5.place(x=130, y=330,width =310)
        self.lbl5.insert(0,"New Customer")
        self.lbl5.config(state="disable")
        
        #self.cust= StringVar()
        #self.cust.set("New Customer")
        #combo_cust = OptionMenu(self.root,self.cust,"New Customer","Old Customer" )
        #combo_cust.place(x=137, y=330, height=70, width=310)
        #combo_cust.config(bg="#FFFFFF", font=("Open Sans", 30),bd=3)

        self.val = StringVar()
        self.val2 = StringVar()

        R1 = Radiobutton(self.root, bd=2, font=("times new roman", 15, "bold"), relief=GROOVE, text="M",
                         bg="#FFFF33", activebackground="#FFFF33", value="M", variable=self.val, cursor="hand2", command=self.MandF)
        R1.place(x=485, y=340, height=55)

        R2 = Radiobutton(self.root, bd=2, font=("times new roman", 15, "bold"), relief=GROOVE, text="F",
                         activebackground="#FFFF33", bg="#FFFFFF", variable=self.val, value="F", cursor="hand2", command=self.MandF)
        R2.place(x=540, y=340, height=55, width=50)

        R3 = Radiobutton(self.root, bd=2, font=("times new roman", 25, "bold"), relief=GROOVE,
                         text="5-25", bg="#FFFF33", value="5-25", variable=self.val2, cursor="hand2", command=self.ages)
        R3.place(x=610, y=340, height=55, width=140)

        R4 = Radiobutton(self.root, bd=2, font=("times new roman", 25, "bold"), relief=GROOVE, text="26-40",
                         bg="blue", fg="#FFFFFF", value="26-40", variable=self.val2, cursor="hand2", command=self.ages)
        R4.place(x=765, y=340, height=55, width=140)

        R5 = Radiobutton(self.root, bd=2, font=("times new roman", 25, "bold"), relief=GROOVE, text="41-99",
                         bg="blue", fg="#FFFFFF", value="41-99", variable=self.val2, cursor="hand2", command=self.ages)
        R5.place(x=920, y=340, height=55, width=140)

        self.val.set("M")
        self.val2.set("5-25")

        # =============================== Row 4 =====================================
        # =============================== Row 4 =====================================
        # =============================== Row 4 =====================================
        # =============================== Row 4 =====================================

        self.lbl6 = Label(self.root, text="Good Customer",
                          fg="red", font=("Open Sans", 40))
        self.lbl6.place(x=135, y=430)
        
        self.cond=StringVar()
        self.cond.set("CONDITION")

        combo_code = OptionMenu(self.root,self.cond,"Good Customer","Problem","Banned","Banned", "Do not Serve", "Code Red", "Code Green","Code Pink",command=self.condition )
        combo_code.place(x=760, y=422, height=70, width=265)
        combo_code.config(bg="#FFFFFF", font=("Open Sans", 30),bd=3)

        self.color_btn = Button(self.root, relief=GROOVE, bd=3, bg="#FFFFFF",
                              activebackground="#FFFFFF", text="COLOR CHOOSER", font=("Open Sans", 15), cursor="hand2", command=self.colorchoose)
        self.color_btn.place(x=550, y=425, height=65, width=200)
    
        # =============================== Row 5 =====================================
        # =============================== Row 5 =====================================
        # =============================== Row 5 =====================================
        # =============================== Row 5 =====================================

        self.button4 = Button(self.root, relief=GROOVE, bd=2, bg="red", activebackground="red", fg="#FFFFFF",
                              activeforeground="#FFFFFF", text="SURVEY", font=("Open Sans", 30, "bold"), cursor="hand2", command=self.survey)
        self.button4.place(x=142, y=520, height=73, width=280)

        self.button5 = Button(self.root, relief=GROOVE, bd=2, bg="#FFFFFF", activebackground="#FFFFFF",
                              text="SPARE", font=("Open Sans", 30, "bold"), cursor="hand2")
        self.button5.place(x=470, y=520, height=73, width=280)

        self.button6 = Button(self.root, relief=GROOVE, bd=2, bg="#FFFFFF", activebackground="#FFFFFF",
                              text="SPARE", font=("Open Sans", 30, "bold"), cursor="hand2")
        self.button6.place(x=788, y=520, height=73, width=280)

        # =============================== Row 6 =====================================
        # =============================== Row 6 =====================================
        # =============================== Row 6 =====================================
        # =============================== Row 6 =====================================

        self.button4_s = Button(self.root, relief=GROOVE, bd=2, state=DISABLED, bg="#000000", cursor="hand2")
        self.button4_s.place(x=142, y=615, height=73, width=280)

        self.button5_s = Button(self.root, relief=GROOVE, bd=2,state=DISABLED, bg="#000000",cursor="hand2")
        self.button5_s.place(x=470, y=615, height=73, width=280)

        self.button6_s = Button(self.root, relief=GROOVE, bd=2, state=DISABLED, bg="#000000", cursor="hand2")
        self.button6_s.place(x=788, y=615, height=73, width=280)

        # =============================== Row 7 =======================================
        # =============================== Row 7 =======================================
        # =============================== Row 7 =======================================
        # =============================== Row 7 =======================================

        self.lbl7 = Label(self.root, bd=2, relief=GROOVE,
                          bg="#FFFF33", image=self.Icon1)
        self.lbl7.place(x=200, y=720, width=360, height=350)

        Table_Frame = Frame(self.root, bd=6, relief=RIDGE, bg=defaultbg)
        Table_Frame.place(x=600, y=720, width=380, height=345)

        self.table = Text(Table_Frame, bd=0,font=("Open Sans", 15), bg=defaultbg)
        self.table.insert(INSERT,("Date                                           Time\n10-07-2020                           23:05:23\n09-07-2020                           20:35:23"))
        self.table.place(x=0,y=0,width=370,height=170)
        self.table.configure(state="disabled")
        #self.table.heading("Date", text="DATE")
        #self.table.heading("Time", text="TIME")

        separator1 = ttk.Separator(self.root, orient='horizontal')
        separator1.place(x=600, width=380, y=1070)

        # =============================== Row 8 =======================================
        # =============================== Row 8 =======================================
        # =============================== Row 8 =======================================
        # =============================== Row 8 =======================================

        self.button7 = Button(self.root, relief=GROOVE, bd=2, bg="#00FF00", activebackground="#00FF00",
                              fg="#FFFFFF", activeforeground="#FFFFFF", text="Left Bldg", font=("Open Sans", 30), cursor="hand2", command=self.leftbldg)
        self.button7.place(x=142, y=1100, height=70, width=170)

        self.button8 = Button(self.root, relief=GROOVE, bd=2, bg="#909090", activebackground="#909090",
                              fg="#FFFFFF", activeforeground="#FFFFFF", text="Delete", font=("Open Sans", 30), cursor="hand2",command=self.delete)
        self.button8.place(x=330, y=1100, height=70, width=170)

        self.button9 = Button(self.root, relief=GROOVE, bd=2, bg="#00FFFF",
                              activebackground="#00FFFF", text="Link", font=("Open Sans", 30), cursor="hand2", command= self.link)
        self.button9.place(x=518, y=1100, height=70, width=170)

        self.button10 = Button(self.root, relief=GROOVE, bd=2, bg="#ff8c00",
                               activebackground="#ff8c00", text="T-Offer", font=("Open Sans", 30), cursor="hand2",command=self.Toffer)
        self.button10.place(x=702, y=1100, height=70, width=170)

        self.button11 = Button(self.root, relief=GROOVE, bd=2, bg="yellow",
                               activebackground="yellow", text="Coupon", font=("Open Sans", 30), cursor="hand2", command= self.Coupon)
        self.button11.place(x=890, y=1100, height=70, width=170)

        # =============================== Row 9 =======================================
        # =============================== Row 9 =======================================
        # =============================== Row 9 =======================================
        # =============================== Row 9 =======================================

        self.button7_s = Button(self.root, relief=GROOVE,bd=2,state=DISABLED, bg="#000000",cursor="hand2")
        self.button7_s.place(x=142, y=1195, height=70, width=170)

        self.button8_s = Button(self.root, relief=GROOVE, bd=2,state=DISABLED, bg="#000000",cursor="hand2")
        self.button8_s.place(x=330, y=1195, height=70, width=170)

        self.button9_s = Button(self.root, relief=GROOVE, bd=2, state=DISABLED, bg="#000000",cursor="hand2")
        self.button9_s.place(x=518, y=1195, height=70, width=170)

        self.button10_s = Button(self.root, relief=GROOVE, bd=2,state=DISABLED,bg="#000000",cursor="hand2")
        self.button10_s.place(x=702, y=1195, height=70, width=170)

        self.button11_s = Button(self.root, relief=GROOVE, bd=2,state=DISABLED, bg="#000000",cursor="hand2")
        self.button11_s.place(x=890, y=1195, height=70, width=170)

        # =============================== Row 10 =======================================
        # =============================== Row 10 =======================================
        # =============================== Row 10 =======================================
        # =============================== Row 10 =======================================

        self.Text = Frame(self.root, bd=2, relief=SUNKEN, bg=defaultbg)
        self.Text.place(x=200, y=1310, width=810, height=235)

        self.Text1 = Text(self.Text, bd=0, relief=SUNKEN,font=40, bg=defaultbg)
        self.Text1.place(x=0, y=0)

        self.Text1.insert(INSERT,("Date\t\t\t\t\t\t\t\t                                               Time\n10-07-2020\t\t\t\t\t\t\t\t\t                      23:05:23\nHi! Whats Up.? How R u?"))
        self.Text1.place(x=0,y=0,width=870,height=230)
        self.Text1.configure(state="disabled")

        # =============================== Row 11 =======================================
        # =============================== Row 11 =======================================
        # =============================== Row 11 =======================================
        # =============================== Row 11 =======================================

        self.button12 = Button(self.root, relief=GROOVE, bd=2, bg="yellow",
                               activebackground="yellow", text="Back", font=("Open Sans", 50), cursor="hand2", command=self.back)
        self.button12.place(x=480, y=1590, height=100, width=255)




# ======================================= Functions =====================================
# ======================================= Functions =====================================
# ======================================= Functions =====================================
# ======================================= Functions =====================================
        
    def back(self):
        self.root.destroy()
        root = Tk()
        win2(root)
        root.mainloop()

# ============================= For Post Code and Edit Row-1 ===================================
# ============================= For Post Code and Edit Row-1 ===================================
# ============================= For Post Code and Edit Row-1 ===================================
# ============================= For Post Code and Edit Row-1 ===================================

    def postcode(self):
        self.root2 = Toplevel(root)  # Child Window "Tk() can Also be use here"
        self.root2.title("UK Postcode")
        self.root2.geometry("750x250+350+150")
        self.root2.configure(bg="black")
        self.root2.grab_set()
        self.root2.resizable(False, False)

        title_child = Label(self.root2, text="Postcode", bg="#152238", fg="white", compound=LEFT, font=(
            "Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)

        postcode_lbl = Label(self.root2, text="Postcode", font=(
            "time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
        self.postcode_ = Entry(self.root2, bd=5, width=30,
                               bg="lightgrey", font=("times new roman", 18))
        self.postcode_.place(x=260, y=120)

        Save_btn = Button(self.root2, text="Save", font=("times new roman", 30, "bold"), activebackground="blue",
                          activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.save)
        Save_btn.place(x=275, y=200, width=170, height=35)

        Refuse_btn = Button(self.root2, text="Refuse", font=("times new roman", 30, "bold"), activebackground="darkgrey",
                            activeforeground="white", bg="darkgrey", fg="white", cursor="hand2", command=self.refuse)
        Refuse_btn.place(x=465, y=200, width=170, height=35)

    def refuse(self):
        self.lbl1 = Button(self.root, relief=GROOVE, bd=3, text="Postcode", font=(
            "Open Sans", 20), fg="#FFFFFF", activeforeground="#FFFFFF", bg="#FF1493", image=self.Icon2, compound=RIGHT)
        self.lbl1.place(x=660, y=158, height=55, width=230)
        self.root2.destroy()

    def save(self):
        self.post = self.postcode_.get()
        if self.post == "":
            return messagebox.showerror("Error", "Post code Feild required to save")
        else:
            self.lbl1 = Label(self.root, relief=GROOVE, bd=3, text=self.post, font=(
                "Open Sans", 20), fg="#FFFFFF", activeforeground="#FFFFFF", bg="#FF1493")
            self.lbl1.place(x=660, y=158, height=55, width=230)
            self.root2.destroy()

    def edit(self):
        self.Entry1.config(state=NORMAL)
        self.postcode()

# ============================= For M and F, and ages Row-3 ===================================
# ============================= For M and F, and ages Row-3 ===================================
# ============================= For M and F, and ages Row-3 ===================================
# ============================= For M and F, and ages Row-3 ===================================

    def MandF(self):
        if self.val.get() == "M":
            R1 = Radiobutton(self.root, bd=2, font=("times new roman", 15, "bold"), relief=GROOVE, text="M",
                             bg="#FFFF33", activebackground="#FFFF33", value="M", variable=self.val, cursor="hand2", command=self.MandF)
            R1.place(x=485, y=340, height=55)

            R2 = Radiobutton(self.root, bd=2, font=("times new roman", 15, "bold"), relief=GROOVE, text="F",
                             activebackground="#FFFF33", bg="#FFFFFF", variable=self.val, value="F", cursor="hand2", command=self.MandF)
            R2.place(x=540, y=340, height=55, width=50)
        else:
            R1 = Radiobutton(self.root, bd=2, font=("times new roman", 15, "bold"), relief=GROOVE, text="M",
                             bg="#FFFFFF", activebackground="#FFFF33", value="M", variable=self.val, cursor="hand2", command=self.MandF)
            R1.place(x=485, y=340, height=55)

            R2 = Radiobutton(self.root, bd=2, font=("times new roman", 15, "bold"), relief=GROOVE, text="F",
                             activebackground="#FFFF33", bg="#FFFF33", variable=self.val, value="F", cursor="hand2", command=self.MandF)
            R2.place(x=540, y=340, height=55, width=50)

    def ages(self):
        if self.val2.get() == "5-25":

            R3 = Radiobutton(self.root, bd=2, font=("times new roman", 25, "bold"), relief=GROOVE,
                             text="5-25", bg="#FFFF33", value="5-25", variable=self.val2, cursor="hand2", command=self.ages)
            R3.place(x=610, y=340, height=55, width=140)

            R4 = Radiobutton(self.root, bd=2, font=("times new roman", 25, "bold"), relief=GROOVE, text="26-40",
                             bg="blue", fg="#FFFFFF", value="26-45", variable=self.val2, cursor="hand2", command=self.ages)
            R4.place(x=765, y=340, height=55, width=140)

            R5 = Radiobutton(self.root, bd=2, font=("times new roman", 25, "bold"), relief=GROOVE, text="41-99",
                         bg="blue", fg="#FFFFFF", value="41-99", variable=self.val2, cursor="hand2", command=self.ages)
            R5.place(x=920, y=340, height=55, width=140)

        elif self.val2.get() == "26-45":

            R3 = Radiobutton(self.root, bd=2, font=("times new roman", 25, "bold"), relief=GROOVE, text="5-25",
                             bg="blue", fg="#FFFFFF", value="5-25", variable=self.val2, cursor="hand2", command=self.ages)
            R3.place(x=610, y=340, height=55, width=140)

            R4 = Radiobutton(self.root, bd=2, font=("times new roman", 25, "bold"), relief=GROOVE,
                             text="26-40", bg="#FFFF33", value="26-45", variable=self.val2, cursor="hand2", command=self.ages)
            R4.place(x=765, y=340, height=55, width=140)

            R5 = Radiobutton(self.root, bd=2, font=("times new roman", 25, "bold"), relief=GROOVE, text="41-99",
                         bg="blue", fg="#FFFFFF", value="41-99", variable=self.val2, cursor="hand2", command=self.ages)
            R5.place(x=920, y=340, height=55, width=140)

        else:
            R3 = Radiobutton(self.root, bd=2, font=("times new roman", 25, "bold"), relief=GROOVE, text="5-25",
                             bg="blue", fg="#FFFFFF", value="5-25", variable=self.val2, cursor="hand2", command=self.ages)
            R3.place(x=610, y=340, height=55, width=140)

            R4 = Radiobutton(self.root, bd=2, font=("times new roman", 25, "bold"), relief=GROOVE, text="26-40",
                         bg="blue", fg="#FFFFFF", value="26-45", variable=self.val2, cursor="hand2", command=self.ages)
            R4.place(x=765, y=340, height=55, width=140)

            R5 = Radiobutton(self.root, bd=2, font=("times new roman", 25, "bold"), relief=GROOVE,
                             text="41-99", bg="#FFFF33", value="41-99", variable=self.val2, cursor="hand2", command=self.ages)
            R5.place(x=920, y=340, height=55, width=140)

            global cond
            cond = self.cond
# ===================== Label & condition ==============================            
# ===================== Label & condition ==============================            
# ===================== Label & condition ==============================            
# ===================== Label & condition ==============================            
    
    def colorchoose(self): # color chooser dailogue box
        self.color = colorchooser.askcolor()[1] 
        print(self.color) 
        self.lbl6.config(fg=str(self.color))

    def condition(self,cond):
        self.lbl6.config(text=cond)


# ============================ LINK ==============================
# ============================ LINK ==============================
# ============================ LINK ==============================
# ============================ LINK ==============================
    
    def link(self):
        self.lbl5.config(state="normal")
        if self.lbl5.get() == "New Customer":
            try:
                self.EE=str(self.Entry1.get()).split(": ")[1]
                self.conn=sqlite3.connect("Customer.db")
                self.c=self.conn.cursor()
                self.data = ("SELECT CID FROM Customer1")
                self.c.execute(str(self.data))
                results = (self.c).fetchall()
                if results:
                    a=0
                    for i in results:
                        b= i[a]
                    
                        if str(b) == str(self.EE):
                            self.valuer=int(self.EE)
                            self.valuer += 1
                            print(self.valuer)
                            a+=1
                else:
                    self.valuer = 1

                self.Entry1.config(state=NORMAL)
                self.Entry1 = Entry(self.root, bg=defaultbg,bd=2, font=("Open Sans", 60))
                self.Entry1.place(x=110, y=230, width=265)
                self.Entry1.insert(0, "ID: "+str(self.valuer))
                self.Entry1.config(state=DISABLED)
                self.lbl5.config(state="disable")
                

            except Exception:
                return messagebox.showerror("Error","Something Wrong")
        else:
            pass

        self.root3 = Toplevel(root)  # Child Window "Tk() can Also be use here"
        self.root3.title("UK Postcode")
        self.root3.geometry("350x350+1700+150")
        self.root3.grab_set()
        self.root3.resizable(False, False)

        btn1 = Button(self.root3, font=("times new roman", 25, "bold"),bg="#DE1738",fg="white",text="QR CODE Scanner",command=self.Qrcoder)
        btn1.place(x=20, y=70)

        btn2 = Button(self.root3, font=("times new roman", 25, "bold"),bg="lightgreen",fg="white",text="Code Writer",command=self.Text_writer)
        btn2.place(x=20, y=160, width=310)

    def Qrcoder(self): 
        now = datetime.now()
        self.Time2=now.strftime('%H:%M:%S')

        self.today2= now.strftime("%d-%b-%Y")
  
        try:
            font = cv2.FONT_HERSHEY_SIMPLEX
            self.cam= cv2.VideoCapture(0)
            while True:
                _, frame = self.cam.read()
                self.decodeObjects = pyzbar.decode(frame)
                for self.obj in self.decodeObjects:
                    print("Data",self.obj.data)
                    self.obj=str(self.obj.data)
                    cv2.putText(frame, "Scaning Done Data is:",(150,150), font, 1, (255,0,0),3)
                cv2.imshow("QRScanner"+"      "+"Press Escape Key to Stop" ,frame)
                key = cv2.waitKey(1)
                if key == 27:
                    break

                labelframe = Label(self.root3, text="Invoice no: "+str(self.obj), font=("times new roman", 15))  
                labelframe.place(x=10, y=250) 
                labelframe = Label(self.root3, text=str(self.Time2), font=("times new roman", 15))  
                labelframe.place(x=10, y=270) 
                labelframe = Label(self.root3, text=str(self.today2), font=("times new roman", 15))  
                labelframe.place(x=10, y=290) 

        except Exception:
            return messagebox.showerror("Cann't Open Qr Scanner Try \nagain!!!")
    
    def Text_writer(self):
        now = datetime.now()
        self.Time2=now.strftime('%H:%M:%S')

        self.today2= now.strftime("%d-%b-%Y")
  
        self.root4 = Toplevel(root)  # Child Window "Tk() can Also be use here"
        self.root4.title("Code Typer")
        self.root4.geometry("350x350+1700+150")
        self.root4.grab_set()
        self.root4.resizable(False, False)

        self.Et1 = Entry(self.root4, font=("times new roman", 10, "bold"))
        self.Et1.place(x=20, y=70)
        self.Et1.insert(0,"aaaa")
        
        self.Et2 = Entry(self.root4, font=("times new roman", 10, "bold"))
        self.Et2.place(x=200, y=70)
        self.Et2.insert(0,"1111")

        
        btn_sav2 = Button(self.root4, font=("times new roman", 20, "bold"),bg="lightgreen",fg="white",text="Save",command=self.save0)
        btn_sav2.place(x=20, y=160, width=310)

        btn_back2 = Button(self.root4, font=("times new roman", 20, "bold"),bg="blue",fg="white",text="Back",command=self.btn_back)
        btn_back2.place(x=20, y=220, width=310)
            
    
    def save0(self):
        self.a=self.Et1.get()
        self.b=self.Et2.get()
        if len(str(self.a))<4 or len(str(self.a))>4:
            return messagebox.showerror("Error","Alfa Values cann't greater than 4 or less than 4")

        if len(str(self.b))<4 or len(str(self.b))>4:
            return messagebox.showerror("Error","Numeric Values cann't greater than 4 or less than 4")

        else:
            self.c=self.Et1.get()
            self.d=self.Et2.get()
            self.root4.destroy()
            labelframe = Label(self.root3, text="Invoice no: "+str(self.c+self.b), font=("times new roman", 15))  
            labelframe.place(x=10, y=250) 
            labelframe = Label(self.root3, text=str(self.Time2), font=("times new roman", 15))  
            labelframe.place(x=10, y=270) 
            labelframe = Label(self.root3, text=str(self.today2), font=("times new roman", 15))  
            labelframe.place(x=10, y=290) 


    def btn_back(self):
        self.root4.destroy()

# ========================== T-Offer ===================================
# ========================== T-Offer ===================================
# ========================== T-Offer ===================================
# ========================== T-Offer ===================================


    def Toffer(self):
        self.root5 = Toplevel(root)  # Child Window "Tk() can Also be use here"
        self.root5.title("UK Postcode")
        self.root5.geometry("400x750+1700+150")
        self.root5.config(bg="#FFFFFF")
        self.root5.grab_set()
        self.root5.resizable(False, False)

        now = datetime.now()
        self.Time3=now.strftime('%H:%M:%S')

        self.today3= now.strftime("%d-%m-%Y")


        self.Save5 = Button(self.root5, bd=2,relief=GROOVE,font=("times new roman", 25),bg="red",fg="white",text="Save",command=self.Qrcoder)
        self.Save5.place(x=200, y=570, height=30, width=120)

        self.cancel = Button(self.root5, bd=2,relief=GROOVE,font=("times new roman", 25,),bg="white",text="Cancel",command=self.cancel)
        self.cancel.place(x=60, y=570, height=30, width=120)

                 
        Table_Frame=Frame(self.root5,bd=0, relief=FLAT, bg="#FFFFFF")
        Table_Frame.place(x=5,y=100,width=390,height=450)
        style=ttk.Style(Table_Frame)
        #style.theme_use("calm")
        style.configure("Treeview",font=60)

        self.Offer_table=ttk.Treeview(Table_Frame,columns=("T_Offer"))
        #self.Offer_table.config(font=30)
        self.Offer_table.heading("T_Offer", text="T-Offer")
        self.Offer_table.column("T_Offer", width=50)
     
        self.Offer_table['show']='headings'
        self.Offer_table.bind("<ButtonRelease-1>",self.getcursor)
        self.fetch_data()
        self.search()


    def search(self):
        self.Offer_table.pack(fill=BOTH,expand=1)
        self.Offer_table.bind("<ButtonRelease-1>",self.getcursor)
        self.fetch_data()

    def fetch_data(self):
        self.conn=sqlite3.connect("Customer.db")
        self.c=self.conn.cursor()
        self.c.execute("select * from Offer_Cupons")
        rows=self.c.fetchall()
        if len(rows)!=0:
                self.Offer_table.delete(*self.Offer_table.get_children())
                for row in rows:
                        self.Offer_table.insert('',END,values=row)
                self.conn.commit()
        self.conn.close()

    def getcursor(self,ev):
        cursor_row=self.Offer_table.focus()
        Content=self.Offer_table.item(cursor_row)
        row=Content['values']
        #print(row)
       # a = row[0]
       # self.Std_ID.set(a)
       
        self.lblt = Label(self.root5, bd=0,relief=GROOVE,text=str(row[0]),font=("times new roman", 30),bg="yellow")
        self.lblt.place(x=0, y=0,height=100)
        self.lblt1 = Label(self.root5, bd=0,relief=GROOVE,text="\n\n\n\n "+str(self.Time3)+"/"+str(self.today3),font=("times new roman", 13),bg="yellow")
        self.lblt1.place(x=223, y=0,height=100,width=170)
        
    def cancel(self):
        self.root5.destroy()

# ========================== Coupon ===================================
# ========================== Coupon ===================================
# ========================== Coupon ===================================
# ========================== Coupon ===================================

    def Coupon(self):    
        self.root6 = Toplevel(root)  # Child Window "Tk() can Also be use here"
        self.root6.title("UK Postcode")
        self.root6.geometry("350x350+1700+150")
        self.root6.grab_set()
        self.root6.resizable(False, False)

        btn1 = Button(self.root6, font=("times new roman", 25, "bold"),bg="#DE1738",fg="white",text="QR CODE Scanner",command=self.Qrcoder1)
        btn1.place(x=20, y=70)

        btn2 = Button(self.root6, font=("times new roman", 25, "bold"),bg="lightgreen",fg="white",text="Code Writer",command=self.Text_writer1)
        btn2.place(x=20, y=160, width=310)


    def Qrcoder1(self):
        now = datetime.now()
        self.Time2=now.strftime('%H:%M:%S')

        self.today2= now.strftime("%d-%b-%Y")
  
        try:
            font = cv2.FONT_HERSHEY_SIMPLEX
            self.cam1= cv2.VideoCapture(0)
            while True:
                _, frame = self.cam1.read()
                self.decodeObjects1 = pyzbar.decode(frame)
                for self.obj1 in self.decodeObjects1:
                    print("Data",self.obj1.data)
                    self.obj1=str(self.obj1.data)
                    cv2.putText(frame, "Scaning Done Data is:",(150,150), font, 1, (255,0,0),3)
                cv2.imshow("QRScanner"+"      "+"Press Escape Key to Stop" ,frame)
                key = cv2.waitKey(1)
                if key == 27:
                    break
                labelframe = Label(self.root6, text="Invoice no: "+str(self.obj), font=("times new roman", 15))  
                labelframe.place(x=10, y=250) 
                labelframe = Label(self.root6, text=str(self.Time2), font=("times new roman", 15))  
                labelframe.place(x=10, y=270) 
                labelframe = Label(self.root6, text=str(self.today2), font=("times new roman", 15))  
                labelframe.place(x=10, y=290) 

        except Exception:
            return messagebox.showerror("Cann't Open Qr Scanner Try \nagain!!!")
    
    def Text_writer1(self):
        self.root7 = Toplevel(root)  # Child Window "Tk() can Also be use here"
        self.root7.title("Code Typer")
        self.root7.geometry("350x350+1700+150")
        self.root7.grab_set()
        self.root7.resizable(False, False)

        self.Et1 = Entry(self.root7, font=("times new roman", 10, "bold"))
        self.Et1.place(x=20, y=70)
        self.Et1.insert(0,"aaaa")
        
        self.Et2 = Entry(self.root7, font=("times new roman", 10, "bold"))
        self.Et2.place(x=200, y=70)
        self.Et2.insert(0,"1111")

        btn_sav2 = Button(self.root7, font=("times new roman", 20, "bold"),bg="lightgreen",fg="white",text="Save",command=self.save1)
        btn_sav2.place(x=20, y=160, width=310)

        btn_back2 = Button(self.root7, font=("times new roman", 20, "bold"),bg="blue",fg="white",text="Back",command=self.btn_back1)
        btn_back2.place(x=20, y=220, width=310)
            

    def save1(self):
        now = datetime.now()
        self.Time2=now.strftime('%H:%M:%S')

        self.today2= now.strftime("%d-%b-%Y")
  
        self.a=self.Et1.get()
        self.b=self.Et2.get()
        if len(str(self.a))<4 or len(str(self.a))>4:
            return messagebox.showerror("Error","Alfa Values cann't greater than 4 or less than 4")

        if len(str(self.b))<4 or len(str(self.b))>4:
            return messagebox.showerror("Error","Numeric Values cann't greater than 4 or less than 4")

        else:
            self.c=self.Et1.get()
            self.d=self.Et2.get()
            self.root7.destroy()
            labelframe = Label(self.root6, text="Invoice no: "+str(self.c+self.b), font=("times new roman", 15))  
            labelframe.place(x=10, y=250) 
            labelframe = Label(self.root6, text=str(self.Time2), font=("times new roman", 15))  
            labelframe.place(x=10, y=270) 
            labelframe = Label(self.root6, text=str(self.today2), font=("times new roman", 15))  
            labelframe.place(x=10, y=290) 


    def btn_back1(self):
        self.root6.destroy()

# ===================== SURVEY ==============================            
# ===================== SURVEY ==============================            
# ===================== SURVEY ==============================            
# ===================== SURVEY ==============================            

    def survey(self):
        self.root8 = Toplevel()  # Child Window "Tk() can Also be use here"
        self.root8.title("Survey")
        self.root8.geometry("700x700+1600+150")
        self.root8.configure(bg="black")
        self.root8.focus_force()  # Fouce on Child Window
        self.root8.grab_set()  # Hold the Child window till closinf of the window
        self.root8.resizable(False, False)
        # =====================================Child Window Title=================================
        # =====================================Child Window Title=================================
        # =====================================Child Window Title=================================
        # =====================================Child Window Title=================================

        title_child = Label(self.root8, text="SURVEY", bg="#152238", fg="white", font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
        sub_title_child = Label(self.root8, text="Answer some question for survey",bg="yellow", font=("Calibri (Body)", 14, "bold"), anchor="w").place(x=0, y=95, relwidth=1)

        # ====================Child Window Entries=======================================
        # ====================Child Window Entries=======================================
        # ====================Child Window Entries=======================================
        # ====================Child Window Entries=======================================

        Ques1_lbl = Label(self.root8, text="Q.1 How is our survice?", font=(
            "time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=150)

        Ans2_lbl = Label(self.root8, text="A.1", font=(
            "time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=200)

        Ques2_lbl = Label(self.root8, text="Q.2 Would you like to visit again?", font=(
            "time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=250)

        Ans2_lbl = Label(self.root8, text="A.2", font=(
            "time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=300)

        Ques3_lbl = Label(self.root8, text="Q.3 How is our products?", font=(
            "time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=350)

        Ans3_lbl = Label(self.root8, text="A.3", font=(
            "time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=400)

        Ques4_lbl = Label(self.root8, text="Q.4 What do you like most about the store?", font=(
            "time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=450)

        Ans4_lbl = Label(self.root8, text="A.4", font=(
            "time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=500)

        Ques5_lbl = Label(self.root8, text="Q.5 What would you like to suggest for change in store?", font=(
            "time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=550)

        Ans5_lbl = Label(self.root8, text="A.5", font=(
            "time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=600)

        self.Ans1_entry = Entry(self.root8, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.Ans1_entry.place(x=230, y=200)

        self.Ans2_entry = Entry(self.root8, bd=5, width=30,  bg="lightgrey", font=("times new roman", 18))
        self.Ans2_entry.place(x=230, y=300)

        self.Ans3_entry = Entry(self.root8, bd=5, width=30,  bg="lightgrey", font=("times new roman", 18))
        self.Ans3_entry.place(x=230, y=400)

        self.Ans4_entry = Entry(self.root8, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.Ans4_entry.place(x=230, y=500)

        self.Ans5_entry = Entry(self.root8, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.Ans5_entry.place(x=230, y=600)


        # ===========================Child Window Buttons===================================
        # ===========================Child Window Buttons===================================
        # ===========================Child Window Buttons===================================
        # ===========================Child Window Buttons===================================

        clear_btn = Button(self.root8, text="Clear", font=("times new roman", 18, "bold"), activebackground="#262626",
                           activeforeground="white", bg="#262626", fg="white", cursor="hand2", command=self.clear).place(x=300, y=650, width=140, height=30)

        save_btn = Button(self.root8, text="Save", font=("times new roman", 18, "bold"), activebackground="#00B0F0",
                          activeforeground="white", bg="#00B0F0", fg="white", cursor="hand2", command=self.save2).place(x=465, y=650, width=140, height=30)

    def clear(self):
        self.Ans1_entry.delete(0,END)
        self.Ans2_entry.delete(0,END)
        self.Ans3_entry.delete(0,END)
        self.Ans4_entry.delete(0,END)
        self.Ans5_entry.delete(0,END)
    
    def save2(self):
        self.A1 = str(self.Ans1_entry.get())
        self.A2 = str(self.Ans2_entry.get())
        self.A3 = str(self.Ans3_entry.get())
        self.A4 = str(self.Ans4_entry.get())
        self.A5 = str(self.Ans5_entry.get())
        messagebox.showinfo("Saved","Survey Saved")
    
# ========================= Left Building ==========================
# ========================= Left Building ==========================
# ========================= Left Building ==========================
# ========================= Left Building ==========================

    def leftbldg(self):
        try:
            temp = self.valuer
            int(temp)
        except ValueError:
            return messagebox.showinfo('Error','Generate CID by Clicking')
            
        now = datetime.now()
        self.Exit_Time=now.strftime('%H:%M:%S')
        self.Exit_today= now.strftime("%d-%b-%Y")
        self.lbl5.config(state="normal")
        self.CoT=self.lbl5.get()
        self.lbl5.config(state="disable") 
        if self.CoT == "New Customer":
            if self.Entry2.get() == "Enter name if known":
                self.Entry2 = "None"
            else:
                self.EntryE3 = self.Entry2.get()  
            
            try:
                self.conn=sqlite3.connect("Customer.db")
                self.c=self.conn.cursor()
                self.c.execute("CREATE TABLE IF NOT EXISTS Customer1(CID TEXT PRIMARY KEY, Name TEXT, C_Type TEXT, C_Color TEXT, Gender TEXT, Age_B TEXT, Condition TEXT)")
                self.c.execute("INSERT INTO Customer1(CID, Name, C_Type, C_Color, Gender, Age_B, Condition) VALUES (?,?,?,?,?,?,?)",(str(self.valuer),str(self.EntryE3),str("Old Customer"),str(self.color),str(self.val),str(self.val2),str(self.cond)))
                self.c.execute("INSERT INTO Cust_TimeStamps(CID , Time_Entry , Time_Exit, Date) VALUES (?,?,?,?)",(str(self.valuer),str(self.Ent_Time),str(self.Exit_Time),str(self.Exit_today)))
                
                self.conn.commit()
                self.c.close()
                self.conn.close()
                return messagebox.showinfo("Successfull","Successfully Added Data")
            except Exception:
                return messagebox.showerror("Error!!","Somthing went wrong not able to add data try again ")
                        #messagebox.showinfo("Error!!", "May be your Roll No. already exist. Please Check")        
        else:
            pass

# ========================= DELETE ==========================
# ========================= DELETE ==========================
# ========================= DELETE ==========================
# ========================= DELETE ==========================

    def delete(self):
        pass


class win2:
    def __init__(self, root):

        self.root=root
        self.root.geometry("1200x1920+1370+0")
        self.root.title("Customers".center(160))

        #=================== Icons ===============================

        self.Icon1 = ImageTk.PhotoImage(file="Pics\\2.jpg")

        #================== Main Frame =========================
        #================== Main Frame =========================

        self.FrameM=Frame(self.root, bd=0,bg="#DCDCDC") 
        self.FrameM.place(x=100,y=120, height=1600,width=1000)
            
        #================== Top Frame =========================
        #================== Top Frame =========================
        
        self.FrameT=Frame(self.FrameM, bg="#FFFFFF") 
        self.FrameT.place(x=0,y=0, height=39,relwidth=1)
        
        #=================== Row 1 =============================
        #=================== Row 1 =============================
        #=================== Row 1 =============================
        #=================== Row 1 =============================
        
        now = datetime.now()
        self.today= now.strftime("%d-%m-%Y")
        
        self.date =  Label(self.FrameM,text=str(self.today) , font = ("Open Sans", 20),bg="#FFFFFF")
        self.date.place(x=530, y=0)
        
        self.lbl_hr = Label(self.FrameM,text="12" , font = ("Open Sans", 20),bg="#FFFFFF")
        self.lbl_hr.place(x=700, y=0)
        
        self.lbl_COLON = Label(self.FrameM,text=":" , font = ("Open Sans", 20),bg="#FFFFFF")
        self.lbl_COLON.place(x=732, y=0)
              
        self.lbl_min = Label(self.FrameM,text="12" , font = ("Open Sans", 20),bg="#FFFFFF")
        self.lbl_min.place(x=740, y=0)
       
        self.lbl_COLON = Label(self.FrameM,text=":" , font = ("Open Sans", 20),bg="#FFFFFF")
        self.lbl_COLON.place(x=772, y=0)
       
        self.button1 = Button(self.FrameM, relief=FLAT, bd=0, text="Logout", bg="#FFFFFF", font=("Open Sans", 20), activebackground="#FFFFFF", cursor="hand2")
        self.button1.place(x=830, y=0, height=38, width=140)

        #=================== Row 2 =============================
        #=================== Row 2 =============================
        #=================== Row 2 =============================
        #=================== Row 2 =============================


        self.button2 = Button(self.FrameM, relief=GROOVE, bd=3, text="Today's Customers", bg="#FFFFFF", font=("Open Sans", 20,"bold"), activebackground="#FFFFFF", cursor="hand2", command=self.bbtemp)
        self.button2.place(x=30, y=55, height=43, width=300)


        #=================== Row 3 =============================
        #=================== Row 3 =============================
        #=================== Row 3 =============================
        #=================== Row 3 =============================


        self.headlbl = Label(self.FrameM, text="Customers In Shop", bg="#DCDCDC", font=("Open Sans", 53))
        self.headlbl.place(x=25, y=110)

        #=================== Row Frames =======================
        #=================== Row Frames =======================
        #=================== Row Frames =======================
        #=================== Row Frames =======================

        
        #====================== Row 1 ============================
        a=22
        b=198
        for i in range(1,7):
            self.Frame1=Frame(self.FrameM, bd=2,relief=GROOVE, bg="#DCDCDC") 
            self.Frame1.place(x=a,y=b, height=138,width=138)
            
      
            for i in range(1,8):
                self.Frame1=Frame(self.FrameM, bd=2,relief=GROOVE, bg="#DCDCDC") 
                self.Frame1.place(x=a,y=b, height=138,width=138)
                b+=155 
            b=198
            a+=164             
        
        self.clock()


    def bbtemp(self):
        self.root.destroy()
        root = Tk()
        obj = win1(root)
        root.mainloop()

    def clock(self):
        self.h = str(time.strftime("%H"))
        self.m = str(time.strftime("%M"))
         
        self.lbl_hr.config(text = self.h)
        self.lbl_min.config(text = self.m)


root = Tk()
defaultbg = root.cget('bg')
obj = win1(root)
root.mainloop()
