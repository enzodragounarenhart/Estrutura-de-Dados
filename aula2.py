#variaveis
erros = 0

def convert_to_int(numList):
    for item in numList:
        try:
            num = float(item)
            numList.append(num)
        except ValueError:
            print(f"Codejacks hated your {item}coal too much!")
    return numList

def soma_elementos(numVal):
    soma = 0
    for item in numVal:
        soma += item
        

print("Digite uma lista de números: ")
numEnt = input().split()

lista = convert_to_int(numEnt)
        

    
    
#output final
print("Números válidos: ", lista)
print("A soma dos itens é: ", soma_elementos(lista))
print("Total de erros: ",erros)