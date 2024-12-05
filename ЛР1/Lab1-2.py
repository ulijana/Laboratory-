disk = 1.44
page = 100
str = 50
sum = 25
byte_sym = 4

all_byte = (disk * 1024)*1024
byte_str = sum * byte_sym
byte_page = byte_str * str
bytes_book = byte_page * page
num_books = all_byte/bytes_book

print("Количество книг, помещающихся на дискету:", round(num_books))

