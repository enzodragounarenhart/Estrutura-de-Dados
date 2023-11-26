from Fila import *

minha_fila = Fila()

def menu():
    while True:    
        print("""
            
            ~~~~~~~~ MENU  DE FILA ~~~~~~~~
            
            1 - ADICIONAR ITEM
            2 - REMOVER ITEM
            3 - EXIBIR TODOS
            4 - EXIBIR PRIMEIRO
            5 - CHAMAR PRIMEIRO
            6 - EXIBIR TAMANHO DA FILA
            0 - SAIR
                
            """)

        op = int(input("Digite uma opção: "))
        
        if op == 0:
            break
        elif op == 1:
            item = input("Digite um item a ser enfileirado: ")
            minha_fila.enfileirar(item)
        elif op == 2:
            index = int(input("Digite o lugar do item na fila a ser removido: "))
            minha_fila.desenfileirar(index)
        elif op == 3:
            fila = minha_fila.exibir_fila()
            for i, item in enumerate(minha_fila.exibir_fila()):
                print(f"{i}: {item}")
        elif op == 4:
            print(f"O primeiro item da fila é: {minha_fila.exibir_primeiro()}")
        elif op == 5:
            print(f"O primeiro da fila({minha_fila.chamar_proximo()}) foi chamado!")
        elif op == 6:
            print("O tamanho da fila é: ", minha_fila.tamanho())

if __name__ == "__main__":
    menu()
        
