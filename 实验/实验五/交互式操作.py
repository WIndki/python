import sqlite3

# 连接到 SQLite 数据库（如果数据库不存在，则会自动创建）
conn = sqlite3.connect('student_courses.db')
cursor = conn.cursor()

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
    ('Mathematics', 'Dr. Smith', 3),
    ('Physics', 'Dr. Johnson', 4),
    ('Chemistry', 'Dr. Lee', 3),
    ('Biology', 'Dr. White', 2),
    ('Computer Science', 'Dr. Brown', 4)
]

cursor.executemany('INSERT INTO courses (course_name, instructor, credits) VALUES (?, ?, ?)', courses)
conn.commit()

# 查询表中满足某种条件的记录（例如，学分大于3的课程）
cursor.execute('SELECT * FROM courses WHERE credits > 3')
results = cursor.fetchall()
print("Courses with more than 3 credits:")
for row in results:
    print(row)

# 删除表中满足某种条件的记录（例如，课程名称为 'Biology' 的记录）
cursor.execute('DELETE FROM courses WHERE course_name = "Biology"')
conn.commit()

# 修改某条记录（例如，将 'Computer Science' 的学分改为 5）
cursor.execute('UPDATE courses SET credits = 5 WHERE course_name = "Computer Science"')
conn.commit()

# 关闭数据库连接
conn.close()