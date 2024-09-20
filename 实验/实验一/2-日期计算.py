from datetime import date, timedelta

if __name__ == "__main__":
    today = date.today()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)

    print("今天的日期:", today)
    print("昨天的日期:", yesterday)
    print("明天的日期:", tomorrow)