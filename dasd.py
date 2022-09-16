import random
print("1=камень 2=ножницы 3=бумага ")

user = int(input("введите число от 1 до 3 "))
if user == 1:
    print("игрок показал камень")
elif user == 2:
    print("игрок показал ножницы")
elif user == 3:
    print("игрок показал бумагу")
cpu = random.randint(1, 3)
if cpu == 1:
    print ("пк показал камень")
elif cpu == 2:
    print("игрок показал ножницы")
elif cpu == 3:
    print("игрок показал бумагу")

if user == cpu:
    print("ничья")
    
#победы игрока и победы cpu
else:
    if user == 1 and cpu == 2:
        print ("игрок победил")
    elif user == 2 and cpu == 3:
        Print("игрок победил")
    elif user == 3 and cpu == 1:
        print("игрок победил")
        
        
    #победы компа
    else:
        print("комп победил")
