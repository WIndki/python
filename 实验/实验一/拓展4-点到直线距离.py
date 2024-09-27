import math

def line_equation(x1, y1, x2, y2):
    if x1 == x2:
        print("垂直线的斜率不存在")
        return None,None
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    return k, b

def point_to_line_distance(x0, y0, k, b):
    distance = abs(k * x0 - y0 + b) / math.sqrt(k**2 + 1)
    return distance

def main():
    #输入两点，计算直线方程
    x1, y1 = map(float, input("第一个点x1,y1").split())
    x2, y2 = map(float, input("第二个点x2,y2").split())
    k,b = line_equation(x1, y1, x2, y2)
    if not k is None:
        print(f"直线方程为：y = {k}x + {b}")
        x0, y0 = map(float, input("第三个点 (x0 y0): ").split())
        distance = point_to_line_distance(x0, y0, k, b)
    else:
        distance = abs(x0 - x1)
    print(f"点({x0}, {y0}) 到直线 y = {k}x + {b} 的距离是 {distance:.2f}")

if __name__ == "__main__":
    main()