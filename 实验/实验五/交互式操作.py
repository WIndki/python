import sqlite3

# 连接到 SQLite 数据库（如果数据库不存在，则会自动创建）
conn = sqlite3.connect('./实验/实验五/student_courses.db')
cursor = conn.cursor()

#删除表
cursor.execute('DROP TABLE IF EXISTS courses')

# 创建本学期课程表
cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    instructor TEXT NOT NULL,
    credits INTEGER NOT NULL
)
''')

# 插入5条记录
courses = [
    ('数学', '老师一', 3),
    ('物理', '老师二', 4),
    ('化学', '老师三', 3),
    ('生物', '老师四', 2),
    ('计算机', '老师五', 4)
]

cursor.executemany('INSERT INTO courses (course_name, instructor, credits) VALUES (?, ?, ?)', courses)
conn.commit()

# 查询表中满足某种条件的记录（例如，学分大于3的课程）
cursor.execute('SELECT * FROM courses WHERE credits > 3')
results = cursor.fetchall()
print("大于三学分的绩点有：")
for row in results:
    print(row)

# 删除表中满足某种条件的记录（例如，课程名称为 'Biology' 的记录）
cursor.execute('DELETE FROM courses WHERE course_name = "生物"')
conn.commit()

# 修改某条记录（例如，将 'Computer Science' 的学分改为 5）
cursor.execute('UPDATE courses SET credits = 5 WHERE course_name = "计算机"')
conn.commit()

cursor.execute('SELECT * FROM courses')
results = cursor.fetchall()
print("修改后的课程表：")
for row in results:
    if row[3] > 0:
        print(row)

# 关闭数据库连接
conn.close()