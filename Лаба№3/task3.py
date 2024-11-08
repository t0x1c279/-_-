# TODO  Напишите функцию count_letters
def count_letters(txt):
    count=0
    letters={}
    for x in txt:
        small_letter=x.lower()
        if small_letter.isalpha():
            if small_letter in letters:
                letters[small_letter] += 1
            else:
                letters[small_letter] = 1
    return letters
# TODO Напишите функцию calculate_frequency
def calculate_frequency(letters,total):
    frequency={}
    total= sum(letters.values())
    for l,c in letters.items():
        frequency[l]=round(c/total,2)
    return frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
letters=count_letters(main_str)
total = sum(letters.values())
frequency=calculate_frequency(letters,total)
# TODO Распечатайте в столбик букву и её частоту в тексте
for i,j in frequency.items():
    print(f"{i}: {j:.2f}")