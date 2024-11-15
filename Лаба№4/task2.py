# TODO импортировать необходимые молули
import csv  # Импортируем модуль для работы с CSV файлами
import json  # Импортируем модуль для работы с JSON файлами

INPUT_FILENAME = "input.csv"#Имя входного файла
OUTPUT_FILENAME = "output.json"#Имя выходного файла


def task() -> None:#Определяем функцию task, которая не возвращает значения
    #Открываем CSV файл для чтения
    with open(INPUT_FILENAME, 'r') as input_file:
        READER = csv.DictReader(input_file)  # Читаем CSV как словарь, т.е каждая строка будет представлена как словарь
        list_str=[ROW for ROW in READER]# Создаем список словарей из строк CSV файла
    # TODO считать содержимое csv файла
    with open(OUTPUT_FILENAME, 'w') as output_file: #Открываем JSON файл для записи
        # Сериализуем список словарей в JSON формат и записываем в файл
        json.dump(list_str, output_file, indent=4,ensure_ascii=False)# TODO Сериализовать в файл с отступами равными 4
#indent=4 отвечает за отступ в 4 пробела в JSON файле(делается это для удобного чтения)
#ensure_ascii=False- управляет тем, как обрабатываются не-ASCII символы при сериализации объектов в JSON формат
if __name__ == '__main__':
    task()#Вызов функции task
    # Открываем выходной JSON файл для чтения и вывода его содержимого на экран
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f: #Читаем каждую строчку из файла
            print(line, end="")#И печатаем
