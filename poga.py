import tkinter as tk
from tkinter import messagebox
import time

root = tk.Tk()
click_count = 0
start_time = 0
click_speed = 0
green = 255
blue = 255

def setup_start_screen():
    global start_frame
    start_frame = tk.Frame(root, bg='white')
    start_frame.pack(fill='both', expand=True)

    start_label = tk.Label(start_frame, text="Pogas Spiešanas Spēle", font=('Verdana', 24, 'bold'), bg='white')
    start_label.pack(pady=40)

    start_button = tk.Button(start_frame, text="Sākt", command=start_game, width=20, height=2, bg='lightgray')
    start_button.pack(pady=20)

def start_game():
    global start_time
    start_frame.pack_forget()
    setup_game_screen()
    start_time = time.time()
    ttime()

def setup_game_screen():
    global game_frame, click_label, click_button, time_label, click_speed_label
    game_frame = tk.Frame(root, bg='white')
    game_frame.pack(fill='both', expand=True)

    global click_label, click_speed_label, time_label, click_button
    click_label = tk.Label(game_frame, text=f"Spiešanas skaits: {click_count}", font=('Verdana', 16), bg='white')
    click_label.pack(pady=20)

    click_speed_label = tk.Label(game_frame, text=f"Vidējais spiešanas ātrums: {click_speed:.2f}", font=('Verdana', 16), bg='white')
    click_speed_label.pack(pady=20)

    click_button = tk.Button(game_frame, text="Spied mani!", command=click, bg='lightgray')
    click_button.pack(pady=20)

    time_label = tk.Label(game_frame, text="Laiks: 0s", font=('Verdana', 16), bg='white')
    time_label.pack(pady=20)

def click():
    global click_count, click_label
    click_count += 1
    click_label.config(text=f"Spiešanas skaits: {click_count}")

def ttime():
    global start_time, click_speed_label, click_count, game_frame, green, blue, time_label, click_speed
    elapsed_time = time.time() - start_time
    time_label.config(text=f"Laiks: {int(elapsed_time)}s")

    if elapsed_time > 0:
        click_speed = click_count / elapsed_time
        click_speed_label.config(text=f"Vidējais spiešanas ātrums: {click_speed:.2f} klikšķi/sec")

        if click_speed > 0:
            target_green = max(0, 255 - int(click_speed * 30))
            target_blue = max(0, 255 - int(click_speed * 15))

            if green > target_green:
                green = max(target_green, green - 1)
            else:
                green = min(target_green, green + 1)

            if blue > target_blue:
                blue = max(target_blue, blue - 1)
            else:
                blue = min(target_blue, blue + 1)

        hex_color = f'#FF{green:02x}{blue:02x}'
        game_frame.config(bg=hex_color)

    root.after(50, ttime)

def end_game():
    elapsed_time = int(time.time() - start_time)
    messagebox.showinfo("Spēles beigas", f"Tu esi nospiedis pogu {click_count} reizes {elapsed_time} sekundēs, un tavs vidējais ātrums bija {click_speed:.2f} klikšķi/sec!")
    root.destroy()

root.title("Pogas Spiešanas Spēle")
root.geometry("400x400")
root.protocol("WM_DELETE_WINDOW", end_game)

setup_start_screen()
root.mainloop()
