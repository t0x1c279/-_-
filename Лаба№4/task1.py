import json
#Импортируем модуль json для работы с json файлами
# TODO решите задачу
file="input.json"#Указал имя файла

def task() -> float:#Объявляем функцию возвращающую числа с плавающей точкой
    # Читаем данные из JSON файла
    with open(file, 'r') as FILE:#Открываем файл для чтения
        list_slov = json.load(FILE)# Загружаем содержимое файла и преобразуем его в список словарей

    # Инициализируем сумму
    total_sum = 0.0

    # Проходим по каждому словарю в списке и
    for item in list_slov:
        # Проверяем, есть ли ключи "score" и "weight" в текущем словаре
        if "score" in item and "weight" in item:
            # Если есть, добавляем произведение score и weight к общей сумме
            total_sum += item["score"] * item["weight"]

    # Возвращаем сумму, округленную до 3 знаков после запятой
    return round(total_sum, 3)


if __name__=='__main__':
    print(task())#Вызываю функцию task и вывожу результат на экран
