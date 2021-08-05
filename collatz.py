import time

# the simplest math problem no one can solve

num = int(input("Pick a number: "))
print(num)

#rules : 3x + 1
#if number even : number / 2
#if number odd : (number * 3) + 1

while num >= 0:
    if num % 2 == 0:
        num = num / 2
        print(num)
        time.sleep(1)
    elif num % 2 != 0:
        num = (num *3) + 1
        print(num)
        time.sleep(1)

# pick any number and the number will stuck at 4,2,1
