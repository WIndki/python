def date_format(date):
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    return year + "年" + month + "月" + day + "日"

def main():
    date = input("输入日期(YYYYMMDD): ")
    date = date_format(date)
    print(f"格式化后的日期为: {date}")

if __name__ == "__main__":
    main()