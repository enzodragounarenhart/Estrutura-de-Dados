import random

listaNum = []
randomlist = []
option = 0

def int_list(list):
    list_num = []
    for num in list:
        try:
            number = int(num)
            list_num.append(number)
        except ValueError:
            print(f"Bad Input! {number}")
    return list_num

def random_list(length):
    list = []
    for item in range(length):
        list.append(random.randint(1,1000))
    return list
    

while True:
    print("~~~~~~ MENU ~~~~~~")
    print(
    """
    1 - Add numbers
    2 - Print a random list
    3 - Print list
    4 - Sort list
    10 - Clear list
    0 - Exit
    """)
    option = int(input())
    if option == 1:
        print("Write your numbers to add to the list(split by a comma): ")
        entrada = input().split(",")
        for num in int_list(entrada):
            listaNum.append(num)
    elif option == 2:
        print("Inform the length of the list: ")
        length = int(input())
        print(random_list(length))
    elif option == 3:
        print(listaNum)
    elif option == 4:
        listaNum.sort()
        print(listaNum)
    elif option == 10:
        listaNum.clear()
    elif option == 0:
        break
        
        

