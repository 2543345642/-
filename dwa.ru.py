import random

user = random.randint(1, 6)
cpu = random.randint(1, 6)
print("игрок выбросил", user)
print("cpu выбросил", cpu)
if cpu > user:
    print("cpu выиграл")
else:
    if cpu<user:
        print("победил игрок")
    else:
        print("ничья")

