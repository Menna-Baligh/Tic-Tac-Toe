import tkinter as tk
from tkinter import messagebox
import random
from pygame import mixer

# Initialize mixer for sounds
mixer.init()
win_sound = "win.mp3"
lose_sound = "lose.mp3"
draw_sound = "draw.mp3"

# GUI setup
BG_COLOR = "#f7e1f0"
BUTTON_COLOR = "#c084bf"
BTN_FONT = ("Comic Sans MS", 18, "bold")
TITLE_FONT = ("Comic Sans MS", 26, "bold")
TIMER_FONT = ("Comic Sans MS", 20, "bold")

# Window
window = tk.Tk()
window.title("Tic Tac Toe")
window.configure(bg=BG_COLOR)

# Title
title_label = tk.Label(window, text="Tic Tac Toe", font=TITLE_FONT, bg=BG_COLOR, fg="#4b0049")
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Timer
seconds = 0
timer_running = False
timer_label = tk.Label(window, text="Time: 0s", font=TIMER_FONT, bg=BG_COLOR, fg="#4b0049")
timer_label.grid(row=1, column=0, columnspan=3)

def start_timer():
    global seconds, timer_running
    if timer_running:
        seconds += 1
        timer_label.config(text=f"Time: {seconds}s")
        window.after(1000, start_timer)

def reset_timer():
    global seconds
    seconds = 0
    timer_label.config(text="Time: 0s")

# Game logic
board = [""] * 9
buttons = []

def play_sound(file):
    try:
        mixer.music.load(file)
        mixer.music.play()
    except:
        pass

def check_winner(player):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    return any(board[i] == board[j] == board[k] == player for i, j, k in wins)

def is_draw():
    return all(cell != "" for cell in board)

def computer_move():
    best_score = -float("inf")
    best_move = None
    for i in range(9):
        if board[i] == "":
            board[i] = "X"
            score = minimax(board, 0, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                best_move = i
    if best_move is not None:
        board[best_move] = "X"
        buttons[best_move].config(text="X", state="disabled", disabledforeground="black")
        if check_winner("X"):
            play_sound(lose_sound)
            messagebox.showinfo("Game Over", "You lost!")
            stop_game()
        elif is_draw():
            play_sound(draw_sound)
            messagebox.showinfo("Game Over", "It's a draw!")
            stop_game()

def minimax(board_state, depth, is_maximizing):
    if check_winner("X"):
        return 1
    if check_winner("O"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best = -float("inf")
        for i in range(9):
            if board_state[i] == "":
                board_state[i] = "X"
                score = minimax(board_state, depth + 1, False)
                board_state[i] = ""
                best = max(best, score)
        return best
    else:
        best = float("inf")
        for i in range(9):
            if board_state[i] == "":
                board_state[i] = "O"
                score = minimax(board_state, depth + 1, True)
                board_state[i] = ""
                best = min(best, score)
        return best

def on_click(index):
    if board[index] == "":
        board[index] = "O"
        buttons[index].config(text="O", state="disabled", disabledforeground="#4b0049")
        if check_winner("O"):
            play_sound(win_sound)
            messagebox.showinfo("Game Over", "You won!")
            stop_game()
        elif is_draw():
            play_sound(draw_sound)
            messagebox.showinfo("Game Over", "It's a draw!")
            stop_game()
        else:
            window.after(500, computer_move)

def stop_game():
    global timer_running
    timer_running = False
    for btn in buttons:
        btn.config(state="disabled")

def reset_board():
    global board, timer_running
    board = [""] * 9
    for btn in buttons:
        btn.config(text="", state="normal")
    reset_timer()
    timer_running = True
    start_timer()

# Board buttons
for i in range(9):
    btn = tk.Button(window, text="", font=BTN_FONT, width=6, height=3, bg=BUTTON_COLOR,


command=lambda i=i: on_click(i))
    btn.grid(row=(i//3)+2, column=i%3, padx=5, pady=5)
    buttons.append(btn)

# Control buttons
btn_restart = tk.Button(window, text="Restart", font=BTN_FONT, bg="#ab52a0", fg="white", command=reset_board)
btn_restart.grid(row=5, column=0, columnspan=1, pady=15)

btn_exit = tk.Button(window, text="Exit", font=BTN_FONT, bg="#ab52a0", fg="white", command=window.quit)
btn_exit.grid(row=5, column=2, columnspan=1)

# Start the game
timer_running = True
start_timer()
window.mainloop()