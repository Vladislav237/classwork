import random
print('Input first index matrix: ')
x = int(input())
print('Input second index matrix: ')
y = int(input())
def creatArray():
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(random.randint(-3,3))


    return array
matrix=creatArray()

result = []
print(matrix)
for i in matrix:
    result.append(min(i))
print(result)
