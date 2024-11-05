from conexao.conexao import Conexao
from modelos import contato

conn = Conexao("contatos", "postgres", "postgres", "localhost", "5432")
conn.conectar()

# Exemplo de uso das funções
if __name__ == "__main__":

    while(True):
        #Menu com funções
        print("1 - Adicionar um contato")
        print("2 - Mostrar um contato")
        print("2 - Mostrar todos os contatos")
        print("3 - Atualizar um contato")
        print("4 - Deletar um contato")
        print("0 - Sair")
        
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            id_cliente = int(input("Digite o ID do Cliente desejado: "))                        
            if conn:
                pedidos = conn.obter_pedidos_por_cliente(id_cliente)
                for pedido in pedidos:
                    print(pedido)
        elif opcao == 2:
            id_pedido = int(input("Digite o ID do Pedido desejado: "))                        
            if conn:
                itens = conn.obter_itens_por_pedido(id_pedido)
                for item in itens:
                    print(item.nome)
        elif opcao == 3:
            print("Digite o intervalo de Datas desejado: ")                        
            data_inicio = input("Digite a data de início: ")
            data_fim = input("Digite a data de fim: ")
            if conn:
                clientes = conn.obter_clientes_por_data(data_inicio, data_fim)
                for cliente in clientes:
                    print(cliente)
        elif opcao == 0:
            break
        else:
            print("Opção inválida")