# TODO Напишите функцию find_common_participants
def find_common_participants(a,b,x=','):
    participants_first=set(a.split(x))
    participants_second=set(b.split(x))
    intersection_participants=participants_first.intersection(participants_second)
    return sorted (intersection_participants)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
obshie=find_common_participants(participants_first_group,participants_second_group,'  ')
print(obshie)