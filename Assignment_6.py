import tkinter as tk

def menu_command():
    print("Menu command executed!")

root = tk.Tk()
root.geometry("300x300")
# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=menu_command)
file_menu.add_command(label="Open", command=menu_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create an Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=menu_command)
edit_menu.add_command(label="Copy", command=menu_command)
edit_menu.add_command(label="Paste", command=menu_command)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

root.mainloop()
