import os

main_fila = []
deleted_fila = []

def clear():
    sistema = os.name
    if sistema == "nt":
        os.system("cls")
    else:
        os.system("clear")   

def menu():
    print(""" /\/\/\/\/\/ MENU \/\/\/\/\/\ \n
    1 - ENFILEIRAR
    2 - DESENFILEIRAR
    4 - EXIBIR PRIMEIRO
    5 - EXIBIR FILA
    0 - SAIR
        """)

def in_queue(fila, valor):
    valor.capitalize()
    fila.append(valor)

def de_queue(fila: list):
    if not fila:
        print("Fila Vazia!")
    else:
        fila.pop(0)
        
def show_fila(fila):
    if not fila:
        print("Fila vazia!")
    else:
        for nome in enumerate(fila):
            print(nome)
            
def show_first(fila):
    if not fila:
        print("Fila vazia")
    else:
        print(f"O {fila[0]} é o primeiro da fila!")