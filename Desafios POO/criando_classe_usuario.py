class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.__nome = nome  # Atributo encapsulado
        self.__numero = numero  # Atributo encapsulado
        self.__plano = plano  # Atributo encapsulado

    @property
    def nome(self):
        return self.__nome

    @property
    def numero(self):
        return self.__numero

    @property
    def plano(self):
        return self.__plano

    def __str__(self):
        return f"Usuário {self.__nome} criado com sucesso."


# Função principal para simular a entrada e saída
def main():
    # Entrada:
    nome = input("")
    numero = input("")
    plano = input("")

    # Criação do objeto UsuarioTelefone:
    usuario = UsuarioTelefone(nome, numero, plano)

    # Exibindo a mensagem de sucesso:
    print(usuario)


if __name__ == "__main__":
    main()