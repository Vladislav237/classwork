#Задание 1
file = open("S:\\Группы\\ИБС215 Алгоритмизация\\Илюшин\\output.txt", "w")
file.write("conten")
# Задание 2
file=open("S:\\Группы\\ИБС215 Алгоритмизация\\Илюшин\\input.txt")
content=file.read()
file.close()
file = open("S:\\Группы\\ИБС215 Алгоритмизация\\Илюшин\\output.txt", "a")
file.write(content)
file.write("<copy>")
file.close()

# Задание 3
from datetime import datetime
file = open("S:\\Группы\\ИБС215 Алгоритмизация\\Илюшин\\logs.txt", "x")
def a(text):
    file = open("S:\\Группы\\ИБС215 Алгоритмизация\\Илюшин\\logs.txt", "a")
    date=str(datetime.now())
    file.write(date)
    file.write(text)

while True:
    a(input())
  # Задание 4
file = open('S:\\Группы\\ИБС215 Алгоритмизация\\III Сложные задания\\data.txt')
mylist = file.readlines()
mylist=str(mylist)
file=mylist.split("\n")
count=mylist.count("John")
print(count)
# Задание 5
with open('S:\\Группы\\ИБС215 Алгоритмизация\\III Сложные задания\\encrypt_mess.txt') as file:
    content=file.read()
a={'б':'a', 'в':'б', 'г':'в', 'д':'г', 'е':'д', 'ё':'е', 'ж':'ё', 'з':'ж', 'и':'з', 'й':'и', 'к':'й', 'л':'к',
   'м':'л', 'н':'м', 'о':'н', 'п':'о', 'р':'п', 'с':'р', 'т':'с', 'у':'т', 'ф':'у', 'х':'ф', 'ц':'х', 'ч':'ц',
   'ш':'ч', 'щ':'ш', 'ъ':'щ', 'ы':'ъ', 'ь':'ы', 'э':'ь', 'ю':'э', 'я':'ю', 'а':'я', 'О':'1', 'Д':'2', 'Т':'3',
   'Ч':'4', 'П':'5', 'Ш':'6', 'С':'7', 'В':'8', 'Е':'9', 'Я':'0',
   '/':'.', '_':'!', ',':' ', ' ':',', '^':':', '*':'\n'}
for i in content:
    if i in a:
        print(a.get(i),end='')
# Задание 6
inputTXT=input("Текст> ")
Save=input("Сохранить?> ")
if Save== 'yes':
    inputFileName=input('Название файла> ')
    file = open(inputFileName, "w")
    file.write(inputTXT)
    file.close()
else:
    print("no save")
