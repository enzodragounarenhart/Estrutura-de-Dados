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
            cursor.execute('DELETE FROM conexoes WHERE contato1_id = %i OR contato2_id = %i',(contato_id, contato_id))
            cursor.execute('DELETE FROM contatos WHERE (id = %i)',(contato_id))
            conn.commit()
        except mysql.connector.errors as Error:
            conn.rollback()
            print(f"Ocorreu um erro! {Error}")
            
        conn.close()
        
    def listar_contatos(self):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM contatos')
        contatos = cursor.fetchall()
        
        conn.close()
        return contatos
    
    def listar_contato(self, contato_id):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        try:
            cursor.execute('SELECT * FROM contatos WHERE (id = %i),', (contato_id))
            contato = cursor.fetchone()
        except mysql.connector.errors as Error:
            conn.rollback()
            print(f"Ocorreu um erro! {Error}")
            
        return contato

def adicionar_conexao(contato1_id, contato2_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    cursor.execute('BEGIN')
    
    try:
        cursor.execute('SELECT * FROM conexoes WHERE (contato1_id = %i AND contato2_id = %i) OR (contato1_id = %i AND contato2_id = %i)',
                       (contato1_id, contato2_id, contato2_id, contato1_id))
        if cursor.fetchone() is None:
            cursor.execute('INSERT INTO conexoes (contato1_id, contato2_id) VALUES (%i, %i)', (contato1_id, contato2_id))
        else:
            print("A conexão entre esses contatos já existe!")
        
        conn.commit()
    except mysql.connector.errors as Error:
        conn.rollback()
        print(f"Ocorreu um erro!\n {Error}")
        
    conn.close()
    
def listar_conexoes(contato_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT contatos.nome
        FROM contatos
        JOIN conexoes ON contatos.id = CASE
            WHEN conexoes.contato1_id = %i THEN conexoes.contato2_id
            ELSE conexoes.contato1_id
        END
        WHERE conexoes.contato1_id = %i OR conexoes.contato2_id = %i               
    ''', (contato_id, contato_id, contato_id))
    
    conexoes = cursor.fetchall()
    conn.close()
    return conexoes

def menu():
    while True:
        contato = Contato()
        print("""
        
        ~~~~~~~~ MENU ~~~~~~~~
        
        1 - ADICIONAR CONTATO
        2 - LISTAR CONTATOS
        3 - ADICIONAR CONEXÃO
        4 - LISTAR CONEXÕES DE UM CONTATO
        5 - EXCLUIR CONTATO
        0 - SAIR
              
        """)

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
            contatos = contato.listar_contatos()
            print("~~~~~~~~ LISTA DE CONTATOS ~~~~~~~~")
            for contato in contatos:
                print(f"ID: {contato[0]}, Nome: {contato[1]}, Perfil LinkedIn {contato[2]}")
        elif op == 3:
            contato1_id = int(input("ID do primeiro contato: "))
            contato2_id = int(input("ID do segundo contato: "))
            adicionar_conexao(contato1_id, contato2_id)
        elif op == 4:
            contato_id = input("Digite o ID do contato: ")
            conexoes = listar_conexoes(contato_id)
            print("Conexões do contato: ")
            for conexao in conexoes:
                print(conexao[0])
        elif op == 5:
            contato_id = input("Digige o ID do contato a ser excluido: ")
            contato.excluir_contato(contato, contato_id)
        elif op == 0:
            break
            
if __name__ == "__main__":
    criar_banco(db_config)
    menu()