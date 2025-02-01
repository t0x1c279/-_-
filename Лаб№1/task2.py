from task_1 import Car,Book,Smartphone

 # TODO: импортируйте классы, созданные в ходе выполнения прошлого задания
if __name__ == "__main__":
    Car_1=Car('Nissan','Terrano',2019)
    Book_1=Book('Оно','Стивен Кинг',1184)
    Smartphone_1=Smartphone('Redmi Note 12 Pro', 'Xiaomi', 2023, 5000, 5.53)
 # TODO: инстанцировать все описанные классы, создав три объекта.C()

    try:
        Car_1.get_age("32323")
     # TODO: вызвать метод с некорректными аргументами(b)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        Book_1.read("bb3")
     # TODO: вызвать метод с некорректными аргументами(a)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        Smartphone_1.time_of_using_phone(3)
     # TODO: вызвать метод с некорректными аргументами(a)
    except ValueError:
        print('Ошибка: неправильные данные')