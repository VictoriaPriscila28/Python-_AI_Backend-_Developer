saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def encontrar_cliente_por_cpf(cpf, clientes):
    """Função para encontrar um cliente pelo CPF."""
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            return cliente
    return None

def cpf_existe(cpf, clientes):
    """Função para verificar se o CPF já está cadastrado."""
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            return True
    return False
def cadastrar_cliente(clientes):
    """Função para cadastrar um novo cliente e adicioná-lo à lista de clientes."""
    nome = input("Por favor insira seu nome: ")
    data_nascimento = input("Por favor insira sua data de nascimento (DD/MM/AAAA): ")
    cpf = input("Por favor insira seu CPF sem traços: ")
    endereco = input("Por favor insira seu endereço: ")

    if cpf_existe(cpf, clientes):
        print(f"Erro: CPF {cpf} já está cadastrado.")
        return

    cliente = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco,
        'contas': []
    }

    clientes.append(cliente)
    print(f"Cliente {nome} cadastrado com sucesso.")


def exibir_clientes(clientes):
    """Função para exibir todos os clientes cadastrados."""
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for idx, cliente in enumerate(clientes, start=1):
        print(f"\nCliente {idx}:")
        print(f"Nome: {cliente['nome']}")
        print(f"Data de Nascimento: {cliente['data_nascimento']}")
        print(f"CPF: {cliente['cpf']}")
        print(f"Endereço: {cliente['endereco']}")
        if cliente['contas']:
            for conta in cliente['contas']:
                print(f"  Conta Bancária: Agência {conta['agencia']}, Número da Conta {conta['numero_conta']}")
        else:
            print("  Sem contas bancárias cadastradas.")

def sacar():
    global saldo, numero_saques, extrato
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

def depositar():
    global saldo, extrato
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")


def historico():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def cadastrar_conta_bancaria(clientes):
    """Função para cadastrar uma conta bancária para um cliente existente."""
    cpf = input("Por favor, insira o CPF do cliente para vincular a conta: ")

    cliente = encontrar_cliente_por_cpf(cpf, clientes)
    if cliente is None:
        print(f"Erro: CPF {cpf} não está cadastrado.")
        return

    agencia = input("Por favor, insira a agência da conta: ")
    numero_conta = "0001"  # Todas as contas terão o número 0001

    conta = {
        'agencia': agencia,
        'numero_conta': numero_conta
    }

    cliente['contas'].append(conta)
    print(f"Conta bancária vinculada ao cliente {cliente['nome']} com sucesso.")


def main():
    clientes = []  # Inicializa a lista de clientes

    while True:

        print("\nEscolha uma opção:")
        print("1. Cadastrar cliente")
        print("2. Exibir clientes")
        print("3. Sacar")
        print("4. Depositar")
        print("5. Historico")
        print("6. Cadastrar conta bancaria")
        print("7. Sair")

        opcao = int(input("Escolha a opção desejada: "))
        if opcao == 1:
            cadastrar_cliente(clientes)
        elif opcao == 2:
            exibir_clientes(clientes)
        elif opcao == 3:
            sacar()
        elif opcao == 4:
            depositar()
        elif opcao == 5:
            historico()
        elif opcao == 6:
            cadastrar_conta_bancaria(clientes)
        elif opcao == 7:
            print("Saindo")
            break
        else:
            print("Opção inválida. Tente novamente!")


if __name__ == "__main__":
    main()