import mysql.connector
class Connection:
    def __init__(self):
        self.db_config = {}
        
    def criar_banco(self):
        conn = mysql.connector.connect(**self.db_config)
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