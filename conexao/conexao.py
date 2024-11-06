import psycopg2
from psycopg2 import sql
from psycopg2 import OperationalError
from modelos.contatos import Contatos


class Conexao:
    
    def __init__(self, nome_db, usuario, senha, host, porta):
        self.nome_db = nome_db
        self.usuario = usuario
        self.senha = senha
        self.host = host
        self.porta = porta
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = psycopg2.connect(
                database=self.nome_db,
                user=self.usuario,
                password=self.senha,
                host=self.host,
                port=self.porta
            )
            print("Conexão ao banco de dados PostgreSQL realizada com sucesso")
        except OperationalError as e:
            print(f"Ocorreu um erro ao conectar ao banco de dados: {e}")
            raise


    def adicionar_contato(self, Contatos):
        if self.conexao is None:
            print("Não há conexão com o banco de dados.")
            return []

        try:
            cursor = self.conexao.cursor()
            query = """
                INSERT INTO contatos (nome, email, telefone) VALUES (%s, %s, %s)
            """
            cursor.execute(query, (Contatos.nome, Contatos.email, Contatos.telefone))
            self.conexao.commit()
            cursor.close()
            print("Contato adicionado com sucesso.")
            return []
        except OperationalError as e:
            print(f"Ocorreu um erro ao adicionar o contato: {e}")
            return []
    

    def mostrar_um_contato(self, contato_id):
        if self.conexao is None:
            print("Não há conexão com o banco de dados.")
            return []

        try:
            cursor = self.conexao.cursor()
            query = """
                SELECT * FROM contatos WHERE id = %s
            """
            cursor.execute(query, (contato_id,)) 
            resultado = cursor.fetchone()
            cursor.close()

            if resultado:
                return Contatos(id=resultado[0], nome=resultado[1], email=resultado[2], telefone=resultado[3])
            else:
                print("Contato não encontrado.")
                return []
        except OperationalError as e:
            print(f"Ocorreu um erro ao buscar o contato: {e}")
            return []
    
    def mostrar_todos_contatos(self):
        if self.conexao is None:
            print("Não há conexão com o banco de dados.")
            return []

        try:
            cursor = self.conexao.cursor()
            query = "SELECT * FROM contatos"
            cursor.execute(query)
            contatos_data = cursor.fetchall()
            cursor.close()

            contatos = [Contatos(id=linha[0], nome=linha[1], email=linha[2], telefone=linha[3]) for linha in contatos_data]

            return contatos
        except Exception as e:
            print(f"Ocorreu um erro ao buscar os contatos: {e}")
            return []

    def atualizar_contato(self, contato):
        if self.conexao is None:
            print("Não há conexão com o banco de dados.")
            return []

        try:
            cursor = self.conexao.cursor()
            query = """
                UPDATE contatos SET nome = %s, email = %s, telefone = %s WHERE id =  %s
            """
            cursor.execute(query, (Contatos.nome, Contatos.email, Contatos.telefone, Contatos.id))
            self.conexao.commit()
            cursor.close()
            print("Contato atualizado com sucesso.")
            return []
        except OperationalError as e:
            print(f"Ocorreu um erro ao atualizar o contato: {e}")
            return []
    
    def deletar_contato(self, contato_id):
        if self.conexao is None:
            print("Não há conexão com o banco de dados.")
            return False

        try:
            cursor = self.conexao.cursor()
            query = "DELETE FROM contatos WHERE id = %s"
            cursor.execute(query, (contato_id,)) 
            self.conexao.commit()
            cursor.close()
            print("Contato deletado com sucesso.")
            return True
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o contato: {e}")
            return False