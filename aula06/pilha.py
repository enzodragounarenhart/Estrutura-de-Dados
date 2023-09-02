import os
import time

main_list = []
deleted_list = []
def menu():
    print(""" /\/\/\/\/\/ MENU \/\/\/\/\/\ \n
    1 - EMPILHAR
    2 - DESEMPILHAR
    3 - LIMPAR
    4 - EXIBIR TOPO
    5 - EXIBIR PILHA
    0 - SAIR
        """)

def empilhar(pilha, ent):
    pilha.append(ent)

def desempilhar(pilha):
    if not pilha:
        print("Pilha vazia!")
    else:
        pilha.pop()
    
def limpar(pilha):
    if not pilha:
        print("Pilha vazia!")
    else:
        pilha.clear()
        
def print_pilha(pilha):
    if not pilha:
        print("Pilha vazia!")
    else:
        for num in reversed(pilha):
            print(num)
            
def desempilhar_varios(pilha: list, qtd: int):
    if not pilha:
        print("Pilha vazia!")
    else:
        if len(pilha) < qtd:
            qtd = len(pilha) + 1
            if not pilha:
                print("Pilha vazia!")
            else:
                empilhar(deleted_list, pilha[-1])
                pilha.pop()

def limpar():
    time.sleep(1)
    sistema = os.name
    if sistema == "nt":
        os.system("cls")
    else:
        os.system("clear")   
    
def exibir_topo():
    return main_list[-1]
