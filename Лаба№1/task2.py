# TODO Найдите количество книг, которое можно разместить на дискете
I=1.44*(2**23)
count_pages=100
count_lines=50
count_symbols=25
kod=4*8
print("Количество книг, помещающихся на дискету:", round(I/round(count_symbols*count_lines*count_pages*kod)))
