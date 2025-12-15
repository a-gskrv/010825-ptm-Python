"""01 Фигуры и площади

Создайте абстрактный класс Shape.
В классе должен быть метод area(), который возвращает площадь фигуры.
Реализуйте два класса:
- Circle, который принимает радиус.
- Rectangle, который принимает ширину и высоту.
"""



class Shape():
    pass


class Circle():
    pass


class Rectangle(Shape):
    pass


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print("Площадь круга:", circle.area())
    print("Площадь прямоугольника:", rectangle.area())


    # Площадь круга: 78.53981633974483
    # Площадь прямоугольника: 24
