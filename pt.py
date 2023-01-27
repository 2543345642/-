LIBRARY = [

    {
        "название": "Тестовая книга",
        "автор": "Каыфавф",
        "год": 1232
    }

]


def add_book():
    print("Добавляем книгу ")
    title = input("Введите название произведения:")
    if not title:
        print("нет названия!!! Введите ещё раз название")
        return

    author = input("Введите имя автора")
    if not author:
        print("нет имя автора!!! Введите ещё раз имя автора")
        return

    year = input("Введите год издания:")
    if not year:
        print("нет года!!! Введите ещё раз год")
        return
    if year.isdigit():
        year = int(year)
    else:
        print("Год должен быть числом!!! Введите ещё раз год")
        return
    book = {"название": title,
            "автор": author,
            "год": year,
    }

    LIBRARY.append(book)
    print(f"Книга: {title}; автор: {author}; год: {year}, успешно добавлена в библеотеку")


def show_library():
    for num, book in enumerate(LIBRARY, 1):
        print("номер на полке", num)
        print("название", book["название"])
        print("автор", book["автор"])
        print("год", book["год"])


show_library()


"""
def Ordinal number():
    input("Введите порядковый номер. Счёт начинается от 0")

    print("ищем книгу")
"""