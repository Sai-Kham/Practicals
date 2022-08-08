import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

no_of_quick_picks = int(input("How many quick picks? "))
while no_of_quick_picks <= 0:
    print("Invalid number")
    no_of_quick_picks = int(input("How many quick picks? "))

for i in range(no_of_quick_picks):
    quick_pick = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in quick_pick:
            number = random.randint(MINIMUM, MAXIMUM)
        quick_pick.append(number)
    quick_pick.sort()
    print(quick_pick)












