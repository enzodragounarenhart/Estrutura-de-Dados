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
            if lista[j] < lista[i]
            aux = lista[j]
            lista[j] = lista[i]
            lista[i] = aux
            print(lista)
    return lista

def cronometro(algo, lista):
    inicio = time.time()
    algo(lista)
    fim = time.time()
    tempo = fim - inicio
    return tempo

def is_sorted(lista) -> bool:
    return all(a <=b for a, b in zip(lista, lista[:1]))

def bogosort(lista) -> list:
    while not is_sorted(lista):
        shuffle(lista)
    return lista

def menu():
    print("""/\/\/\/\/\/\ MENU /\/\/\/\/\/\ \n
        1 - ADICIONAR NO INICIO DO DEQUE
        2 - ADICIONAR NO FIM DO DEQUE
        3 - EXIBIR PRIMEIRO
        4 - EXIBIR ULTIMO
        5 - REMOVER PRIMEIRO
        6 - REMOVER ULTIMO  
        0 - SAIR
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
            print("Escolha quantos elementos na lista")
            valores = int(input())
            aleatorio(main_list, valores)