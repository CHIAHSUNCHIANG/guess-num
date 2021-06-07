#產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了"
# 猜錯的話 要告訴他比答案大/小


import random
start = input('Please choose the start number of the random number list: ')
end = input('Please choose the end number of the random number list: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0

while True:
    count += 1
    number = input('Please type in one number between 1 ~ 100: ')
    number = int(number)
    if number == r:
        print('You are correct')
        print('This is your', count, 'times')
        break
    elif number > r:
        print('Your answer is bigger than the number')
    elif number < r:
        print('Your answer is smaller than the number')
# 延伸： 印出猜了幾次
    print('This is your', count, 'times')


