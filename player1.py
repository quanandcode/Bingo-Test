from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
from get_value import *
import time
from playsound import playsound
from kiem_tra_bingo import *
# from get_value import value
window = Tk()
window.geometry("1000x625")
window.title('BINGO')
window.resizable(width=False, height=False)

# CREATE your_turn
your_turn_size = [200, 100]
your_turn_img = ImageTk.PhotoImage(Image.open(
    "./images/your_turn.png").resize((your_turn_size), Image.ANTIALIAS))
your_turn = Label(window, image=your_turn_img)
# CREATE opponent's turn
opponent_turn_size = [200, 100]
opponent_turn_img = ImageTk.PhotoImage(Image.open(
    "./images/opponent_turn.png").resize((your_turn_size), Image.ANTIALIAS))
opponent_turn = Label(window, image=opponent_turn_img)
# DEF turn


def Turn(turn):
    turn.place(x=25, y=25)


# CALL turn
Turn(your_turn)
###########################################################################
# CREATE timer
timer_size = [200, 150]
timer_img = ImageTk.PhotoImage(Image.open(
    "./images/timer.png").resize((timer_size), Image.ANTIALIAS))
timer = Label(window, image=timer_img, compound=CENTER, font=("Comic Sans MS", 48),
              text="05:00")
# CALL timer
# timer.config(text="00:01")

timer.place(x=25, y=25+(100+25))
# time coutdowwn
giay = 5 * 60
my_turn = True
value = 0
def down():
    global giay
    global my_turn
    mins, secs = divmod(giay, 60)
    timer.config(text=str(mins) + ":" +
                 str(int(secs/10)) + str(int(secs % 10)))
    giay -= 1
    if (giay == 0):
        messagebox.showinfo("Time Countdown", "Time's up ")
        return 0    
    if (my_turn == True):
        timer.after(1000, down)
###########################################################################

