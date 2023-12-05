import mysql.connector

db_config = {
    'user': 'turma6ntop',
    'password': 'turma6ntop',
    'host': 'db4free.net',
    'database': 'linkedin6n',
    'port': 3306
}

def criar_banco(db_config):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos(
            id INT PRIMARY KEY AUTO_INCREMENT,
            nome varchar(50),
            perfil_linkedin varchar(50)
        );               
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conexoes(
            id INT PRIMARY KEY AUTO_INCREMENT,
            contato1_id INT,
            contato2_id INT,
            FOREIGN KEY (contato1_id) REFERENCES contatos(id),
            FOREIGN KEY (contato2_id) REFERENCES contatos(id)
        )              
    ''')
    
    conn.commit()
    conn.close()

class Contato:
    def __init__(self):
        self.id = 0
        self.nome = ""
        self.perfil_linkedin = ""
        
        
    def add_contato(self, nome, perfil_linkedin):
        self.nome = nome
        self.perfil_linkedin = perfil_linkedin
        
    def listar_ids(self):
        return [contatos[0] for contatos in self.listar_contatos()]
        
    
    def adicionar_contato(self):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        print(self.nome)
        print(self.perfil_linkedin)
        try:
            cursor.execute('SELECT * FROM contatos WHERE perfil_linkedin = %s', (self.perfil_linkedin,))
            if cursor.fetchone() is None:
                cursor.execute('INSERT INTO contatos (nome, perfil_linkedin) VALUES (%s, %s);', (self.nome, self.perfil_linkedin))
            else:
                return 0
        except mysql.connector.Error as Error:
            conn.rollback()
            return print(Error)
        conn.commit()
        conn.close()
        return 1
        
    
    def excluir_contato(self,contato_id):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        cursor.execute('BEGIN')
        
        try:
            cursor.execute('DELETE FROM conexoes WHERE contato1_id = %s OR contato2_id = %s',(contato_id, contato_id))
            cursor.execute('DELETE FROM contatos WHERE (id = %s)',(contato_id,))
            conn.commit()
        except mysql.connector.Error as Error:
            conn.rollback()
            print(f"Ocorreu um erro! {Error}")
        
        print("Contato excluido com sucesso!")
            
        conn.close()
        
    def listar_contatos(self):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM contatos')
        contatos = cursor.fetchall()
        
        conn.close()
        return contatos
    
    def exibir_contato(self, contato_id):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        try:
            cursor.execute('SELECT * FROM contatos WHERE (id = %s)', (contato_id,))
            contato = cursor.fetchone()
            return contato
        except mysql.connector.Error as Error:
            conn.rollback()
            print(f"Ocorreu um erro! {Error}")
        
        conn.close()
        return contato
            
        
    
def menu():
    while True:
        contato = Contato()
        
        contatos = contato.listar_contatos()
        lista_ids = contato.listar_ids()
        
        print("""
        
        ~~~~~~~~ MENU ~~~~~~~~
        
        1 - ADICIONAR CONTATO
        2 - LISTAR CONTATOS
        3 - EXCLUIR CONTATO
        4 - EXIBIR DETALHES DE UM CONTATO
        0 - SAIR
              
        """)
        
        try:
            op = int(input("Escolha uma opção: "))
            
                        
                        
            if op == 1:
                nome = (input("Nome do contato: "))
                perfil_linkedin = (input("Perfil do LinkedIn do contato: "))
                contato.add_contato(nome, perfil_linkedin)
                if contato.adicionar_contato() == 1:
                    print("Contato adicionado com sucesso!")
                elif contato.adicionar_contato() == 0:
                    print("Contato já cadastrado!")
                else: print("Erro ao cadastrar contato!")
                
            elif op == 2:
                
                print("~~~~~~~~ LISTA DE CONTATOS ~~~~~~~~")
                for contato in contatos:
                    print(f"ID: {contato[0]}, Nome: {contato[1]}")

            elif op == 3:
                
                print("~~~~~~~~ LISTA DE CONTATOS ~~~~~~~~")
                for contatos in contatos:
                    print(f"ID: {contatos[0]}, Nome: {contatos[1]}")
                    
                    
                while True:
                    try:
                        contato_id = int(input("\nDigite o ID do contato a ser excluido(0 para sair): "))
                        if contato_id == 0:
                            break
                        elif contato_id not in lista_ids:
                            print("Contato nao encontrado, tente novamente.")
                        else: 
                            contato.excluir_contato(contato_id)
                    except ValueError:
                        print("Valor invalido. Tente novamente!")
            
            elif op == 4:
                
                while True:
                    try:
                        id = int(input("Digite o ID do Usuario para exibir mais detalhes(0 para sair): "))
                        if id == 0:
                            break
                        elif id not in lista_ids:
                            print("Contato nao encontrado, tente novamente.")
                        else: 
                            ex_contato = contato.exibir_contato(id)
                            print(f"""
                                
            ~~~~~~ Contato {ex_contato[0]} ~~~~~~
            
            Nome do Contato: {ex_contato[1]}
            Perfil do LinkedIn: {ex_contato[2]}
                                
                                """)
                    except ValueError:
                        print("Valor invalido. Tente novamente!")
            
            elif op == 0:
                break
        except ValueError:
                    print("Valor invalido. Tente novamente!")
            
if __name__ == "__main__":
    criar_banco(db_config)

    menu()
    