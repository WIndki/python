def sum_positive_even_numbers(numbers):
    sum = 0
    for number in numbers:
        if number >0 and number % 2 == 0:
            sum += number
    return sum

def main():
    input_list = input("输入列表空格分隔: ").split()
    input_list = list(map(int,input_list))
    result = sum_positive_even_numbers(input_list)
    print(f"偶数和为: {result}")

if __name__ == "__main__":
    main()
