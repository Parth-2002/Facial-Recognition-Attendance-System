from tkinter import *
from tkinter import ttk  # For modern-looking widgets
from PIL import Image, ImageTk  # For handling images

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Set window size
        self.root.title("Face Recognition Attendance System")  # Set window title

        # 🔹 **1. Header Images (Top 3 Images)**
        img1 = Image.open(r"C:\Users\rahulbhise\Documents\Facial-Recognition-Attendance-system\Images\Pic1.jpg")
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
        img_bg = Image.open(r"C:\Users\rahulbhise\Documents\Facial-Recognition-Attendance-system\Images\background.jpg")
        img_bg = img_bg.resize((1530, 710), Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        bg_lbl = Label(self.root, image=self.photoimg_bg)
        bg_lbl.place(x=0, y=130, width=1530, height=710)

        # 🔹 **3. Title Text**
        title_lbl = Label(bg_lbl, text="FACE RECOGNITION ATTENDANCE SYSTEM",
                          font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # --------------------------------------
        # 🔹 **4. Feature Buttons**
        # --------------------------------------

        # 🟢 **Student Details**
        img4 = Image.open(r"C:\Users\rahulbhise\Documents\Facial-Recognition-Attendance-system\Images\student.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_lbl, image=self.photoimg4, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)
        b1_1 = Button(bg_lbl, text="Student Details", font=("times new roman", 15, "bold"),
                      bg="blue", fg="white", cursor="hand2")
        b1_1.place(x=200, y=330, width=220, height=40)

        # 🟢 **Face Detector**
        img5 = Image.open(r"C:\Users\rahulbhise\Documents\Facial-Recognition-Attendance-system\Images\detector.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b2 = Button(bg_lbl, image=self.photoimg5, cursor="hand2")
        b2.place(x=500, y=100, width=220, height=220)
        b2_1 = Button(bg_lbl, text="Face Detector", font=("times new roman", 15, "bold"),
                      bg="blue", fg="white", cursor="hand2")
        b2_1.place(x=500, y=330, width=220, height=40)

        # 🟢 **Attendance**
        img6 = Image.open(r"C:\Users\rahulbhise\Documents\Facial-Recognition-Attendance-system\Images\attendance.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b3 = Button(bg_lbl, image=self.photoimg6, cursor="hand2")
        b3.place(x=800, y=100, width=220, height=220)
        b3_1 = Button(bg_lbl, text="Attendance", font=("times new roman", 15, "bold"),
                      bg="blue", fg="white", cursor="hand2")
        b3_1.place(x=800, y=330, width=220, height=40)
         
        # 🟢 **Help**
        img7 = Image.open(r"C:\Users\rahulbhise\Documents\Facial-Recognition-Attendance-system\Images\help.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b4 = Button(bg_lbl, image=self.photoimg7, cursor="hand2")
        b4.place(x=1100, y=100, width=220, height=220)
        b4_1 = Button(bg_lbl, text="Help Desk", font=("times new roman", 15, "bold"),
                      bg="blue", fg="white", cursor="hand2")
        b4_1.place(x=1100, y=330, width=220, height=40)

        # 🟢 **Training**
        img8 = Image.open(r"C:\Users\rahulbhise\Documents\Facial-Recognition-Attendance-system\Images\traindata.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b5 = Button(bg_lbl, image=self.photoimg8, cursor="hand2")
        b5.place(x=200, y=380, width=220, height=220)
        b5_1 = Button(bg_lbl, text="Train Data", font=("times new roman", 15, "bold"),bg="blue", fg="white", cursor="hand2")
        b5_1.place(x=200, y=600, width=220, height=40)

        # 🟢 **Photos**
        img9 = Image.open(r"C:\Users\rahulbhise\Documents\Facial-Recognition-Attendance-system\Images\photoimage.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b6 = Button(bg_lbl, image=self.photoimg9, cursor="hand2")
        b6.place(x=500, y=380, width=220, height=220)
        b6_1 = Button(bg_lbl, text="Photos", font=("times new roman", 15, "bold"),bg="blue", fg="white", cursor="hand2")
        b6_1.place(x=500, y=600, width=220, height=40)

        # 🟢 **Developer**
        img10 = Image.open(r"C:\Users\rahulbhise\Documents\Facial-Recognition-Attendance-system\Images\developer.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b7 = Button(bg_lbl, image=self.photoimg10, cursor="hand2")
        b7.place(x=800, y=380, width=220, height=220)
        b7_1 = Button(bg_lbl, text="Developer", font=("times new roman", 15, "bold"),bg="blue", fg="white", cursor="hand2")
        b7_1.place(x=800, y=600, width=220, height=40)

        # 🟢 **Exit**
        img11 = Image.open(r"C:\Users\rahulbhise\Documents\Facial-Recognition-Attendance-system\Images\exit.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b8 = Button(bg_lbl, image=self.photoimg11, cursor="hand2")
        b8.place(x=1100, y=380, width=220, height=220)
        b8_1 = Button(bg_lbl, text="Exit", font=("times new roman", 15, "bold"),bg="blue", fg="white", cursor="hand2")
        b8_1.place(x=1100, y=600, width=220, height=40)

# Main Execution
if __name__ == "__main__":
    root = Tk()  # Create Tkinter root window
    obj = Face_Recognition_System(root)  # Create object of class
    root.mainloop()  # Start main event loop