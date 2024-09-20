import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def main():
    radius = float(input("输入圆的半径: "))
    if radius >= 0:
        area = calculate_circle_area(radius)
        print(f"=半径{radius}圆的面积是{area:.2f}")
    else:
        print("半径不能为负数")

if __name__ == "__main__":
    main()