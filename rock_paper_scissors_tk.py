
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import random as r
import time

def btn_rock_click():
    #print('Button Rock Clicked')
    plyr1.ply_choice = 'rock' 
    plyr2.ply_choice = rand_choice()
    label_im1['image']=choices[plyr1.ply_choice]
    label_im2['image']=choices[plyr2.ply_choice]
    game()

    return True    

def btn_paper_click():
    #print('Button Paper Clicked')
    plyr1.ply_choice = 'paper'
    plyr2.ply_choice = rand_choice()
    label_im1['image']=choices[plyr1.ply_choice]
    label_im2['image']=choices[plyr2.ply_choice]
    game()
    return True

def btn_scissors_click():
    #print('Button Scissors Clicked')
    plyr1.ply_choice = 'scissors' 
    plyr2.ply_choice = rand_choice()
    label_im1['image']=choices[plyr1.ply_choice]
    label_im2['image']=choices[plyr2.ply_choice]
    game()
    return True

def btn_restart():
    global plyr1
    global plyr2
    del plyr1
    del plyr2
    plyr1 = Player('Ali')
    plyr2 = Player('Computer')
    label_scr1['text']='0'
    label_scr2['text']='0'
    label_3['text']=f'Ready to Start'
    label_im1['text'] = ''
    label_im2['text'] = ''
    #label_3['text']=f'{plyr1.name} -- {plyr2.name}'

def btn_exit():
    winner_msg = "it is a tie" if plyr1.user_score == plyr2.user_score else ("Player1 won!" if plyr1.user_score > plyr2.user_score else "Player2 won!")
    message = "--------------------------------"
    message += "\n"
    message += f"\nYour Score: {plyr1.user_score}"
    message += f"\nThe computer Score: {plyr2.user_score}"
    message += f"\n{winner_msg}"
    message += "\n"
    message += "\n--------------------------------"
    message += "\nThanks for playing. Please play again!"
    tkinter.messagebox.showinfo("Results...", message)
    root.destroy()

class Player:
    """docstring for ClassName"""
    def __init__(self, name):
        self.name = name
        self.user_score = 0
        self.tie_no = 0
        self.ply_choice = 'None'


def game():
    global plyr1
    global plyr2
    winner = winner_choice(plyr1.ply_choice, plyr2.ply_choice)
    if winner!=None:
        if winner==plyr1.ply_choice:
            plyr1.user_score += 1
            label_scr1['text'] = str(plyr1.user_score)
            label_3['text'] = 'Player1 won!'
        else:
            plyr2.user_score += 1
            label_scr2['text'] = str(plyr2.user_score)
            label_3['text'] = 'Player2 won!'
    else:
        plyr1.tie_no += 1
        plyr2.tie_no += 1
        label_3['text'] = 'It is a tie!'
    
    return True    



def rand_choice():
    options=["rock", "paper", "scissors"]
    return r.choice(options)

        
def winner_choice(chc1, chc2):
        
    winners = {
        "rock":{
            "rock": None,       # it is a tie
            "paper": "paper",   # winners["rock"]["paper"] = "paper" winner 
            "scissors": "rock", # winners["rock"]["scissors"] = "rock" winner
        },
        "paper":{
            "rock": "paper",
            "paper": None,      # it is a tie
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,   # it is a tie
        },
    }

    winner = winners[chc1][chc2]

    return winner


plyr1 = Player('Ali')
plyr2 = Player('Computer')

root = tk.Tk()
root.geometry('700x650')
root.resizable(False, False)
root.title('Rock-Paper-Scissors')
font=("Helvetica", 14)

images={'player_1':tk.PhotoImage(file='./assets/player11.png'),'player_2':tk.PhotoImage(file='./assets/player2.png'),'vs':tk.PhotoImage(file='./assets/vs1.png')}
choices={'rock':tk.PhotoImage(file='./assets/rock75.png'),'paper':tk.PhotoImage(file='./assets/paper75.png'),'scissors':tk.PhotoImage(file='./assets/scissors75.png'),'None': ''}
img1=plyr1.ply_choice

rock_icon = tk.PhotoImage(file='./assets/rock2.png')
paper_icon = tk.PhotoImage(file='./assets/paper2.png')
scissors_icon = tk.PhotoImage(file='./assets/scissors2.png')
player1_icon = tk.PhotoImage(file='./assets/player175.png')
player2_icon = tk.PhotoImage(file='./assets/player275.png')
vs_icon = tk.PhotoImage(file='./assets/vs15.png')
think_icon = tk.PhotoImage(file='./assets/thinking.png')



label_1 = ttk.Label(root, text='Rock-Paper-Scissors', foreground="brown", font=("Helvetica", 25, 'bold'))
label_1.grid(column=0, row=0, columnspan=6, padx=5, pady=5)

label_p1 = ttk.Label(root, image=player1_icon, text='PLAYER-1', foreground="red", compound=tk.BOTTOM, font=("Helvetica", 15, 'bold'))
label_p1.grid(column=0, row=1, padx=5, pady=5)

label_s1 = ttk.Label(root,image=vs_icon)
label_s1.grid(column=1, row=1, columnspan=4, padx=5, pady=5)

label_p2 = ttk.Label(root, image=player2_icon, text='PLAYER-2', foreground="blue", compound=tk.BOTTOM, font=("Helvetica", 15, 'bold'))
label_p2.grid(column=5, row=1, padx=5, pady=5)

label_scr1 = ttk.Label(root, text='0', foreground="white", background="black", font=("Helvetica", 35), width=3, padding=[3,3,3,3])
label_scr1.grid(column=0, row=2, padx=5, pady=5)

label_3 = ttk.Label(root, text='Ready to Start', font=("Helvetica", 25), width=13)
label_3.grid(column=1, row=2, columnspan=4, padx=5, pady=5)

label_scr2 = ttk.Label(root, text='0', foreground="white", background="black", font=("Helvetica", 35), width=3, padding=[3,3,3,3])
label_scr2.grid(column=5, row=2, padx=5, pady=5)

label_s2 = ttk.Label(root, text='What is your choice :', font=("Helvetica", 16), padding=[3,3,3,3])
label_s2.grid(column=1, row=3, columnspan=4, padx=5, pady=5)

label_im1 = ttk.Label(root, text='', font=("Helvetica", 45))
label_im1.grid(column=0, row=3, padx=5, pady=5)

label_im2 = ttk.Label(root, text='', font=("Helvetica", 45))
label_im2.grid(column=5, row=3, padx=5, pady=5)


btn_rock = tk.Button(root, image=rock_icon, text='ROCK', compound=tk.TOP, relief="ridge", command=btn_rock_click)
btn_rock.grid(column=0, row=4, columnspan=2, rowspan=2, padx=5, pady=5)

btn_paper = tk.Button(root, image=paper_icon, text='PAPER', compound=tk.TOP, relief="ridge", command=btn_paper_click)
btn_paper.grid(column=2, row=4, columnspan=2, rowspan=2, padx=5, pady=5)

btn_scissors = tk.Button(root, image=scissors_icon, text='SCISSORS', compound=tk.TOP, relief="ridge", command=btn_scissors_click)
btn_scissors.grid(column=4, row=4, columnspan=2, rowspan=2, padx=5, pady=5)

btn_exit = ttk.Button(root, text='Exit', command=btn_exit, width=14)
btn_exit.grid(column=4, row=6, pady=10)

btn_restart = ttk.Button(root, text='Restart',command=btn_restart, width=14)
btn_restart.grid(column=5, row=6)



root.mainloop()
