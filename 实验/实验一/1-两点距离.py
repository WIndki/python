import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def main():
    print("输入(x1, y1):")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))

    print("输入(x2, y2):")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))

    distance = calculate_distance(x1, y1, x2, y2)
    print(f"({x1}, {y1}) 与 ({x2}, {y2}) 距离为 {distance}")

if __name__ == "__main__":
    main()