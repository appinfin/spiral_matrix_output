from tkinter import *
import random
import time
runing = True
def run():
    
    def reboot():
        master.destroy()
    def generation_random_number():
        """Ф-ция генерирует список случайных целых чисел"""
        matrix_5x5=[]
        for i in range(5):
            random_list = list(random.randint(0, 100)+k for k in range(5))
            matrix_5x5.append(random_list)
            
        matrix_output(matrix_5x5)
        
        return matrix_5x5

    def spiral_matrix_otput(matrix_5x5):
        ## [1] строка 1 (А11 - А15)
        for i in range(5):
            time.sleep(1)
            v = matrix_5x5[0][i]
            ent_spiral = Entry(master, width = 3, bg = '#A80D05', font = ' Arial 12', justify = 'center')
            ent_spiral.insert(0, v)
            ent_spiral.grid(row = 0, column = i+6, padx = 2, pady = 2)
            ent_spiral.update()
        # [2] элементы А25, А35, А45
        for i in range(1,4): 
            time.sleep(1)
            v = matrix_5x5[i][4]
            ent_spiral = Entry(master, width = 3, bg = '#A80D05', font = ' Arial 12', justify = 'center')
            ent_spiral.insert(0, v)
            ent_spiral.grid(row = i, column = 10, padx = 2, pady = 2)
            ent_spiral.update()
        # [3] строка 5 (А55 - А51)
        for col in range (10,5,-1):
            time.sleep(1)
            ent_spiral = Entry(master, width = 3, bg = '#A80D05', font = ' Arial 12', justify = 'center')
            v = matrix_5x5[4][col-6] # строка 5
            ent_spiral.insert(0, v)
            ent_spiral.grid(row = 4, column = col, padx = 2, pady = 2)
            ent_spiral.update()
        # [4] элементы А41, А31, A21
        for i in range(3,0,-1): 
            time.sleep(1)
            v = matrix_5x5[i][0]
            ent_spiral = Entry(master, width = 3, bg = '#A80D05', font = ' Arial 12', justify = 'center')
            ent_spiral.insert(0, v)
            ent_spiral.grid(row = i, column = 6, padx = 2, pady = 2)
            ent_spiral.update()            
        # [5] строка 2 (А22 - А24)
        for i in range(1,4): 
            time.sleep(1)
            v = matrix_5x5[1][i]
            ent_spiral = Entry(master, width = 3, bg = '#DD7269', font = ' Arial 12', justify = 'center')
            ent_spiral.insert(0, v)
            ent_spiral.grid(row = 1, column = 6+i, padx = 2, pady = 2)
            ent_spiral.update()
        # [6] элементы А34, А44
        for i in range(2,4): 
            time.sleep(1)
            v = matrix_5x5[i][3]
            ent_spiral = Entry(master, width = 3, bg = '#DD7269', font = ' Arial 12', justify = 'center')
            ent_spiral.insert(0, v)
            ent_spiral.grid(row = i, column = 9, padx = 2, pady = 2)
            ent_spiral.update()   
        # [7] строка 5 (А43 - А42)
        for i in range (8,6,-1):
            time.sleep(1)
            ent_spiral = Entry(master, width = 3, bg = '#DD7269', font = ' Arial 12', justify = 'center')
            v = matrix_5x5[3][i-6] # строка 5
            ent_spiral.insert(0, v)
            ent_spiral.grid(row = 3, column = i, padx = 2, pady = 2)
            ent_spiral.update()
        # A32
        time.sleep(1)
        ent_spiral = Entry(master, width = 3, bg = '#DD7269', font = ' Arial 12', justify = 'center')
        v = matrix_5x5[2][1] # строка 5
        ent_spiral.insert(0, v)
        ent_spiral.grid(row = 2, column = 7, padx = 2, pady = 2)
        ent_spiral.update()
        # A33
        time.sleep(1)
        ent_spiral = Entry(master, width = 3, bg = '#DBB6B3', font = ' Arial 12', justify = 'center')
        v = matrix_5x5[2][2] # строка 5
        ent_spiral.insert(0, v)
        ent_spiral.grid(row = 2, column = 8, padx = 2, pady = 2)
        ent_spiral.update()
            
    def matrix_output(matrix_5x5):

        for row in range(5):
            for col in range(5):
                text_value = matrix_5x5[row][col]
                ent_matrix_5x5 = Entry(master, width = 3, font = ' Arial 12', justify = 'center')
                ent_matrix_5x5.insert(0, text_value)
                ent_matrix_5x5.grid(row = row, column = col, padx = 2, pady = 2)

    master = Tk()
    master.title('Spiral Matrix output')
    master.geometry('450x153+50+50')
    master.resizable(False, False)
    master.iconify()
    master.update()
    master.deiconify()
    
    for row in range(5):
        for col in range(6,11):
            ent_spiral = Entry(master, width = 3, font = ' Arial 12', bg = '#ccc', justify = 'center')
            ent_spiral.grid(row = row, column = col, padx = 2, pady = 2)

    but = Button(master, text = 'Generation matrix', command = reboot)
    but.grid(row = 5, column = 0, columnspan = 5)

    but = Button(master, text = 'Display items >>>', command = lambda: spiral_matrix_otput(matrix_5x5))
    but.focus_set()
    but.grid(row = 2, column = 5)

    but = Button(master, text = 'Exit', command = quit)
    but.grid(row = 5, column = 6, columnspan = 5)
    

    matrix_5x5 = generation_random_number()

    master.mainloop()
while runing:
    run()
