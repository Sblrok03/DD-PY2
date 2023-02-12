class Book:
    """Базовый класс Book"""
    def __init__(self, author: str, name: str, price: int) -> None:
        """Инициализируем экземпляр класса Book со следующими атрибутами"""
        self.author = author
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """Возвращает информационную строку, что книга (экземпляр класса) была написана"""
        return f'Книга "{self.name}" была написана'

    def __repr__(self) -> str:
        """Возвращает валидную строку"""
        return f'{self.__class__.__name__}({self.author!r}, {self.name!r}, {self.price!r})'

    def get_price(self) -> int:
        """Возвращает стоимость книги"""
        return self.price


class ClassicalBook(Book): # наследуется от базового класса Book
    """Дочерний класс ClassicalBook"""
    def __init__(self, author: str, name: str, price: int, genre: str, discount: int) -> None:
        """Инициализируем экземпляр класса ClassicalPainting со следующими атрибутами"""
        super().__init__(author, name, price)
        self.genre = genre
        self.discount = discount

    def __repr__(self) -> str:
        """Возвращает валидную питоновскую строку класса, вставив которую обратно в код, позволяет создать
        экземпляр класса ClassicalBook"""
        return f'{self.__class__.__name__}({self.author!r},{self.name!r}, {self.price!r}, {self.genre!r}, ' \
               f'{self.discount!r})'

    def get_price(self) -> str:
        """Возвращает общую стоимость книги с учетом цены бумаги"""
        total = super().get_price() - self.discount
        return f'Итоговая цена книги: {total}'


class DigitalBook(Book): # наследуется от базового класса Book
    """Дочерний класс DigitalBook"""
    def __init__(self, author: str, name: str, price: int, technical_recources: str) -> None:
        """Инициализируем экземпляр класса DigitalBook со следующими атрибутами"""
        super().__init__(author, name, price)
        self.techrecources = technical_recources

    def __repr__(self) -> str:
        """Возвращает валидную питоновскую строку класса, вставив которую обратно в код, позволяет создать
                экземпляр класса DigitalBook"""
        return f'{self.__class__.__name__}({self.author!r},{self.name!r}, {self.price!r}, {self.techrecources!r})'

    def book_recources(self) -> str:
        """Возвращает строку с техническими ресурсами, которые были использованы при написании книги"""
        return f'Были использованы следующие ресурсы: {self.techrecources}'


if __name__ == "__main__":
    book_1 = ClassicalBook("Фёдор Достоевский", "Братья Карамазовы", 500, "Роман", 100)
    print(book_1)
    print(book_1.get_price(),'rub.')
    print(book_1.__repr__())

    book_2 = DigitalBook("Иванов Иван Иванович", "Статья", 300, "LaTeX")
    print(book_2)
    print(book_2.get_price(),'rub.', book_2.book_recources())
    print(book_2.__repr__())
    pass
