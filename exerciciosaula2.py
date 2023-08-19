## EXERCICIO 1

listaNum = []

print("Digite uma lista de números separados por vírgula: ")
entrada = input().split(",")

for item in entrada:
    try:
        numero = int(item)
        listaNum.append(numero)
        
    except ValueError:
        print(f"Bad Input! {item}")
        
def soma_pares(lista):
    soma = 0
    for item in lista:
        if item % 2 == 0:
            soma += item
    return soma

print(f"Soma dos números pares {soma_pares(listaNum)}")

## EXERCICIO 2

print("Digite o seu peso: ")
peso = float(input())

print("Digite a sua altura: ")
altura = float(input())

def calcular_imc(peso, altura):
    return peso/(altura*altura)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc >= 18.5 and imc <= 24.9:
        return "Peso normal"
    elif imc >24.9 and imc <= 29.9:
        return "Acima do peso (sobrepeso)"
    elif imc >29.9 and imc <= 34.9:
        return "Obesidade I"
    elif imc >34.9 and imc <= 39.9:
        return "Obesidade II"
    elif imc >39.9:
        return "Obesidade III"
    
imc = calcular_imc(peso, altura)
classImc = classificar_imc(imc)
print(f"Cálculo de IMC: {imc}")
print(f"Classificação do seu IMC: {classImc}")

## EXERCICIO 3
listaEx3 = []

print("Digite uma lista de números")

entrada3 = input().split(",")

for item in entrada3:
    try:
        numero = int(item)
        listaEx3.append(numero)
        
    except ValueError:
        print(f"Bad Input! {item}")
        
listaEx3.sort()
maximo = listaEx3[-1]
minimo = listaEx3[0]

print(f"Máximo: {maximo}\n Mínimo: {minimo}")

## EXERCICIO 4
def vogalis(text):
    vogais = 0
    string = "aeiouAEIOU"
    
    for letra in text:
        if letra.lower() in string:
            vogais += 1
    return vogais

print("Escreva uma palavra: ")
palavra = input()



print(palavra)
print(vogalis(palavra))