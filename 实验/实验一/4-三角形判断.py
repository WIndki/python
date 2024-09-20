import math

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def triangle_type(a, b, c):
    if a == b == c:
        return "等边三角形"
    elif a == b or b == c or a == c:
        return "等腰三角形"
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return "直角三角形"
    else:
        return "普通三角形"

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def main():
    a = float(input("请输入三角形的第一条边长: "))
    b = float(input("请输入三角形的第二条边长: "))
    c = float(input("请输入三角形的第三条边长: "))

    if is_triangle(a, b, c):
        area = triangle_area(a, b, c)
        t_type = triangle_type(a, b, c)
        print(f"可以构成三角形，面积为: {area:.2f}")
        print(f"三角形的类型为: {t_type}")
    else:
        print("不能构成三角形")

if __name__ == "__main__":
    main()