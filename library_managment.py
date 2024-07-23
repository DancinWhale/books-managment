import json


class LibraryManagement:
    @classmethod
    def read_file(cls):  # Функция для считывания json файла и возврата всех имеющихся книг
        try:
            with open("books.json", "r+") as jFile:
                json_obj = json.load(jFile)
            return json_obj
        except:  # Если файла нет, то отдается пустой массив
            return []

    @classmethod
    def update_file(cls, data):  # Функция обновления файла
        with open("books.json", "w+") as jFile:  # Обновление файла
            jFile.write(json.dumps(data, indent=4))
        return True

    @classmethod
    def add_book(cls, title, author, year):
        json_obj = cls.read_file()  # Получаем все книги для вычисления уникального id

        try:
            # Заполнение данных для добавления новой книги
            new_book_id = max([i['id'] for i in json_obj]) + 1 if len(json_obj) != 0 else 0
            new_book_title = title
            new_book_author = author
            new_book_year = year
            res_object = {
                "id": new_book_id,
                "title": new_book_title,
                "author": new_book_author,
                "year": new_book_year,
                "status": "In stock"
            }
            json_obj.append(res_object)  # Добавление новой книги

            cls.update_file(json_obj)  # Обновление файла
            return True
        except:
            return False  # Возвращаем False, если произошла ошибка

    @classmethod
    def delete_book(cls, book_id):
        json_obj = cls.read_file()  # Считываем все книги
        res_object = []
        flag = False
        for book in json_obj:  # Заполняем измененный массив без удаляемой книги
            if book["id"] == book_id:
                flag = True  # Флаг о том, что книга есть в списке
                continue
            else:
                res_object.append(book)  # Добавляем неудаляемую книгу в измененный список
        if flag:
            cls.update_file(res_object)  # Обновление файла
            return flag
        else:
            return flag  # Возвращается, если не найдено нужной нам книги

    @classmethod
    def find_book(cls, title, author, year):
        json_obj = cls.read_file()  # Загружаем данные
        match_books = []  # Заготавливаем переменную для подходящих книг
        match_parameters = sum([1 if i != "" else 0 for i in [title, author, year]])  # Смотрим сколько должно быть совпадений
        for book in json_obj:
            count_parameters = 0  # Переменная для подсчета
            if title != "" and title == book["title"]:
                count_parameters += 1
            if author != "" and author == book["author"]:
                count_parameters += 1
            if year != "" and int(year) == book["year"]:
                count_parameters += 1
            if count_parameters == match_parameters:  # Если совпало необходимое количество параметров, то добавляем книгу в список
                match_books.append(book)
        return match_books

    @classmethod
    def change_status(cls, book_id):
        json_obj = cls.read_file()
        flag = False
        for book in range(len(json_obj)):  # Заполняем измененный массив без удаляемой книги
            if json_obj[book]["id"] == book_id:
                if json_obj[book]["status"] == "In stock":
                    json_obj[book]["status"] = "Out of stock"
                else:
                    json_obj[book]["status"] = "In stock"
                flag = True
            else:
                continue
        if flag:
            cls.update_file(json_obj)  # Обновление файла
            return flag
        else:
            return flag  # Возвращается, если не найдено нужной нам книги