def bind_all(nums):
    def value00(event): 
        value = nums[0][0]['text']
        print(value)
        nums[0][0]['fg'] = "#123"
        nums[0][0]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[0][0].bind("<Button-1>", value00)
    # 01

    def value01(event):
        value = nums[0][1]['text']
        print(value)
        nums[0][1]['fg'] = "#123"
        nums[0][1]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[0][1].bind("<Button-1>", value01)
    # 02

    def value02(event):
        value = nums[0][2]['text']
        print(value)
        nums[0][2]['fg'] = "#123"
        nums[0][2]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[0][2].bind("<Button-1>", value02)
    # 03

    def value03(event):
        value = nums[0][3]['text']
        print(value)
        nums[0][3]['fg'] = "#123"
        nums[0][3]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[0][3].bind("<Button-1>", value03)
    # 04

    def value04(event):
        value = nums[0][4]['text']
        print(value)
        nums[0][4]['fg'] = "#123"
        nums[0][4]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[0][4].bind("<Button-1>", value04)
    # 10

    def value10(event):
        value = nums[1][0]['text']
        print(value)
        nums[1][0]['fg'] = "#123"
        nums[1][0]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[1][0].bind("<Button-1>", value10)
    # 11

    def value11(event):
        value = nums[1][1]['text']
        print(value)
        nums[1][1]['fg'] = "#123"
        nums[1][1]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[1][1].bind("<Button-1>", value11)
    # 12

    def value12(event):
        value = nums[1][2]['text']
        print(value)
        nums[1][2]['fg'] = "#123"
        nums[1][2]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[1][2].bind("<Button-1>", value12)
    # 13

    def value13(event):
        value = nums[1][3]['text']
        print(value)
        nums[1][3]['fg'] = "#123"
        nums[1][3]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[1][3].bind("<Button-1>", value13)
    # 14

    def value14(event):
        value = nums[1][4]['text']
        print(value)
        nums[1][4]['fg'] = "#123"
        nums[1][4]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[1][4].bind("<Button-1>", value14)
    # 20

    def value20(event):
        value = nums[2][0]['text']
        print(value)
        nums[2][0]['fg'] = "#123"
        nums[2][0]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[2][0].bind("<Button-1>", value20)
    # 21

    def value21(event):
        value = nums[2][1]['text']
        print(value)
        nums[2][1]['fg'] = "#123"
        nums[2][1]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[2][1].bind("<Button-1>", value21)
    # 22

    def value22(event):
        value = nums[2][2]['text']
        print(value)
        nums[2][2]['fg'] = "#123"
        nums[2][2]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[2][2].bind("<Button-1>", value22)
    # 23

    def value23(event):
        value = nums[2][3]['text']
        print(value)
        nums[2][3]['fg'] = "#123"
        nums[2][3]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[2][3].bind("<Button-1>", value23)
    # 24

    def value24(event):
        value = nums[2][4]['text']
        print(value)
        nums[2][4]['fg'] = "#123"
        nums[2][4]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[2][4].bind("<Button-1>", value24)
    # 30

    def value30(event):
        value = nums[3][0]['text']
        print(value)
        nums[3][0]['fg'] = "#123"
        nums[3][0]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[3][0].bind("<Button-1>", value30)
    # 31

    def value31(event):
        value = nums[3][1]['text']
        print(value)
        nums[3][1]['fg'] = "#123"
        nums[3][1]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[3][1].bind("<Button-1>", value31)
    # 32

    def value32(event):
        value = nums[3][2]['text']
        print(value)
        nums[3][2]['fg'] = "#123"
        nums[3][2]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[3][2].bind("<Button-1>", value32)
    # 33

    def value33(event):
        value = nums[3][3]['text']
        print(value)
        nums[3][3]['fg'] = "#123"
        nums[3][3]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[3][3].bind("<Button-1>", value33)
    # 34

    def value34(event):
        value = nums[3][4]['text']
        print(value)
        nums[3][4]['fg'] = "#123"
        nums[3][4]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[3][4].bind("<Button-1>", value34)
    # 40

    def value40(event):
        value = nums[4][0]['text']
        print(value)
        nums[4][0]['fg'] = "#123"
        nums[4][0]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[4][0].bind("<Button-1>", value40)
    # 41

    def value41(event):
        value = nums[4][1]['text']
        print(value)
        nums[4][1]['fg'] = "#123"
        nums[4][1]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[4][1].bind("<Button-1>", value41)
    # 42

    def value42(event):
        value = nums[4][2]['text']
        print(value)
        nums[4][2]['fg'] = "#123"
        nums[4][2]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[4][2].bind("<Button-1>", value42)
    # 43

    def value43(event):
        value = nums[4][3]['text']
        print(value)
        nums[4][3]['fg'] = "#123"
        nums[4][3]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[4][3].bind("<Button-1>", value43)
    # 44

    def value44(event):
        value = nums[4][4]['text']
        print(value)
        nums[4][4]['fg'] = "#123"
        nums[4][4]['image'] = ImageTk.PhotoImage(Image.open(
            "./images/num_click.png").resize((96, 96), Image.ANTIALIAS))
        global my_turn
        my_turn = False
    nums[4][4].bind("<Button-1>", value44)


# CREATE Score


score_arr = [0, 0]
score_history = ['W', 'L', 'L']  # win,loss
score_size = [200, 125]
score_img = ImageTk.PhotoImage(Image.open(
    "./images/score.png").resize((score_size), Image.ANTIALIAS))
score = Label(window, image=score_img, compound=CENTER, font=("Comic Sans MS", 48), fg="#ffc90e", cursor="hand2",
              text=str(score_arr[0])+" : "+str(score_arr[1]))
# CALL score
score.place(x=25, y=25+(100+25)+(25+150))
# score event


def show_score_chart(event):
    score_window = Tk()
    score_window.geometry("300x100")
    score_window.title("History")
    #
    hist = "History:\n"
    for his in score_history:
        hist += his+" "
    show_history_title = Label(score_window, text=hist)
    show_history_title.pack()
    score_window.mainloop()


