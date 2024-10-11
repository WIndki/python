import tkinter as tk
import random
import math

class Ball:
    def __init__(self, canvas, x, y, vx, vy, radius, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.color = color
        self.id = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.canvas.move(self.id, self.vx, self.vy)
        self.check_collision_with_walls()

    def check_collision_with_walls(self):
        if self.x - self.radius <= 0 or self.x + self.radius >= self.canvas.winfo_width():
            self.vx = -self.vx
        if self.y - self.radius <= 0 or self.y + self.radius >= self.canvas.winfo_height():
            self.vy = -self.vy

    def check_collision_with_ball(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = math.sqrt(dx**2 + dy**2)
        if distance < self.radius + other.radius:
            self.vx, other.vx = other.vx, self.vx
            self.vy, other.vy = other.vy, self.vy

def update_balls():
    for ball in balls:
        ball.move()
        for other_ball in balls:
            if ball != other_ball:
                ball.check_collision_with_ball(other_ball)
    root.after(20, update_balls)

root = tk.Tk()
root.title("Ball Collision Detection")
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

balls = []
for _ in range(10):
    x = random.randint(50, 750)
    y = random.randint(50, 550)
    vx = random.randint(-5, 5)
    vy = random.randint(-5, 5)
    radius = random.randint(10, 30)
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    balls.append(Ball(canvas, x, y, vx, vy, radius, color))

update_balls()
root.mainloop()