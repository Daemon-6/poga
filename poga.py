import tkinter as tk
from tkinter import messagebox
import time


root = tk.Tk()
click_count = 0
start_time = 0

def setup_start_screen():
    global start_frame
    start_frame = tk.Frame(root)
    start_frame.pack(fill='both', expand=True)

    start_label = tk.Label(start_frame, text="Pogas Spiešanas Spēle", font=('Verdana', 24, 'bold'))
    start_label.pack(pady=40)

    start_button = tk.Button(start_frame, text="Sākt", command=start_game, width=20, height=2)
    start_button.pack(pady=20)

def start_game():
    global start_time
    start_frame.pack_forget()
    setup_game_screen()
    start_time = time.time()
    ttime()

def setup_game_screen():
    global game_frame, click_label, click_button, time_label
    game_frame = tk.Frame(root)
    game_frame.pack(fill='both', expand=True)

    global click_count
    click_label = tk.Label(game_frame, text=f"Spiešanas skaits: {click_count}", font=('Verdana', 16))
    click_label.pack(pady=20)

    click_button = tk.Button(game_frame, text="Spied mani!", command=click)
    click_button.pack(pady=20)

    time_label = tk.Label(game_frame, text="Laiks: 0s", font=('Verdana', 16))
    time_label.pack(pady=20)

def click():
    global click_count, click_label
    click_count += 1
    click_label.config(text=f"Spiešanas skaits: {click_count}")

def ttime():
    elapsed_time = int(time.time() - start_time)
    time_label.config(text=f"Laiks: {elapsed_time}s")
    root.after(1000, ttime)

def end_game():
    elapsed_time = int(time.time() - start_time)
    messagebox.showinfo("Spēles beigas", f"Tu esi nospiedis pogu {click_count} reizes {elapsed_time} sekundēs!")
    root.destroy()

root.title("Pogas Spiešanas Spēle")
root.geometry("400x400")
root.protocol("WM_DELETE_WINDOW", end_game)

setup_start_screen()
root.mainloop()
