lista = []

print(
"""
1 - PARA INSERIR
2 - PARA REMOVER O ÚLTIMO
3 - PARA REMOVER O PRIMEIRO
4 - PARA IMPRIMIR A LISTA
5 - PARA REMOVER ESPECIFICO
6 - PARA ORDENAR A LISTA
7 - PARA INSERIR EM UMA POSIÇÃO
0 - PARA SAIR
"""
)

while True:
    
    opc = int(input("Digite uma opção: "))
    
    
    if opc == 0:
        break
    
    if opc == 1:
        num = int(input("Digite um número: "))
        lista.append(num)

    elif opc == 2:
        lista.pop()
        
    elif opc == 3:
        lista.pop(0)
        
    elif opc == 4:
        for item in lista:
            print(item)
            
    elif opc == 5:
        index = int(input("Digite a posição do número: "))
        lista.pop(index)
        
    elif opc == 6:
        lista.sort()
        
    elif opc == 7:
        numIn = int(input("Digite o número: "))
        indexIn = int(input("Digite a posição do número: "))
        lista.insert(index)
        
    else:
        print("Digite uma opção válida")
