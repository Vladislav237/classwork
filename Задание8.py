#Задание 1
def upper():
    a = input()
    for char in a:
        if char.isupper():
            print(char)
upper()
#Задание 2
def punct():
    str = input()
    str1 = str.count("!")
    str1 += str.count("?")
    str1 += str.count(".")
    str1 += str.count(",")
    str1 += str.count("(")
    str1 += str.count(")")
    print(str1)
punct()
