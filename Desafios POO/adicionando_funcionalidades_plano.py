class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.__nome = nome       # Atributo encapsulado
        self.__saldo = saldo     # Atributo encapsulado

    @property
    def nome(self):
        return self.__nome

    @property
    def saldo(self):
        return self.__saldo

    def verificar_saldo(self):
        if self.__saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.__saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.__nome = nome       # Atributo encapsulado
        self.__plano = plano     # Atributo encapsulado

    @property
    def nome(self):
        return self.__nome

    @property
    def plano(self):
        return self.__plano

    def verificar_saldo(self):
        return self.__plano.verificar_saldo()

    def __str__(self):
        return f"Usuário {self.__nome} criado com sucesso."

# Função principal para simular a entrada e saída
def main():
    # Entrada:
    nome_usuario = input("")
    nome_plano = input("")
    saldo_inicial = float(input(""))

    # Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
    plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
    usuario = UsuarioTelefone(nome_usuario, plano_usuario)

    # Verificação do saldo e exibição da mensagem personalizada:
    mensagem_usuario = usuario.verificar_saldo()
    print(mensagem_usuario)

if __name__ == "__main__":
    main()