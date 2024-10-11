import random

scores = [random.randrange(0, 101) for i in range(30)]
grades = [0] * 11

for score in scores:
    grades[int(score / 10)] += 1

level = {'不及格': sum(grades[0:5]), '及格': grades[6], '中等': grades[7], '良好': grades[8], '优秀': sum(grades[9:10])}
print(scores)
print(grades)
print(level)
