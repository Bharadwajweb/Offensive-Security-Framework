import tkinter as tk
from tkinter import messagebox
import os

def start_scan():
    target = target_entry.get()

    if not target:
        messagebox.showerror("Error", "Enter a target")
        return

    with open("targets.txt", "w") as f:
        f.write(target)

    os.system("python main.py")

root = tk.Tk()

root.title("Offensive Security Framework")
root.geometry("500x300")

title = tk.Label(
    root,
    text="Offensive Security Automation Framework",
    font=("Arial", 14, "bold")
)
title.pack(pady=20)

target_label = tk.Label(
    root,
    text="Target Domain"
)
target_label.pack()

target_entry = tk.Entry(
    root,
    width=40
)
target_entry.pack(pady=10)

scan_button = tk.Button(
    root,
    text="Start Scan",
    command=start_scan,
    width=20,
    height=2
)
scan_button.pack(pady=20)

root.mainloop()