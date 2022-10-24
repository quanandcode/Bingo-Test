from tkinter import *
from PIL import ImageTk, Image
# orange: #fa991c
# light: #fbf3f2
# blue: #1c768f
# dark: #032539
value =0
def bind_all(nums):
    #00
    def value00(event):
        value = nums[0][0]['text']
        print(value)
        nums[0][0]['fg'] = "#123"
        nums[0][0]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[0][0].bind("<Button-1>",value00)
    #01
    def value01(event):
        value = nums[0][1]['text']
        print(value)
        nums[0][1]['fg'] = "#123"
        nums[0][1]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[0][1].bind("<Button-1>",value01)
    #02
    def value02(event):
        value = nums[0][2]['text']
        print(value)
        nums[0][2]['fg'] = "#123"
        nums[0][2]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[0][2].bind("<Button-1>",value02)
    #03
    def value03(event):
        value = nums[0][3]['text']
        print(value)
        nums[0][3]['fg'] = "#123"
        nums[0][3]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[0][3].bind("<Button-1>",value03)
    #04
    def value04(event):
        value = nums[0][4]['text']
        print(value)
        nums[0][4]['fg'] = "#123"
        nums[0][4]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[0][4].bind("<Button-1>",value04)
    #10
    def value10(event):
        value = nums[1][0]['text']
        print(value)
        nums[1][0]['fg'] = "#123"
        nums[1][0]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[1][0].bind("<Button-1>",value10)
    #11
    def value11(event):
        value = nums[1][1]['text']
        print(value)
        nums[1][1]['fg'] = "#123"
        nums[1][1]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[1][1].bind("<Button-1>",value11)
    #12
    def value12(event):
        value = nums[1][2]['text']
        print(value)
        nums[1][2]['fg'] = "#123"
        nums[1][2]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[1][2].bind("<Button-1>",value12)
    #13
    def value13(event):
        value = nums[1][3]['text']
        print(value)
        nums[1][3]['fg'] = "#123"
        nums[1][3]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[1][3].bind("<Button-1>",value13)
    #14
    def value14(event):
        value = nums[1][4]['text']
        print(value)
        nums[1][4]['fg'] = "#123"
        nums[1][4]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[1][4].bind("<Button-1>",value14)
    #20
    def value20(event):
        value = nums[2][0]['text']
        print(value)
        nums[2][0]['fg'] = "#123"
        nums[2][0]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[2][0].bind("<Button-1>",value20)
    #21
    def value21(event):
        value = nums[2][1]['text']
        print(value)
        nums[2][1]['fg'] = "#123"
        nums[2][1]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[2][1].bind("<Button-1>",value21)
    #22
    def value22(event):
        value = nums[2][2]['text']
        print(value)
        nums[2][2]['fg'] = "#123"
        nums[2][2]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[2][2].bind("<Button-1>",value22)
    #23
    def value23(event):
        value = nums[2][3]['text']
        print(value)
        nums[2][3]['fg'] = "#123"
        nums[2][3]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[2][3].bind("<Button-1>",value23)
    #24
    def value24(event):
        value = nums[2][4]['text']
        print(value)
        nums[2][4]['fg'] = "#123"
        nums[2][4]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[2][4].bind("<Button-1>",value24)
    #30
    def value30(event):
        value = nums[3][0]['text']
        print(value)
        nums[3][0]['fg'] = "#123"
        nums[3][0]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[3][0].bind("<Button-1>",value30)
    #31
    def value31(event):
        value = nums[3][1]['text']
        print(value)
        nums[3][1]['fg'] = "#123"
        nums[3][1]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[3][1].bind("<Button-1>",value31)
    #32
    def value32(event):
        value = nums[3][2]['text']
        print(value)
        nums[3][2]['fg'] = "#123"
        nums[3][2]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[3][2].bind("<Button-1>",value32)
    #33
    def value33(event):
        value = nums[3][3]['text']
        print(value)
        nums[3][3]['fg'] = "#123"
        nums[3][3]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[3][3].bind("<Button-1>",value33)
    #34
    def value34(event):
        value = nums[3][4]['text']
        print(value)
        nums[3][4]['fg'] = "#123"
        nums[3][4]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[3][4].bind("<Button-1>",value34)
    #40
    def value40(event):
        value = nums[4][0]['text']
        print(value)
        nums[4][0]['fg'] = "#123"
        nums[4][0]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[4][0].bind("<Button-1>",value40)
    #41
    def value41(event):
        value = nums[4][1]['text']
        print(value)
        nums[4][1]['fg'] = "#123"
        nums[4][1]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[4][1].bind("<Button-1>",value41)
    #42
    def value42(event):
        value = nums[4][2]['text']
        print(value)
        nums[4][2]['fg'] = "#123"
        nums[4][2]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[4][2].bind("<Button-1>",value42)
    #43
    def value43(event):
        value = nums[4][3]['text']
        print(value)
        nums[4][3]['fg'] = "#123"
        nums[4][3]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[4][3].bind("<Button-1>",value43)
    #44
    def value44(event):
        value = nums[4][4]['text']
        print(value)
        nums[4][4]['fg'] = "#123"
        nums[4][4]['image'] = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((96,96), Image.ANTIALIAS))
        global my_turn 
        my_turn = False
    nums[4][4].bind("<Button-1>",value44)
