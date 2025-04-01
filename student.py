from tkinter import *
from tkinter import ttk  # For modern-looking widgets
from PIL import Image, ImageTk  # For handling images

class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Set window size
        self.root.title("Face Recognition Attendance System")  # Set window title
        
 # 🔹 **1. Header Images (Top 3 Images)**
        img1 = Image.open(r"C:\Users\rahulbhise\Documents\Facial-Recognition-Attendance-system\Images\student.png")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=500, height=130)

        img2 = Image.open(r"C:\Users\rahulbhise\Documents\Facial-Recognition-Attendance-system\Images\Pic2.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=510, y=0, width=500, height=130)

        img3 = Image.open(r"C:\Users\rahulbhise\Documents\Facial-Recognition-Attendance-system\Images\Pic3.jpg")
        img3 = img3.resize((500, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=1020, y=0, width=500, height=130)

        # 🔹 **2. Background Image**
        img_bg = Image.open(r"C:\Users\rahulbhise\Documents\Student Management System\Images\background.jpg")
        img_bg = img_bg.resize((1530, 710), Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        bg_lbl = Label(self.root, image=self.photoimg_bg),bg_lbl = Label(self.root, bg="light sky blue")  
        bg_lbl.place(x=0, y=130, width=1530, height=710)
         
         #left label frame
        main_frame= Frame(bg_img,bd=2,relief=RIDGE,bg="white")
        main_frame.place(x=10,y=10,width=800,height=500)
       
        img_left = Image.open(r"C:\Users\rahulbhise\Documents\Facial-Recognition-Attendance-system\Images\student.jpeg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)#  resize the image
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl3 = Label(self.root, image=self.photoimg_left)
        f_lbl3.place(x=5, y=0, width=720, height=130)

          #current course label
        main_frame= Frame(bg_img,bd=2,relief=RIDGE,bg="white")
        main_frame.place(x=10,y=10,width=800,height=500)


                     











         #right label frame
        main_frame= Frame(bg_img,bd=2,relief=RIDGE,bg="white")
        main_frame.place(x=15,y=15,width=800,height=500)

         



































# Main Execution
if __name__ == "__main__":
    root = Tk()  # Create Tkinter root window
    obj = student(root)  # Create object of class
    root.mainloop()  # Start main event loop        