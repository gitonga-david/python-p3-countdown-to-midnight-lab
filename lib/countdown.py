# your code goes here!
import time


def countdown(number):
    while number > 0:
        print(f"{number} SECOND(S)!")
        number -=1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(number):
    for i in range(number, 0, -1):
        print(f"{i} SECOND(S)!")
        time.sleep(1)
    print("HAPPY NEW YEAR!")

countdown_with_sleep(5)

