
from book import Book


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, name, author, price, stock):
        if self.find_book(name) is not None:
            print("该图书已存在！")
            return

        book = Book(name, author, price, stock)
        self.books.append(book)
        print("添加成功！")

    def find_book(self, name):
        for book in self.books:
            if book.name == name:
                return book
        return None

    def update_book(self, name, author, price, stock):
        book = self.find_book(name)

        if book is None:
            print("未找到该图书！")
            return

        book.author = author
        book.price = price
        book.stock = stock
        print("修改成功！")

    def delete_book(self, name):
        book = self.find_book(name)

        if book is None:
            print("未找到该图书！")
            return

        self.books.remove(book)
        print("删除成功！")

    def show_book(self, name):
        book = self.find_book(name)

        if book is None:
            print("未找到该图书！")
            return

        book.show_info()

    def show_all(self):
        if not self.books:
            print("当前没有图书！")
            return

        for book in self.books:
            book.show_info()