def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2]) #动态规划求解
    return fib_sequence

def main():
    n = int(input("输入斐波那契数列的长度: "))
    fib_sequence = fibonacci(n)
    print(f"斐波那契数列的前{n}项为: {fib_sequence}")

if __name__ == "__main__":
    main()