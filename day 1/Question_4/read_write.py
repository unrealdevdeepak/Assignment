import pandas as pd
import os

def Write_data():
    data = []
    while True:
        Name = input("Enter name (or 'q' to quit): ")
        if Name == 'q':
            break
        Roll_No = (int(input("Enter Roll No... ")))
        Age = int(input("Enter age: "))
        Gender = (input("Enter Gender"))
        City = input("Enter city: ")
        data.append((Name,Roll_No, Age,Gender, City))

    df = pd.DataFrame(data, columns=['Name','Roll_No', 'Age','Gender' ,'City'])

    df.to_excel('record.xlsx', index=False)

    print("Data written to Excel file: record.xlsx")

    menu()

def read_xls():
    data = pd.read_excel('record.xlsx','Sheet1')
    print(data)
    menu()
    

def menu():
    option=int(input('''
        ##### Write And Read Application in Excel file using Pandas #####
        1) Write Operation
        2) Read Operation
        3) Exit
        Choose from 1 - 3 options....... '''))

    if option== 1 :
        Write_data()
    elif option== 2:
        if os.path.isfile('record.xlsx'):
            read_xls()
        else:
            print("First create the file")
            menu()
    elif option== 3 :
        exit()
    else:
        print("Choose Correct Operation")
        menu()

menu()

