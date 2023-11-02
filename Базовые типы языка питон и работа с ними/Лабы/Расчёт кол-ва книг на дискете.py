# TODO Найдите количество книг, которое можно разместить на дискете
count = 1.44 #мегабайт
colvo = 100 #Страниц
strok = 50 #строк
symbol = 25 #символов
for_1_sym = 4 #байта

count_1_book = colvo*strok*symbol*for_1_sym

count_1_book /=(1024**2)

colvo_in_dysk= count // count_1_book
print("Количество книг, помещающихся на дискету:", round(colvo_in_dysk))
