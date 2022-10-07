import os
import random
way_1 = True
way_2 = True
way_3 = True
user_hp = 100
enemy_hp = 100
scene = "0"
key = ""
s = 5
user_name = input("введите имя героя")
if not user_name: name = "Илья"
game = True	

while game == True:
	os.system("cls")
	key = ""
	# Сцена у камня
	if way_1 or way_2 or way_3:
		os.system("cls")
		print(f"подъезжает {user_name} к трем дорожкам, на перекрестке камень лежит, а на том камне написано: «Кто вправо поедет - тому убитым быть, кто влево поедет - тому богатым быть, а кто прямо поедет - тому женатым быть».")
		if way_1:
			print("1 - Поеду-ка я по той дорожке, где убитому быть. Умру в чистом поле, как славный богатырь!")
		if way_2:
			print("2 - Ну, поеду теперь, где женатому быть!")
		if way_3:
			print("3 - Ну, поеду теперь в дорожку, где богатому быть.")

		number = input("введите номер ответа и нажмите ENTER")
		if number == "1" and way_1:
			key += number
		elif number == "2" and way_2:
			key += number
		elif number == "3" and way_3:
			key += number




	if way_1 and key == "1":
		os.system("cls")

		enemy_name = "Жран Борзый"

		input("сражайтесь с честью, один на один, разбойник хочет сражаться в честном бою. нажмите 1 потом enter, или умри, написав что-то другое")
		print("сражение")
		input("enter - дальше")

		while user_hp > 0 and enemy_hp > 0:
		    os.system("cls")

		    user_attack = random.randint(1, 10)
		    enemy_hp -= user_attack
		    print(f"{user_name} ударил {enemy_name} на {user_attack} и оставил {enemy_hp}")

		    if user_hp < 0: 
		        break
		    
		    enemy_attack = random.randint(1, 10)
		    user_hp -= enemy_attack
		    print(f"{enemy_name} ударил {user_name} на {enemy_attack} и оставил {user_hp}")
		    input("enter - дальше")

		    if enemy_hp < 0: 
		        break


		if user_hp > 0: 
		    print(f"поражение")
		    game = False


		else:
		    print(f"победил {user_name}")
		    

	#Жена
	if way_2 and key == "2":
		os.system("cls")
		while s == True:
			print("угадай число от 1 до 100")
			secret = random.randint(1, 100)
			user_choice = int(input("введите задуманное число"))
			if user_choice == secret:
				Print("победил")
			elif user_choice < secret:
				print("маловато")
				s =- 1
			else:
				print("многовато")
				s =- 1
				print(f"осталось {s} попыток")


		#богатый
	if way_3 and key == "3":
		os.system("cls")
		print("текст с богадством")
		print("1 выбор")
		print("2 выбор")
		name_user = input("введите номер ответа и нажмите ENTER")
		key += name_user
		if way_1 and key == "31":
			os.system("cls")
			print("текст дорога конец 5 - хороший выбор")
			way_1 = False
		elif way_1 and key == "32":
			os.system("cls")
			print("текст дорога конец 6 - плохой выбор")