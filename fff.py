import random
found_mushrooms = 0 # найдены грибы
space = 100 # осталось место
spray = 20 #Спрей
a = 1 #ключ 1

rl = 1 #ключ
while a > 0:  # роверим грибы и спрей
    

    if spray and space > 0 and found_mushrooms < 100 :
        found_mushrooms += random.randint(0, 20) #Грибы собирать
        spray -= 1
        space = 100
        space -= found_mushrooms
        print("поиск грибов...")
        print("найдено: ", found_mushrooms, "грибов")
        print("осталось места в корзине: ", space)
        print("корзина: ", found_mushrooms, "/ 100")
        print("осталось спреев: ", spray)
        input()

    elif space < 0:
        space = 0
        found_mushrooms = 100
        print("поиск грибов...")
        print("найдено: ", found_mushrooms, "грибов")
        print("осталось места в корзине: ", space)
        print("корзина: ", found_mushrooms, "/ 100")
        print("осталось спреев: ", spray)
        input("Питонов ушёл с полной корзиной")
        a -= 1

    elif spray < 0:
        print("поиск грибов...")
        print("найдено: ", found_mushrooms, "грибов")
        print("осталось места в корзине: ", space)
        print("корзина: ", found_mushrooms, "/ 100")
        print("осталось спреев: ", spray)
        input("У Питонова закончился спрей. Пора сваливать")
        a -= 1

    else:
        print("ошибка")

