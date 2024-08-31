import random
from faker import Faker

Faker.seed(0)
faker = Faker('pt_BR')

def gerar_ruas(num_ruas=10):
    return [faker.street_name() for _ in range(num_ruas)]

def gerar_bairros(num=4):
    return [faker.neighborhood() for _ in range(num)]

def gerar_bairros_ruas(num_bairros=4, num_ruas=10):
    bairro_ruas = {}
    bairros = gerar_bairros(num_bairros)
    for bairro in bairros:
        bairro_ruas[bairro] = gerar_ruas(num_ruas)
    return bairro_ruas


def gerar_enderecos(num_enderecos, num_bairros=4, num_ruas=10):
    enderecos = []
    bairros_ruas = gerar_bairros_ruas(num_bairros, num_ruas)
    for i in range(num_enderecos):
        numero = faker.building_number()
        bairro = random.choice(list(bairros_ruas.keys()))
        rua = random.choice(bairros_ruas[bairro])
        cidade = "Antares"
        estado = "RS"
        enderecos.append({"numero": numero, "rua": rua, "bairro": bairro, "cidade": cidade, "estado": estado})

    return enderecos

if __name__ == '__main__':
    n = 10
    enderecos = gerar_enderecos(n)
    for endereco in enderecos:
        print(endereco)