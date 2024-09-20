def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def calculate_Prime(numbers):
    prime_numbers = []
    for number in numbers:
        if isPrime(number):
            prime_numbers.append(number)
    return prime_numbers

def main():
    start = int(input("输入开始值: "))
    end = int(input("输入结束值: "))
    numbers = list(range(start, end+1))
    prime_numbers = calculate_Prime(numbers)
    print(f"在{start}和{end}之间的素数有{len(prime_numbers)}个，有：{prime_numbers}")

if __name__ == "__main__":
    main()