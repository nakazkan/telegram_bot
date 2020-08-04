# чтение из файла с ударениями (4 номер)
f4 = open('words1.txt', 'r')
a = []  # массив с ударениями
for line in f4:
    a.append(line.split())
f4.close()

# чтение из файла с лексическими нормами (7 номер)
f7 = open('words2.txt', 'r')
b = []  # массив с лексическими нормами
for line in f7:
    b.append(line.split())
f7.close()

# чтение классификации из файла
cl = open("clas.txt", 'r')
c = []  # класификация ударений
for line in cl:
    c.append(line)
cl.close()
