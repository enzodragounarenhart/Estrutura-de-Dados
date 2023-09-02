##  Um algoritmo que utilize  as funcionalidades de uma lista, desempenhe o papel
##de uma pilha, deve ter um menu que faça as seguintes operações

import pilha

main_pile = []
deleted_pile = []

if __name__ == "__main__":
    while True:
        pilha.limpar()
        pilha.menu()   
        try:
            opc = int(input("Digite uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um número válido.")
            continue

        if opc == 1:
            entrada = input("Digite os valores para empilhar (separados por vírgula): ")
            valores_separados = entrada.split(",")
        
            for valor_str in valores_separados:
                try:
                    valor = int(valor_str)
                    pilha.empilhar(main_pile, valor)
                except ValueError:
                    print(f"Valor inválido: {valor_str}")

        elif opc == 2:
            pilha.empilhar(deleted_pile, main_pile[-1])
            pilha.desempilhar(main_pile)
        elif opc == 3:
            pilha.limpar(main_pile)
        elif opc == 4:
            print(f"Item no topo da lista: {pilha.exibir_topo(main_pile)}")
        elif opc == 5:
            pilha.print_pilha(main_pile)
        elif opc == 6:
            pilha.exibir_topo(f"Topo da lista dos deletados{deleted_pile}")
        elif opc == 7:
            pilha.print_pilha(deleted_pile)
        elif opc == 8:
            valor = deleted_pile[-1]
            pilha.empilhar(main_pile, valor)
            pilha.desempilhar(deleted_pile)
        
        elif opc == 0:
            break
        else:
            print("Escolha uma opção do MENU!")