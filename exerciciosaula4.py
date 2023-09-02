##  Um algoritmo que utilize  as funcionalidades de uma lista, desempenhe o papel
##de uma pilha, deve ter um menu que faça as seguintes operações

import os
import time

main_list = []

def empilhar(lista, ent):
    for num in ent:
        number = int(num)
        lista.append(number)

def desempilhar(lista):
    if not lista:
        print("Lista vazia!")
    else:
        lista.pop()
    
def limpar(lista):
    if not lista:
        print("Lista vazia!")
    else:
        lista.clear()
        
def print_pilha(lista):
    if not lista:
        print("Lista vazia!")
    else:
        for num in reversed(lista):
            print(num)
            
def desempilhar_varios(lista, qtd):
    if not lista:
        print("Lista vazia!")
    else:
        if len(lista) < qtd:
            qtd = len(lista) + 1
            if not lista:
                print("Lista vazia!")
            else:
                lista.pop()

def limpar():
    time.sleep(1)
    sistema = os.name
    if sistema == "nt":
        os.system("cls")
    else:
        os.system("clear")   
    
def exibir_topo():
    return main_list[-1]

if __name__ == "__main__":
    while True:
        limpar()
        print(""" /\/\/\/\/\/ MENU \/\/\/\/\/\ \n
    1 - EMPILHAR
    2 - DESEMPILHAR
    3 - LIMPAR
    4 - EXIBIR TOPO
    5 - EXIBIR PILHA
    0 - SAIR
        """)
        print("Escolha uma opção")
        op = int(input())
    
        if op == 0:
            break
        elif op == 1:
            print("Digite os números a empilhar: ")
            ent = input().split(",")
            empilhar(main_list, ent)
        elif op == 2:
            print("Digite quantos números a serem desempilhados: ")
            qtd = int(input())
            main_list = desempilhar(main_list)
        elif op == 3:
            main_list = limpar(main_list)
        elif op == 4:
            print(f"Último número da pilha: {exibir_topo()}")
        elif op == 5:
            print_pilha(main_list)
        elif op == 99:
            print(" ,':^) ")