from tkinter import *
from tkinter import ttk  # For modern-looking widgets
from PIL import Image, ImageTk  # For handling images
import os

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Set window size
        self.root.title("Face Recognition Attendance System")  # Set window title

        # Define the relative path to the Images directory
        base_path = "Images/"  # Relative path for macOS
        
        # Function to load images safely
        def load_image(filename, size):
            path = os.path.join(base_path, filename)
            if os.path.exists(path):
                img = Image.open(path).resize(size, Image.LANCZOS)
                return ImageTk.PhotoImage(img)
            else:
                print(f"❌ File NOT found: {path}")
                return None

        # 🔹 **1. Header Images (Top 3 Images)**
        self.photoimg1 = load_image("Pic1.jpg", (500, 130))
        f_lbl1 = Label(self.root, image=self.photoimg1) if self.photoimg1 else None
        if f_lbl1: f_lbl1.place(x=0, y=0, width=500, height=130)
        
        self.photoimg2 = load_image("pic2.webp", (500, 130))
        f_lbl2 = Label(self.root, image=self.photoimg2) if self.photoimg2 else None
        if f_lbl2: f_lbl2.place(x=510, y=0, width=500, height=130)
        
        self.photoimg3 = load_image("pic3.jpg", (500, 130))
        f_lbl3 = Label(self.root, image=self.photoimg3) if self.photoimg3 else None
        if f_lbl3: f_lbl3.place(x=1020, y=0, width=500, height=130)

        # 🔹 **2. Background Image**
        self.photoimg_bg = load_image("background.jpg", (1530, 710))
        bg_lbl = Label(self.root, image=self.photoimg_bg) if self.photoimg_bg else None
        if bg_lbl: bg_lbl.place(x=0, y=130, width=1530, height=710)

        # 🔹 **3. Title Text**
        title_lbl = Label(bg_lbl, text="FACE RECOGNITION ATTENDANCE SYSTEM",
                          font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # --------------------------------------
        # 🔹 **4. Feature Buttons**
        # --------------------------------------

        # 🟢 **Student Details**
        self.photoimg4 = load_image("student.jpg", (220, 220))
        b1 = Button(bg_lbl, image=self.photoimg4, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)
        b1_1 = Button(bg_lbl, text="Student Details", font=("times new roman", 15, "bold"),
                      bg="blue", fg="black", cursor="hand2")
        b1_1.place(x=200, y=330, width=220, height=40)

        # 🟢 **Face Detector**
        self.photoimg5 = load_image("detector.jpg", (220, 220))
        b2 = Button(bg_lbl, image=self.photoimg5, cursor="hand2")
        b2.place(x=500, y=100, width=220, height=220)
        b2_1 = Button(bg_lbl, text="Face Detector", font=("times new roman", 15, "bold"),
                      bg="blue", fg="black", cursor="hand2")
        b2_1.place(x=500, y=330, width=220, height=40)

        # 🟢 **Attendance**
        self.photoimg6 = load_image("attendance.jpg", (220, 220))
        b3 = Button(bg_lbl, image=self.photoimg6, cursor="hand2")
        b3.place(x=800, y=100, width=220, height=220)
        b3_1 = Button(bg_lbl, text="Attendance", font=("times new roman", 15, "bold"),
                      bg="blue", fg="black", cursor="hand2")
        b3_1.place(x=800, y=330, width=220, height=40)
         
        # 🟢 **Help**
        self.photoimg7 = load_image("help.jpg", (220, 220))
        b4 = Button(bg_lbl, image=self.photoimg7, cursor="hand2")
        b4.place(x=1100, y=100, width=220, height=220)
        b4_1 = Button(bg_lbl, text="Help Desk", font=("times new roman", 15, "bold"),
                      bg="blue", fg="black", cursor="hand2")
        b4_1.place(x=1100, y=330, width=220, height=40)

        # 🟢 **Training**
        self.photoimg8 = load_image("traindata.jpg", (220, 220))
        b5 = Button(bg_lbl, image=self.photoimg8, cursor="hand2")
        b5.place(x=200, y=380, width=220, height=220)
        b5_1 = Button(bg_lbl, text="Train Data", font=("times new roman", 15, "bold"),bg="blue", fg="black", cursor="hand2")
        b5_1.place(x=200, y=600, width=220, height=40)

        # 🟢 **Photos**
        self.photoimg9 = load_image("photoimage.jpg", (220, 220))
        b6 = Button(bg_lbl, image=self.photoimg9, cursor="hand2")
        b6.place(x=500, y=380, width=220, height=220)
        b6_1 = Button(bg_lbl, text="Photos", font=("times new roman", 15, "bold"),bg="blue", fg="black", cursor="hand2")
        b6_1.place(x=500, y=600, width=220, height=40)

        # 🟢 **Developer**
        self.photoimg10 = load_image("developer.jpg", (220, 220))
        b7 = Button(bg_lbl, image=self.photoimg10, cursor="hand2")
        b7.place(x=800, y=380, width=220, height=220)
        b7_1 = Button(bg_lbl, text="Developer", font=("times new roman", 15, "bold"),bg="blue", fg="black", cursor="hand2")
        b7_1.place(x=800, y=600, width=220, height=40)

        # 🟢 **Exit**
        self.photoimg11 = load_image("exit.jpg", (220, 220))
        b8 = Button(bg_lbl, image=self.photoimg11, cursor="hand2")
        b8.place(x=1100, y=380, width=220, height=220)
        b8_1 = Button(bg_lbl, text="Exit", font=("times new roman", 15, "bold"),bg="blue", fg="black", cursor="hand2")
        b8_1.place(x=1100, y=600, width=220, height=40)

# Main Execution
if __name__ == "__main__":
    root = Tk()  # Create Tkinter root window
    obj = Face_Recognition_System(root)  # Create object of class
    root.mainloop()  # Start main event loop