score.bind("<Button-1>", show_score_chart)
###########################################################################
# CREATE leave
leave_size = [200, 100]
leave_img = ImageTk.PhotoImage(Image.open(
    "./images/leave.png").resize((leave_size), Image.ANTIALIAS))
leave = Label(window, image=leave_img, cursor="hand2")
# CALL leave
leave.place(x=25, y=25+(100+25)+(25+150)+(50+125))
# leave event


def Leave(event):
    global leave_size, leave_img, leave
    # leave button status
    leave_img = ImageTk.PhotoImage(Image.open(
        "./images/leave_click.png").resize((leave_size), Image.ANTIALIAS))
    leave = Label(window, image=leave_img, cursor="hand2", relief=RAISED)
    leave.place(x=25, y=25+(100+25)+(25+150)+(50+125))
    # messagebox
    if messagebox.askokcancel(title='Quit game', message='Do you wanna quit?'):
        quit()
    else:
        leave_img = ImageTk.PhotoImage(Image.open(
            "./images/leave.png").resize((leave_size), Image.ANTIALIAS))
        leave = Label(window, image=leave_img, cursor="hand2", relief=FLAT)
        leave.place(x=25, y=25+(100+25)+(25+150)+(50+125))
        leave.bind("<Button-1>", Leave)


leave.bind("<Button-1>", Leave)
###########################################################################
# CREATE board
board_size = [500, 500]
board_img = ImageTk.PhotoImage(Image.open(
    "./images/board.png").resize((board_size), Image.ANTIALIAS))
board = Label(window, image=board_img)
# CALL board
board.place(x=25+(200+25), y=25)
###########################################################################
# CREATE submit
submit_size = [100, 50]
submit_img = ImageTk.PhotoImage(Image.open(
    "./images/submit.png").resize((submit_size), Image.ANTIALIAS))
submit = Button(window, image=submit_img)
# CALL submit
submit.place(x=25+(200+25+200), y=25+(500+20))
###########################################################################
# CREATE num
# Create number array
sub_num_array = random.sample(range(1, 26), 25)
num_array = []  # number array
for i in range(5):
    sub_arr = sub_num_array[5*i:5*i+5]
    num_array += [sub_arr]
#
# Create number matrix gui
nums = [[], [], [], [], []]
num_size = [96, 96]
nums_locate = [[], [], [], [], []]
num_img = ImageTk.PhotoImage(Image.open(
    "./images/num.png").resize((num_size), Image.ANTIALIAS))
for i in range(5):  # row, x moves, y stays
    y = 2+(96+2)*i
    for j in range(5):  # column, y moves, x stays
        x = 2+(96+2)*j
        num = Label(board, image=num_img, font=("Comic Sans MS", 48),
                    compound=CENTER, fg="orange", text=str(num_array[i][j]))
        # num.bind("<Button-1>",click)
        # num[]
        nums[i].append(num)
        # location[]
        temp = [x, y]
        nums_locate[i].append(temp)
# DEF click event
# num_img_click = ImageTk.PhotoImage(Image.open("./images/num_click.png").resize((num_size), Image.ANTIALIAS))
# bind
bind_all(nums)
# CALL num
for row in range(5):
    for col in range(5):
        x, y = nums_locate[row][col]
        num = nums[row][col]
        num.place(x=x, y=y)

#############################
# CREATE table
table_size = [200,200]
table_img = ImageTk.PhotoImage(Image.open(
    "./images/table.png").resize((table_size), Image.ANTIALIAS))
table = Label(window, image=table_img)
# CALL table
table.place(x=25+ 200 +25 + 500 + 25, y=25)
###################################################
# CREATE anime
anime_size = [200,350]
anime_img = ImageTk.PhotoImage(Image.open(
    "./images/anime.png").resize((anime_size), Image.ANTIALIAS))
anime = Label(window, image=anime_img)
# CALL anime
anime.place(x=25+ 200 +25 + 500 + 25, y=25 + 200 + 25)
##############################################################
#Call test function
# music
# call timecoutdown
down()
playsound("./music/1.mp3", False)
window.mainloop()

# creat-table

