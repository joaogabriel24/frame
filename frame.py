from tkinter import *
from tkinter import ttk

class MainApp(Tk):
    def __init__(self):
        super().__init__()
        self.font = ("Arial",30)

        self.geometry("900x400")
        self.title("meu app")
        self.create_frames()
        self.create_buttons()
        self.create_labels()

        self.mainloop()

    def create_frames(self):
        self.left_frame = Frame(self,bg="blue",width=150)
        self.left_frame.pack(side=LEFT,fill=Y)
        self.right_frame = Frame(self,bg="red",width=250)
        self.right_frame.pack(side=RIGHT,fill=Y)

    def create_buttons(self):
        self.button1 = Button(self.left_frame,text="Button 1",font=self.font)
        self.button1.pack(pady=20)
        self.button2 = Button(self.left_frame,text="Button 2",font=self.font)
        self.button2.pack(pady=20)     

    def create_labels(self):
        self.label1 = Label(self.right_frame,text="Label 1",font=self.font)
        self.label1.pack(pady=20)
        self.label2 = Label(self.right_frame,text="Label 2",font=self.font)
        self.label2.pack(pady=20)   
        
if __name__ == "__main__":    app = MainApp()   



