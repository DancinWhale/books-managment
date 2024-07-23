from library_managment import LibraryManagement


class App:
    @classmethod
    def start_app(cls):  # Взаимодействие с пользователем
        data_error_message = "XXX Проверьте корректность данных и повторите попытку XXX"  # Стандартная ошибка введенных данных
        print("=====================================================\n"
              "     Добро пожаловать в управление библиотекой       \n"
              "=====================================================")
        while True:  # Меню, где пользователь выбирает действие
            choice = input("\n<======== Меню ========>\n"
                           "1) Добавить книгу\n"
                           "2) Удалить книгу\n"
                           "3) Найти книгу по названию, автору или году выпуска\n"
                           "4) Отобразить все книги\n"
                           "5) Изменить статус книги\n"
                           "6) Выйти\n"
                           "Введите номер вашего действия >> ")
            match choice:

                case "1":
                    print("\n----------- Добавление новой книги -----------")
                    try:
                        new_book_title = input("Ведите название книги >> ")
                        new_book_author = input("Ведите автора книги >> ")
                        new_book_year = int(input("Ведите год издания книги >> "))
                    except ValueError:
                        print(data_error_message)
                        continue
                    adding_new_book = LibraryManagement.add_book(new_book_title, new_book_author, new_book_year)
                    if adding_new_book:
                        print(">>> Книга успешно была добавлена!")
                    else:
                        print(">>> Произошла ошибка при добавлении книги, попробуйте еще раз.")

                case "2":
                    print("\n----------- Удаление книги -----------")
                    try:
                        delete_book_id = int(input("Введите id книги >> "))
                    except:
                        print(data_error_message)
                        continue
                    deleting_book = LibraryManagement.delete_book(delete_book_id)
                    if deleting_book:
                        print(">>> Книга успешно была удалена!")
                    else:
                        print(">>> Не удалось найти книгу по данному id.")

                case "3":
                    print("\n----------- Вывод определенных книг -----------\n"
                          "|Введите данные для поиска необходимых книг.\n"
                          "|Вы можете пропускать поля, просто нажав 'Enter'.")
                    title_search = input("Введите название книги >> ")
                    author_search = input("Введите автора книги >> ")
                    year_search = input("Введите год издания книги >> ")
                    if year_search != "":
                        try:
                            check_int = int(year_search)  # Проверка на то, является ли введенный год числом
                        except:
                            print(data_error_message)
                            continue
                    found_books = LibraryManagement.find_book(title_search, author_search, year_search)

                    print("\n----------- Список подходящих книг ----------+\n"
                          "                                            |\n"
                          "                                            |")
                    for book in found_books:
                        print(
                            " id Книги: " + str(book["id"]) + "\n",
                            "Наименование книги: " + str(book["title"]) + "\n",
                            "Автор: " + str(book["author"]) + "\n",
                            "Год написания: " + str(book["year"]) + "\n",
                            "Статус: " + str(book["status"]) + "\n\n",
                            )
                    print("                                            |\n"
                          "                                            |\n"
                          "--------------------------------------------+\n")

                case "4":
                    books = LibraryManagement.read_file()  # Все найденные книги
                    if len(books) != 0:
                        print("\n----------- Список всех книг ----------+\n"
                              "                                       |\n"
                              "                                       |")
                        for book in books:
                            print(
                                " id Книги: " + str(book["id"]) + "\n",
                                "Наименование книги: " + str(book["title"]) + "\n",
                                "Автор: " + str(book["author"]) + "\n",
                                "Год написания: " + str(book["year"]) + "\n",
                                "Статус: " + str(book["status"]) + "\n\n",
                                )
                        print("                                       |\n"
                              "                                       |\n"
                              "---------------------------------------+\n")
                    else:
                        print("\n!!!-------- Список книг пуст --------!!!\n")

                case "5":
                    print("\n----------- Изменение статуса книги -----------")
                    try:
                        change_book_id = int(input("Введите id книги >> "))
                    except:
                        print("XXX Проверьте корректность введенного id и повторите попытку XXX")
                        continue
                    changing_book = LibraryManagement.change_status(change_book_id)
                    if changing_book:
                        print(">>> Статус книги успешно изменен!")
                    else:
                        print("!!! Не удалось найти книгу по данному id !!!")

                case "6":
                    break
                case _:
                    print("\nXXX Некорректное действие, повторите свой выбор. XXX")


if __name__ == "__main__":  # Запускает приложение
    App.start_app()
