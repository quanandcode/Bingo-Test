from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
from get_value import *
import time
from playsound import playsound
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
#time coutdowwn
giay = 5 * 60 
def down():
    global giay 
    global my_turn
    mins, secs = divmod(giay, 60)
    timer.config(text = str(mins) + ":" + str(int(secs/10))+ str(int(secs%10)))
    if (giay == 0):
        messagebox.showinfo("Time Countdown", "Time's up ")
        return 0
    giay -= 1
    if(my_turn == True):
        timer.after(1000,down)
###########################################################################

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
#music

# play()
#call timecoutdown
down()
playsound("./music/1.mp3", False)
window.mainloop()

# git test
