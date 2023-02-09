import socket
import threading
import os
from pywebcopy import save_webpage

def main_menu():
    while True:
        print("Choose program: \n1 - DDoS\n2 - Web Copy\n3 - Port Scanner\n4 - Get ip\n5 - exit")
        choice = int(input('Choice: '))
        if choice == 1:
            exec(open("DDoS.py").read())
            break
        if choice == 2:
            exec(open("Copy_URL.py").read())
            break
        if choice == 3:
            exec(open("Port_Scan.py").read())
            break

        if choice == 4:
            exec(open("Get_IP.py").read())
            break
        if choice == 5:
            print('Goodbye!')
            break
        else:
            print('Enter the number of program!!!')


if __name__ == "__main__":
    main_menu()