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
    for _ in range(length):
        list.append(random.randint(1,1000))
    return list

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def count_numbers(n):
    n_string = str(n)
    number_list = []
    other_list = []    
    i = 0
    
    for number in n_string:
        number_list.append(int(number))
        
    while i < 10:
        other_list.append(number_list.count(i))
        i +=1
    return other_list

while True:
    print("~~~~~~ MENU ~~~~~~")
    print(
    """
    1 - Add numbers
    2 - Print a random list
    3 - Print list
    4 - Sort list
    5 - Factor a number
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
    elif option == 5:
        print("Inform a number to factor: ")
        n = int(input())
        print(factorial(n))
        print(count_numbers(factorial(n)))
    elif option == 10:
        listaNum.clear()
    elif option == 0:
        break
        
        

