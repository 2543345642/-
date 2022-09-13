import random
user_turn = input("введите камень(1) ножницы(2) и бумага(3)")
computer_turn= random.randint(1, 3)
print("игрок показал", user_turn)
print("игрок показал", computer_turn)
if user_turn == computer_turn:
    print("ничья!")
elif user_turn == 1 and computer_turn == 2:
    print("игрок победил")
elif user_turn == 1 and computer_turn == 3:
    print("пк выиграл")
elif user_turn == 2 and computer_turn == 1:
    print("пк выиграл")
elif user_turn == 2 and computer_turn == 2:
    print("игрок выиграл")
elif user_turn == 3 and computer_turn == 2:
    print("игрок выиграл")
elif user_turn == 3 and computer_turn == 1:
    print("игрок выиграл")
