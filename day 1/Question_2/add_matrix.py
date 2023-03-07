import numpy as np

def matx_1():
    rows = int(input("Enter no. of Rows for 1st Matrix... "))
    columns = int(input("Enter no. of Columns for 1st Matrix... "))

    print("Enter the elements of 1st Matrix in single line seperated by space ")

    elements = list(map(int,input().split()))
    global matrix_1
    matrix_1 = np.array(elements).reshape(rows,columns)
    print(matrix_1)

def matx_2():
    rows = int(input("Enter no. of Rows for 2nd Matrix... "))
    columns = int(input("Enter no. of Columns for 2nd Matrix... "))

    print("Enter the elements of 2nd Matrix in single line seperated by space ")

    elements = list(map(int,input().split()))
    global matrix_2
    matrix_2 = np.array(elements).reshape(rows,columns)
    print(matrix_2)

matx_1()
matx_2()
print(np.add(matrix_1,matrix_2))