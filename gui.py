import tkinter as tk
from tkinter import messagebox
import os

def start_scan():

    target = target_entry.get()
    start_port = start_port_entry.get()
    end_port = end_port_entry.get()

    if not target:
        messagebox.showerror(
            "Error",
            "Enter Target"
        )
        return

    with open("targets.txt", "w") as f:
        f.write(target)

    status_label.config(
        text="Scan Running..."
    )

    os.system("python main.py")

    status_label.config(
        text="Scan Completed"
    )

def open_reports():

    os.startfile("reports")

def open_dashboard():

    os.startfile("dashboard")

root = tk.Tk()

root.title(
    "Offensive Security Framework"
)

root.geometry("700x500")

title = tk.Label(
    root,
    text="Offensive Security Automation Framework",
    font=("Arial",16,"bold")
)

title.pack(pady=15)

tk.Label(
    root,
    text="Target Domain"
).pack()

target_entry = tk.Entry(
    root,
    width=50
)

target_entry.pack(pady=5)

tk.Label(
    root,
    text="Start Port"
).pack()

start_port_entry = tk.Entry(
    root,
    width=20
)

start_port_entry.insert(0,"1")

start_port_entry.pack(pady=5)

tk.Label(
    root,
    text="End Port"
).pack()

end_port_entry = tk.Entry(
    root,
    width=20
)

end_port_entry.insert(0,"100")

end_port_entry.pack(pady=5)

scan_button = tk.Button(
    root,
    text="Start Scan",
    width=20,
    command=start_scan
)

scan_button.pack(pady=15)

report_button = tk.Button(
    root,
    text="Open Reports",
    width=20,
    command=open_reports
)

report_button.pack(pady=5)

dashboard_button = tk.Button(
    root,
    text="Open Dashboard",
    width=20,
    command=open_dashboard
)

dashboard_button.pack(pady=5)

status_label = tk.Label(
    root,
    text="Ready",
    fg="green"
)

status_label.pack(pady=20)

root.mainloop()