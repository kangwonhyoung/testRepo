import tkinter as tk
import random
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

root = tk.Tk()
root.title("OXbingo Game")
#root.geometry('300x250')

def check_for_win(b, p):
    if ((b[1] == p and b[2] == p and b[3] == p) or
    (b[4] == p and b[5] == p and b[6] == p) or
    (b[7] == p and b[8] == p and b[9] == p) or
    (b[1] == p and b[4] == p and b[7] == p) or
    (b[2] == p and b[5] == p and b[8] == p) or
    (b[3] == p and b[6] == p and b[9] == p) or
    (b[3] == p and b[5] == p and b[7] == p) or
    (b[1] == p and b[5] == p and b[9] == p)):
        return tk.Label(root, text = 'WIN')
    else:
        return tk.Label(root, text = 'LOSE')
def get_user_move(board):
    loc = board
    return loc

def button_click(board):

    for i in board:
        if is_free(board, i):
            board[i] = 'O'
            if check_for_win(board, 'O'):
                board[i] = ' '
                return i
            board[i] = ' '
    for i in board:
        if is_free(board, i):
            board[i] = 'X'
            if check_for_win(board, 'X'):
                board[i] = ' '
                return i
            board[i] = ' '
    for i in [button1, button3, button7, button9]:
        if is_free(board, i):
            return i
    if is_free(board, button5):
        return button5
    for i in [button2, button4, button6, button8]:
        if is_free(board, i):
            return i

def check_for_tie(board):
    for i in board:
        if is_free(board, i):
            return False
    return True

def playing(board):
    if turn == 'X':
        loc = get_user_move(board)
        board = 'X'
    else:
        loc = get_computer_move(board)
        board[loc] = 'O'
    if check_for_win(board, turn):
        draw_board(board)
        print(turn)
        tk.Label(root, text = '승리').pack()
        playing = False
    else:
        if check_for_tie(board):
            draw_board(board)
            tk.Label(root, text = '무승부').pack()
            playing = False
        else:
            if turn == 'X': turn = 'O'
            else : turn = 'X'

playing = True
turn = 'X'

button1 = tk.Button(root, text="1", command = button_click, width = 5, height = 2, font = (None, 20)).grid(column=1, row=1)
button2 = tk.Button(root, text="2", command = button_click, width = 5, height = 2, font = (None, 20)).grid(column=2, row=1)
button3 = tk.Button(root, text="3", command = button_click, width = 5, height = 2, font = (None, 20)).grid(column=3, row=1)
button4 = tk.Button(root, text="4", command = button_click, width = 5, height = 2, font = (None, 20)).grid(column=1, row=2)
button5 = tk.Button(root, text="5", command = button_click, width = 5, height = 2, font = (None, 20)).grid(column=2, row=2)
button6 = tk.Button(root, text="6", command = button_click, width = 5, height = 2, font = (None, 20)).grid(column=3, row=2)
button7 = tk.Button(root, text="7", command = button_click, width = 5, height = 2, font = (None, 20)).grid(column=1, row=3)
button8 = tk.Button(root, text="8", command = button_click, width = 5, height = 2, font = (None, 20)).grid(column=2, row=3)
button9 = tk.Button(root, text="9", command = button_click, width = 5, height = 2, font = (None, 20)).grid(column=3, row=3)

board = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
playing = True
turn = 'X'
root.mainloop()
