import os
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


def delete_book() -> None:
    """
    Удаляет книгу или выводит сообщение, что нету такой книги.


    """
    #нету книг
    if not LIBRARY:
        print("В библеотеке нету книг!!!")
        return
    book_number = input("Введите номер(ЦЫФРУ) книги, которую нужно удалить")

    #нету чисел
    if not book_number.isdigit():
        print("Ошибка!Номер книги должен быть числом")
        return
    book_number = int(book_number)
    if book_number <= 0:
        print("Ошибка! Номер должен быть больше 0")
        return
    if book_number > len(LIBRARY):
        print("Ошибка! Номер СЛИШКОМ большой")
    idx = book_number - 1
    book_name = LIBRARY[idx]["название"]
    print("Книга успешна удалена", book_name)
    LIBRARY.pop(book_number - 1)


def search_by_number() -> None:
    if not LIBRARY:
        print("В библеотеке нету книг!!!")
        return
    book_number = input("Введите номер(ЦЫФРУ) книги, которую нужно удалить")
    if not book_number.isdigit():
        print("Ошибка!Номер книги должен быть числом")
        return
    book_number = int(book_number)
    if book_number <= 0:
        print("Ошибка! Номер должен быть больше 0")
        return
    if book_number > len(LIBRARY):
        print("Ошибка! Номер СЛИШКОМ большой")
    idx = book_number - 1
    book = LIBRARY[idx]
    print("номер на полке", idx + 1)
    print("название", book["название"])
    print("автор", book["автор"])
    print("год", book["год"])

print("Здраствуйте")


def menu():
    while True:
        options = [
            ["Показать все книги", lambda: show_library()],
            ["показать книги по номеру", lambda: search_by_number("год")],
            ["добавить книгу", lambda: add_book()],
            ["удалить книгу", lambda: delete_book()],
        ]

        for num, option in enumerate(options, 1):
            print(f"{num}. {option[0]}")

        user_option = input("введите номер варианта и нажмите ENTER:")
        idx = int(user_option) - 1
        options[idx][1]()


menu()
