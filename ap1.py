import os, time

main_deque = []

def inserir_comeco(deque: list, valor):
    deque.insert(0, valor)

def inserir_fim(deque: list, valor):
    deque.append(valor)

def exibir_primeiro(deque: list):
    if not deque:
        print("Deque vazio!")
    else:
        return deque[0]
        
def exibir_ultimo(deque: list):
    if not deque:
        print("Deque vazio!")
    else:
        return deque[-1]
        
def remover_primeiro(deque: list):
    if not deque:
        print("Deque vazio!")
    else:
        return deque.pop(0)
        
def remover_ultimo(deque: list):
    if not deque:
        print("Deque vazio!")
    else:
        return deque.pop(-1)
        
def menu():
    print("""/\/\/\/\/\/\ MENU /\/\/\/\/\/\
        1 - ADICIONAR NO INICIO DO DEQUE
        2 - ADICIONAR NO FIM DO DEQUE
        3 - EXIBIR PRIMEIRO
        4 - EXIBIR ULTIMO
        5 - REMOVER PRIMEIRO
        6 - REMOVER ULTIMO  
        0 - SAIR
          """)

def limpar():
    time.sleep(1)
    sistema = os.name
    if sistema == "nt":
        os.system("cls")
    else:
        os.system("clear") 
    
if __name__ == "__main__":
    while True:
        limpar()
        menu()
        print("Escolha uma opcao")
        op = int(input())
        
        if op == 0:
            break
        elif op == 1:
            print("Digite o numero a ser inserido no comeco do deque: ")
            val = int(input())
            inserir_comeco(main_deque, val)
        elif op == 2:
            print("Digite o numero a ser inserido no fim do deque: ")
            val = int(input())
            inserir_fim(main_deque, val)
        elif op == 3:
            print(f"Primeiro valor do deque: {exibir_primeiro(main_deque)}")
        elif op == 4:
            print(f"Ultimo valor do deque: {exibir_ultimo(main_deque)}")
        elif op == 5:
            print(f"Primeiro valor removido com sucesso! \n Valor removido: {remover_primeiro(main_deque)}")
        elif op == 6:
            print(f"Ultimo valor removido com sucesso! \n Valor removido: {remover_ultimo(main_deque)}")
        
        