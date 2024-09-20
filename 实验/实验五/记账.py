import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from datetime import datetime

# 创建数据库连接
conn = sqlite3.connect('./实验/实验五/expenses.db')
c = conn.cursor()

# 创建表格
c.execute('''CREATE TABLE IF NOT EXISTS expenses
             (
             id INTEGER PRIMARY KEY,
             date TEXT,
             amount REAL,
             category TEXT,
             note TEXT
             )
''')
conn.commit()

# 提交数据到数据库
def submit_data():
    date = date_entry.get()
    amount = amount_entry.get()
    category = category_entry.get()
    note = note_entry.get()
    
    if not date or not amount or not category:
        messagebox.showwarning("输入错误", "请填写所有必填字段")
        return
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showwarning("输入错误", "金额必须是数字")
        return
    
    c.execute("INSERT INTO expenses (date, amount, category, note) VALUES (?, ?, ?, ?)",
              (date, amount, category, note))
    conn.commit()
    update_display()
    clear_entries()

# 更新显示框
def update_display():
    c.execute("SELECT * FROM expenses ORDER BY id DESC LIMIT 10")
    records = c.fetchall()
    
    total_amount = sum(record[2] for record in records)
    total_label.config(text=f"总金额: {total_amount:.2f}")
    
    for row in tree.get_children():
        tree.delete(row)
    
    for record in records:
        tree.insert("", "end", values=record[1:])

# 清空输入框
def clear_entries():
    date_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    note_entry.delete(0, tk.END)

# 创建主窗口
root = tk.Tk()
root.title("个人消费记账")

# 创建输入框
tk.Label(root, text="日期 (YYYY-MM-DD):").grid(row=0, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1)

tk.Label(root, text="金额:").grid(row=1, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1)

tk.Label(root, text="消费类型:").grid(row=2, column=0)
category_entry = tk.Entry(root)
category_entry.grid(row=2, column=1)

tk.Label(root, text="备注:").grid(row=3, column=0)
note_entry = tk.Entry(root)
note_entry.grid(row=3, column=1)

tk.Button(root, text="提交", command=submit_data).grid(row=4, column=0, columnspan=2)

# 创建显示框
tree = ttk.Treeview(root, columns=("date", "amount", "category", "note"), show="headings")
tree.heading("date", text="日期")
tree.heading("amount", text="金额")
tree.heading("category", text="消费类型")
tree.heading("note", text="备注")
tree.grid(row=5, column=0, columnspan=2)

total_label = tk.Label(root, text="总金额: 0.00")
total_label.grid(row=6, column=0, columnspan=2)

# 初始化显示
update_display()

# 运行主循环
root.mainloop()

# 关闭数据库连接
conn.close()