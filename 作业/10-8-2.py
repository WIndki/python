from datetime import datetime
today = datetime.date(datetime.now())
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if today.year % 4 == 0 and today.year % 100 != 0 or today.year % 400 == 0:
    months[1] = 29
days = sum(months[:today.month - 1]) + today.day
print('今天是今年的第{}天'.format(days))