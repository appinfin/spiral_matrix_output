import random

def generation_random_number():
    """Ф-ция генерирует список случайных целых чисел"""
    matrix_5x5=[]
    for i in range(5):
        random_list = list(random.randint(0, 100)+k for k in range(5))
        print(random_list)
        matrix_5x5.append(random_list)
        
    return matrix_5x5

matrix_5x5 = generation_random_number()
print('Вывод элементов матрицы по спирали (по часовой стрелке):')

print(matrix_5x5[0][0:]) # строка 1 (А11 - А15)

for i in range(1,4): # элементы А25, А35, А45
    print(matrix_5x5[i][-1])
    
print(matrix_5x5[4][::-1]) # строка 5

for i in range(3,1,-1):
    print(matrix_5x5[i][0])

print(matrix_5x5[1][0:4])

print(matrix_5x5[2][-2])

l=[]
for i in matrix_5x5[3][1:4].__reversed__():
    l.append(i)
    
print(l)

print(matrix_5x5[2][1:3])
