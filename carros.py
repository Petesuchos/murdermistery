import random
from faker import Faker

from carros_atributos import carros_marcas_modelos, carros_cores

Faker.seed(0)
faker = Faker('pt_BR')

def gerar_dados_carros(num):
    dados_carros = []
    for i in range(num):
        marca = random.choice(list(carros_marcas_modelos.keys()))
        modelo = random.choice(carros_marcas_modelos[marca])
        ano = random.randint(2010, 2024)
        cor = random.choice(carros_cores)
        placa = faker.license_plate()
        dados_carros.append({"marca": marca,
                             "modelo": modelo,
                             "ano":ano,
                             "cor":cor,
                             "placa":placa})
    return dados_carros


if __name__ == '__main__':
    n = 10
    carros = gerar_dados_carros(n)
    for carro in carros:
        print(carro)
