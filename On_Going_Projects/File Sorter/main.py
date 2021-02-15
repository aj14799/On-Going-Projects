# ============ Importing Packages ============
# ============ Importing Packages ============

from tkinter import* 
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

# ===================== Main Class ===================
# ===================== Main Class ===================
# ===================== Main Class ===================
# ===================== Main Class ===================

class win1:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x768+0+0")
        self.root.title("File Sorting Application``".center(420))
        self.root.config(bg="#FFF")
        self.root.resizable(False,False)
        
        title = Label(self.root, text="File Sorting Application", font = ("times new roman",40,"bold"),fg="#FFFFFF", bg ="#023545").pack(fill=X)
        
        # =========== Row1 ==================
        # =========== Row1 ==================
        # =========== Row1 ==================
        # =========== Row1 ==================
        
        lbl1 = Label(self.root, text="Select Folder", font = ("times new roman",25), bg ="#FFF")
        lbl1.place(x=50, y=95)

        self.ent1 = Entry(self.root, bd=3,relief=SUNKEN,font = ("times new roman",25), bg ="lightgrey")
        self.ent1.place(x=250, y=90, width=700)

        self.Button1 = Button(self.root, bd=5,relief=RAISED,text = "BROWSE",font = ("times new roman",25, "bold"),fg ="#FFF", bg ="#404040",activeforeground ="#FFF", activebackground ="#404040")
        self.Button1.place(x=1000, y=90, height=45)
            
        self.separator1 = ttk.Separator(self.root, orient=HORIZONTAL)
        self.separator1.place(x=50, y= 160, width=1220)

        # =========== Row2 ==================
        # =========== Row2 ==================
        # =========== Row2 ==================
        # =========== Row2 ==================

        lbl2 = Label(self.root, text="Various Extention Supports", font = ("times new roman",25), bg ="#FFF")
        lbl2.place(x=50, y=170)

        

        
        
root = Tk()
obj = win1(root)
root.mainloop()
        




