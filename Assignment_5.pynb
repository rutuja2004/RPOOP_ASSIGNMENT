import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

def label1_hover_enter(event):
    label1.config(bg="green")

def label1_hover_leave(event):
    label1.config(bg="red")

label1 = tk.Label(root, text="Label 1", bg="red", fg="white")
label1.pack(pady=10)
label1.bind("<Enter>", label1_hover_enter)
label1.bind("<Leave>", label1_hover_leave)

def label2_hover_enter(event):
    label2.config(bg="yellow")

def label2_hover_leave(event):
    label2.config(bg="blue")

label2 = tk.Label(root, text="Label 2", bg="blue", fg="white")
label2.pack(pady=10)
label2.bind("<Enter>", label2_hover_enter)
label2.bind("<Leave>", label2_hover_leave)

root.mainloop()
