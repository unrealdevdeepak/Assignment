import os
import write_d as wr
import read_d as re


def menu():
    option=int(input('''
        ##### Write And Read App #####
        1) Write Operation
        2) Read Operation
        3) Exit
        Choose from 1 - 3 options....... '''))

    if option == 1 :
        wr.write_f()
    elif option== 2:
        if os.path.isfile('data.txt'):
            re.read_f()
        else:
            print("First create the file")
            menu()
    elif option== 3 :
        exit()
    else:
        print("Choose Correct Operation")
        menu()

menu()



   


