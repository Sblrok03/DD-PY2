import doctest
class Notebook:
    def __init__(self, notebook_type: str, number_of_pages: int):
        """"
        Создание и подготовка к работе объекта "Тетрадь"
        :param notebook_type: Тип тетради
        :param number_of_pages: Количество страниц

        Пример:
        >>> notebook = Notebook("В линию", 18) # инициализация экземпляра класса
        """
        if not isinstance(notebook_type, str):
            raise TypeError("Тип тетради должен быть типа str")
        self.notebook_type = notebook_type

        if not isinstance(number_of_pages, int):
            raise TypeError("Число страниц должно быть типа int")
        if number_of_pages < 0:
            raise  ValueError("Число страниц не может быть отрицательным числом")
        self.number_of_pages = number_of_pages
    def add_pages(self, sheets: int):
        """
        Добавление страниц в тетрадь.
        :param sheets: Количество добавляемых страниц
        """
        if not isinstance(sheets, int):
            raise TypeError("Число страниц должно быть типа int")
        if sheets < 0:
            raise ValueError("Число страниц не может быть отрицательным числом")
        ...
    def is_line_notebook_type(self) -> bool:
        """
        Функция которая проверяет является ли тетрадь тетрадью в линию
        :return: является ли тетрадь тетрадью в линию
        """
        ...

if __name__ == "__main__":
    notebook1 = Notebook("В клетку", 20)
    print(notebook1.notebook_type, notebook1.number_of_pages)
    doctest.testmod()
    #help(Notebook)
    pass

class Table:
    def __init__(self, table_material: str, height: int):
        """"
        Создание и подготовка к работе объекта "Стол"
        :param table_material: Материал стола
        :param height: Высота

        Пример:
        >>> table = Table("Деревянный", 60) # инициализация экземпляра класса
        """
        if not isinstance(table_material, str):
            raise TypeError("Материал стола должен быть типа str")
        self.table_material = table_material

        if not isinstance(height, (float, int)):
            raise TypeError("Высота стола должна быть int или float")
        if height < 0:
            raise  ValueError("Высота не может быть отрицательным числом")
        self.height = height
    def add_weight(self, weight: int):
        """
        Увеличение веса стола.
        :param weight: Количество добавляемого веса
        """
        if not isinstance(weight, int):
            raise TypeError("Количество добавляемого веса должно быть типа int или float")
        if weight < 0:
            raise ValueError("Количество добавляемого веса не может быть отрицательным числом")
        ...
    def is_table_wood_type(self) -> bool:
        """
        Функция которая проверяет сделан ли стол из дерева.
        :return: является ли стол деревянным
        """
        ...

if __name__ == "__main__":
    table1 = Table("Деревянный", 55)
    print(table1.table_material, table1.height)
    doctest.testmod()
    #help(Notebook)
    pass

class Tree:
    def __init__(self, type_of_tree: str, age: int):
        """"
        Создание и подготовка к работе объекта "Дерево"
        :param table_material: Тип дерева
        :param height: Возраст

        Пример:
        >>> table = Table("Ель", 20) # инициализация экземпляра класса
        """
        if not isinstance(type_of_tree, str):
            raise TypeError("Тип дерева должен быть типа str")
        self.type_of_tree = type_of_tree

        if not isinstance(age, (float, int)):
            raise TypeError("Возраст дерева должен быть int или float")
        if age < 0:
            raise  ValueError("Возраст дерева не может быть отрицательным числом")
        self.age = age
    def add_decorations(self, decorations: int):
        """
        Украшение дерева.
        :param decorations: Количество декораций
        """
        if not isinstance(decorations, int):
            raise TypeError("Количество добавляемых декораций должно быть типа int")
        if decorations < 0:
            raise ValueError("Количество добавляемых декораций не может быть отрицательным числом")
        ...
    def is_tree_spruce_type(self) -> bool:
        """
        Функция которая проверяет является ли дерево елью.
        :return: является ли дерево елью
        """
        ...

if __name__ == "__main__":
    tree1 = Tree("Сосна", 55)
    print(tree1.type_of_tree, tree1.age)
    doctest.testmod()
    #help(Notebook)
    pass
