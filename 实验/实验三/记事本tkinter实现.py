import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text_area.get(1.0, tk.END))

def save_as_file():
    save_file()

def undo():
    text_area.event_generate("<<Undo>>")

def redo():
    text_area.event_generate("<<Redo>>")

def copy():
    text_area.event_generate("<<Copy>>")

def cut():
    text_area.event_generate("<<Cut>>")

def paste():
    text_area.event_generate("<<Paste>>")

def find_text():
    find_string = simpledialog.askstring("Find", "Enter text to find:")
    if find_string:
        start_pos = text_area.search(find_string, "1.0", tk.END)
        if start_pos:
            end_pos = f"{start_pos}+{len(find_string)}c"
            text_area.tag_add("highlight", start_pos, end_pos)
            text_area.tag_config("highlight", background="yellow")

def select_all():
    text_area.tag_add("sel", "1.0", tk.END)

def show_about():
    messagebox.showinfo("About", "Author: 黄勉嘉\n")

root = tk.Tk()
root.title("记事本")

text_area = tk.Text(root, undo=True)
text_area.pack(expand=True, fill='both')

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="新建", command=new_file)
file_menu.add_command(label="打开", command=open_file)
file_menu.add_command(label="保存", command=save_file)
file_menu.add_command(label="另存为", command=save_as_file)
menu_bar.add_cascade(label="文件", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="撤销", command=undo)
edit_menu.add_command(label="重做", command=redo)
edit_menu.add_command(label="复制", command=copy)
edit_menu.add_command(label="剪切", command=cut)
edit_menu.add_command(label="粘贴", command=paste)
edit_menu.add_command(label="查找", command=find_text)
edit_menu.add_command(label="全选", command=select_all)
menu_bar.add_cascade(label="编辑", menu=edit_menu)

about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label="作者", command=show_about)
menu_bar.add_cascade(label="关于", menu=about_menu)

root.config(menu=menu_bar)
root.mainloop()