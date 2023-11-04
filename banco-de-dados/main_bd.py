import sqlite3

def criar_banco():
    conn = sqlite3.connect('linkedin_network.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            perfil_linkedin TEXT
        )               
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conexoes(
            id INTEGER PRIMARY KEY,
            contato1_id INTEGER,
            contato2_id INTEGER,
            FOREIGN KEY (contato1_id) REFERENCES contatos(id),
            FOREIGN KEY (contato2_id) REFERENCES contatos(id)
        )              
    ''')
    
    conn.commit()
    conn.close()
    
def adicionar_contato(nome, perfil_linkedin):
    conn = sqlite3.connect('linkedin_network.db')
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO contatos (nome, perfil_linkedin) VALUES (?, ?)', (nome, perfil_linkedin))
    conn.commit()
    conn.close()
    
def excluir_contato(contato_id):
    conn = sqlite3.connect('linkedin_network.db')
    cursor = conn.cursor()
    
    cursor.execute('BEGIN')
    
    try:
        cursor.execute('SELECT * FROM contatos WHERE (id = ?)',(contato_id))
        if cursor.fetchone() is None:
            print("A conexão entre esses contatos já existe!")
        else:
            cursor.execute('DELETE FROM contatos WHERE (id = ?)', (contato_id))
        
        conn.commit()
    except sqlite3.IntegrityError:
        conn.rollback()
        print("Ocorreu um erro de concorrência. Tente novamente!")
        
    conn.close()
    
def listar_contatos():
    conn = sqlite3.connect('linkedin_network.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM contatos')
    contatos = cursor.fetchall()
    
    conn.close()
    return contatos

def adicionar_conexao(contato1_id, contato2_id):
    conn = sqlite3.connect('linkedin_network.db')
    cursor = conn.cursor()
    
    cursor.execute('BEGIN')
    
    try:
        cursor.execute('SELECT * FROM conexoes WHERE (contato1_id = ? AND contato2_id = ?) OR (contato1_id = ? AND contato2_id = ?)',
                       (contato1_id, contato2_id, contato2_id, contato1_id))
        if cursor.fetchone() is None:
            cursor.execute('INSERT INTO conexoes (contato1_id, contato2_id) VALUES (?, ?)', (contato1_id, contato2_id))
        else:
            print("A conexão entre esses contatos já existe!")
        
        conn.commit()
    except sqlite3.IntegrityError:
        conn.rollback()
        print("Ocorreu um erro de concorrência. Tente novamente!")
        
    conn.close()
    
def listar_conexoes(contato_id):
    conn = sqlite3.connect('linkedin_network.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT contatos.nome
        FROM contatos
        JOIN conexoes ON contatos.id = CASE
            WHEN conexoes.contato1_id = ? THEN conexoes.notato2_id
            ELSE conexoes.contato1_id
        END               
    ''', (contato_id, contato_id, contato_id))
    
    conexoes = cursor.fetchall()
    conn.close()
    return conexoes

def menu():
    while True:
        print("""
        
        ~~~~~~~~ MENU ~~~~~~~~
        
        1 - ADICIONAR CONTATO
        2 - LISTAR CONTATOS
        3 - ADICIONAR CONEXÃO
        4 - LISTAR CONEXÕES DE UM CONTATO
        5 - EXCLUIR CONTATO
              
        """)

        op = int(input("Escolha uma opção"))
        
        if op == 1:
            nome = str(input("Nome do contato: "))
            perfil_linkedin = str(input("Perfil do LinkedIn do contato: "))
            adicionar_contato(nome, perfil_linkedin)
        elif op == 2:
            contatos = listar_contatos()
            print("~~~~~~~~ LISTA DE CONTATOS ~~~~~~~~")
            for contato in contatos:
                print(f"ID: {contato[0]}, Nome: {contato[1]}, Perfil LinkedIn {contato[2]}")
        elif op == 3:
            contato1_id = int(input("ID do primeiro contato: "))
            contato2_id = int(input("ID do segundo contato: "))
            adicionar_conexao(contato1_id, contato2_id)
        elif op == 4:
            contato_id = int(input("Digite o ID do contato"))
            conexoes = listar_conexoes(contato_id)
            print("Conexões do contato")
            for conexao in conexoes:
                print(conexao[0])
        elif op == 0:
            break
            
if __name__ == "__main__":
    criar_banco()
    menu()