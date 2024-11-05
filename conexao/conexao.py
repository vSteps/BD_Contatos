import psycopg2
from psycopg2 import sql
from psycopg2 import OperationalError
from modelos.contatos import contato


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


def adicionar_contato(self, contato):
    if self.conexao is None:
        print("Não há conexão com o banco de dados.")
        return []

    try:
        cursor = self.conexao.cursor()
        query = """
            INSERT INTO contatos (contato.nome, contato.email, contato.telefone) VALUES (%s, %s, %s)
        """
        cursor.execute(query, (contato.nome, contato.email, contato.telefone))
        self.conexao.commit()
        cursor.close()
        print("Contato adicionado com sucesso.")
        return []
    except OperationalError as e:
        print(f"Ocorreu um erro ao adicionar o contato: {e}")
        return []

        
        
def mostrar_um_contato(self, id):
    if self.conexao is None:
        print("Não há conexão com o banco de dados.")
        return []

    try:
        cursor = self.conexao.cursor()
        query = """
            SELECT * FROM contatos WHERE id_ VALUES (%s, %s, %s)
        """
        cursor.execute(query, (nome, email, telefone))
        self.conexao.commit()
        cursor.close()
        print("Contato adicionado com sucesso.")
        return []
    except OperationalError as e:
        print(f"Ocorreu um erro ao adicionar o contato: {e}")
        return []

        
    def obter_clientes_por_data(self, data_inicio, data_fim):
        if self.conexao is None:
            print("Não há conexão com o banco de dados.")
            return []

        try:
            cursor = self.conexao.cursor()
            query = """
                SELECT DISTINCT clientes.*
                    FROM clientes
                    JOIN pedidos ON clientes.id = pedidos.cliente_id
                    WHERE pedidos.data_pedido BETWEEN %s AND %s
            """
            cursor.execute(query, (data_inicio,data_fim,))
            resultSet = cursor.fetchall()
            clientes = []
            for row in resultSet:
                clientes.append(Cliente(row[0], row[1], row[2], row[3], row[4]))
            cursor.close()
            return clientes
        except OperationalError as e:
            print(f"Ocorreu um erro ao consultar os itens do pedido: {e}")
            return []