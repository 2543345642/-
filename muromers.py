import os

way_1 = True
way_2 = True
way_3 = True
scene = "0"
key = ""
namee = input("введите герою имя? ")
if not namee: name = "Илья"
game = True


while game == True:
	os.system("cls")
	key = ""
	# Сцена у камня
	if way_1 or way_2 or way_3:
		os.system("cls")
		print(f"подъезжает {namee} к трем дорожкам, на перекрестке камень лежит, а на том камне написано: «Кто вправо поедет - тому убитым быть, кто влево поедет - тому богатым быть, а кто прямо поедет - тому женатым быть».")
		if way_1:
			print("1 - Поеду-ка я по той дорожке, где убитому быть. Умру в чистом поле, как славный богатырь!")
		if way_2:
			print("2 - Ну, поеду теперь, где женатому быть!")
		if way_3:
			print("3 - Ну, поеду теперь в дорожку, где богатому быть.")
		name_user = input("введите номер ответа и нажмите ENTER")
		key += name_user


		#разбойники
	if way_1 and key == "1":
		os.system("cls")
		print("текст с разбойниками")
		print("1 выбор")
		print("2 выбор")
		name_user = input("введите номер ответа и нажмите ENTER")
		key += name_user
		if way_1 and key == "11":
			os.system("cls")
			print("текст дорога конец 1 - хороший выбор")
			way_1 = False
		elif way_1 and key == "12":
			os.system("cls")
			print("текст дорога конец 2 - плохой выбор")
			key 

		#Жена
	if way_2 and key == "2":
		os.system("cls")
		print("текст с женой")
		print("1 выбор")
		print("2 выбор")
		name_user = input("введите номер ответа и нажмите ENTER")
		key += name_user
		if way_1 and key == "21":
			os.system("cls")
			print("текст дорога конец 3 - хороший выбор")
			way_1 = False
		elif way_1 and key == "22":
			os.system("cls")
			print("текст дорога конец 4 - плохой выбор")
		else:
			print("ads")

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
		else:
			print("ads")
	else:
		print("ads")
print("конец")		