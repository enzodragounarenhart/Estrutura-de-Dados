import random, os, time
main_list = []

def enfileirar(lista: list, valor):
    lista.append(valor)
    
def aleatorio(lista: list, valor):
    for _ in range(valor):
        aleatorio = random.randint(0,100)
        enfileirar(lista, aleatorio)
        
def selection_sort(lista: list):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[j] < lista[i]:
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux

def bubble_sort(lista: list):
    for i in range(len(lista)):
        for y in range(i + 1, len(lista)):
            if lista[y] < lista[i]:
                aux = lista[y]
                lista[y] = lista[i]
                lista[i] = aux

def insertion_sort(lista: list):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i -1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

def merge_sort(lista: list):
    if len(lista) > 1:
        meio = len(lista) // 2
        metade_esquerda = lista[:meio]
        metade_direita = lista[meio:]

        merge_sort(metade_esquerda)
        merge_sort(metade_direita)

        i = j = k = 0

        while i < len(metade_esquerda) and j < len(metade_esquerda):
            if metade_esquerda[i] < metade_direita[j]:
                lista[k] = metade_esquerda[i]
                i+=1
            else:
                lista[k] = metade_direita[j]
                j+=1
            k=+1
        while i < len(metade_esquerda):
            lista[k] = metade_esquerda[i]
            i+=1
            k+=1
        while j < len(metade_direita):
            lista[k] = metade_direita[j]
            j+=1
            k+=1
    return lista

def aleatorio(lista: list, valor):
    while len(lista) < valor:
        aleatorio = random.randint(1, 1000)
        if aleatorio not in lista:
            enfileirar(lista, aleatorio)

def cronometro(algo, lista):
    inicio = time.time()
    algo(lista)
    fim = time.time()
    tempo = fim - inicio
    print(f"Tempo: {tempo}")

def is_sorted(lista) -> bool:
    return all(a <=b for a, b in zip(lista, lista[:1]))

def menu():
    print("""/\/\/\/\/\/\ MENU /\/\/\/\/\/\ \n
        1 - DIGITAR NÚMERO
        2 - CRIAR LISTA ALEATÓRIA
        3 - IMPRIMIR LISTA
        4 - SELECTION SORT
        5 - BUBBLE SORT
        6 - INSERTION SORT
        7 - MERGE SORT
        9 - LIMPAR LISTA    
          """)

def limpar():
    sistema = os.name
    if sistema == "nt":
        os.system("cls")
    else:
        os.system("clear") 

if __name__ == "__main__":
    
    while True:
        menu()
        
        print("Digite uma escolha")
        op = int(input())
        
        if op == 0:
            break
        elif op == "clear":
            limpar()
        elif op == 9:
            main_list.clear()
        elif op == 1:
            print("Digite um número para enfileirar")
            num = int(input())
            enfileirar(main_list, num)
        elif op == 2:
            print("Escolha quantos elementos na lista: ")
            quant = int(input())
            aleatorio(main_list, quant)
        elif op == 6:
            cronometro(insertion_sort, main_list)
        elif op == 7:
            cronometro(merge_sort, main_list)
        elif op == 9:
            main_list.clear()