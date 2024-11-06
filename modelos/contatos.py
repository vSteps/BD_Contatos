class Contatos():
    def __init__(self, id, nome, email, telefone):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def id(self):
        return self.id

    def nome(self):
        return self.nome

    def email(self):
        return self.email

    def telefone(self):
        return self.telefone


    def __str__(self):
        return f"Contato(id={self.id}, nome={self.nome}, email={self.email}, telefone={self.telefone})"