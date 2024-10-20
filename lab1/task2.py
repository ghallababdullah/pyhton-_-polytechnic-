pages_in_the_book = 100 # TODO Найдите количество книг, которое можно разместить на дискете
lines_perpage=50
chars_line = 25
all_symbols = pages_in_the_book*lines_perpage*chars_line * 4
disk_size=1.44 * 1024 * 1024
books = disk_size // all_symbols
print("Количество книг, помещающихся на дискету:", int(books))
