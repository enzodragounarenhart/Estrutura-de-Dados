import fila

main_fila = []
deleted_fila = []

if __name__ == "__main__":
    while True:
        fila.menu()
        
        print("Digite uma opção")
        op = input()
        
        if op == '0':
            break
        elif op == 'clear':
            fila.clear()
        elif op == '1':
            print("Digite o nome de uma pessoa: ")
            nome = input()
            fila.in_queue(main_fila, nome)
        elif op == '2':
            fila.in_queue(deleted_fila, main_fila[0])
            fila.de_queue(main_fila)
        elif op == '3':
            fila.show_first(main_fila)
        elif op == '4':
            fila.show_fila(main_fila)
        