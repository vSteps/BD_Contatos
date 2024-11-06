from conexao.conexao import Conexao
from modelos.contatos import Contatos

conn = Conexao("contatos", "postgres", "postgres123banco", "localhost", "5432")
conn.conectar()

if __name__ == "__main__":
    while True:
        print("1 - Adicionar um contato")
        print("2 - Mostrar um contato")
        print("3 - Mostrar todos os contatos")
        print("4 - Atualizar um contato")
        print("5 - Deletar um contato")
        print("0 - Sair")
        
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            contato = Contatos(None, nome, email, telefone)
            conn.adicionar_contato(contato)
        
        elif opcao == 2:
            contato_id = int(input("Digite o ID do contato: "))
            contato = conn.mostrar_um_contato(contato_id)
            if contato:
                print(contato)
        
        elif opcao == 3:
            contatos = conn.mostrar_todos_contatos()
            for contato in contatos:
                print(contato)

        elif opcao == 4:
            contato_id = int(input("ID do contato: "))
            nome = input("Novo Nome: ")
            email = input("Novo Email: ")
            telefone = input("Novo Telefone: ")
            contato = Contatos(contato_id, nome, email, telefone)
            conn.atualizar_contato(contato)

        elif opcao == 5:
            contato_id = int(input("ID do contato a deletar: "))
            conn.deletar_contato(contato_id)

        elif opcao == 0:
            break
        else:
            print("Opção inválida")
