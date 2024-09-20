def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def main():
    x1, y1 = float(input("输入第一象限点的坐标(x1, y1): "))
    x2, y2 = float(input("输入第三象限点的坐标(x2, y2): "))
    distance = calculate_distance(x1, y1, x2, y2)
    print(f"两点之间的距离为: {distance}")