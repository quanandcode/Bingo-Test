from tkinter import *
from PIL import ImageTk, Image
class Left_bar(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self = Frame(self, width=200, height=575,bg="red")
        #
        img1 = ImageTk.PhotoImage(Image.open("./images/your_turn.png").resize((200,100), Image.ANTIALIAS))
        your_turn = Canvas(self,width=200,height=100)
        your_turn.create_image(100,100,image=img1)
        your_turn.pack()
        #
        self.pack()
class Mid_bar(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        #Left bar
        self = Frame(self, width=500, height=575,bg="green")
        self.pack()
class Right_bar(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        #Left bar
        self = Frame(self, width=200, height=575,bg="blue")
        self.pack()
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("BINGO")
        self.geometry("1000x625")
        self.resizable(width=False, height=False)
        window = Frame()
        window.place(x=25,y=25)
        # 
        left_bar = Left_bar(window)
        left_bar.grid(row=0, column=0)
        #
        mid_bar = Mid_bar(window)
        mid_bar.grid(row=0,column=1,padx=25)
        #
        right_bar = Right_bar(window)
        right_bar.grid(row=0,column=2)
        #raise
        # left_bar.tkraise()
app = App()
app.mainloop()