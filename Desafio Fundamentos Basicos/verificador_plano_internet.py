def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"

    elif consumo > 10 and consumo <= 20:
        return "Plano Prata Fibra - 100Mbps"

    else:
        return "Plano Premium Fibra - 300Mbps"


# Solicita ao usuário que insira o consumo médio mensal de dados:

consumo = float(input())
print(recomendar_plano(consumo))