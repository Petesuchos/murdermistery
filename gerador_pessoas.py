import random
import numpy as np
import sqlite3
from datetime import datetime
from faker import Faker

random.seed(0)
np.random.seed(0)
Faker.seed(0)
faker = Faker('pt_BR')


def gerar_pessoas_em_lote(lote):
    pessoa_data = []
    cpfs_gerados = set()

    for i in range(lote):
        sexo = random.choice(['M', 'F'])
        if sexo == 'M':
            nome = faker.first_name_male()
            sobrenome = faker.last_name_male()
        else:
            nome = faker.first_name_female()
            sobrenome = faker.last_name_female()

        cpf = faker.cpf()
        while cpf in cpfs_gerados:
            cpf = faker.cpf()
        cpfs_gerados.add(cpf)

        data_nascimento = faker.date_of_birth(minimum_age=18, maximum_age=50)
        pessoa_data.append(
            {"nome": nome, "sobrenome": sobrenome, "sexo": sexo, "cpf": cpf, "data_nascimento": data_nascimento})
    print(f"Lote de {lote} pessoas criado em memória com sucesso.")
    return pessoa_data


def gerar_renda_anual_em_lote(lote):
    ranges = [(1200, 5000), (5000, 10000), (10000, 40000), (40000, 100000), (100000, 200000), (200000, 500000),
              (500000, 2000000)]
    probabilities = [0.05, 0.15, 0.25, 0.25, 0.20, 0.09, 0.01]

    # Gerando escolhas aleatórias ponderadas para os intervalos
    counts = np.random.multinomial(lote, probabilities)

    # Gerando os floats aleatórios dentro dos intervalos selecionados
    random_floats = []
    for count, (low, high) in zip(counts, ranges):
        random_floats.extend(np.random.uniform(low, high, count))

    # Embaralhando os números para garantir uma distribuição aleatória
    np.random.shuffle(random_floats)
    print("Rendas anuais criadas em memória com sucesso.")
    return [round(float(num), 2) for num in random_floats]


def gerar_enderecos_por_renda(renda_lista):
    enderecos = []
    lista_bairros = [{"bairro": "Toca da Onça", "categoria": "baixa"}, {"bairro": "Quirinópolis", "categoria": "baixa"},
                     {"bairro": "Vila Moçambique", "categoria": "média"},
                     {"bairro": "Córrego Alto", "categoria": "média"}, {"bairro": "Antares", "categoria": "média"},
                     {"bairro": "Lado-de-lá", "categoria": "média"}, {"bairro": "Centro", "categoria": "média"},
                     {"bairro": "Mirante de Santa Maria", "categoria": "alta"},
                     {"bairro": "Acácias", "categoria": "alta"}, ]
    for b in lista_bairros:
        b |= {"ruas": [faker.street_name() for _ in range(10)]}

    bairros_por_categoria = {
        "baixa": [b for b in lista_bairros if b["categoria"] == "baixa"],
        "média": [b for b in lista_bairros if b["categoria"] == "média"],
        "alta": [b for b in lista_bairros if b["categoria"] == "alta"]
    }
    for renda in renda_lista:
        if renda <= 30_000.:
            pesos = [0.6, 0.37, 0.03]
        elif renda <= 300_000.:
            pesos = [0.2, 0.7, 0.1]
        else:
            pesos = [0.05, 0.25, 0.7]
        categoria_sorteada = random.choices(["baixa", "média", "alta"], pesos, k=1)[0]
        bairro = random.choice(bairros_por_categoria[categoria_sorteada])
        rua = random.choice(bairro["ruas"])
        numero = faker.building_number()
        enderecos.append(
            {"end_numero": numero, "rua": rua, "bairro": bairro["bairro"], "cidade": "Nova Londres", "estado": "SP"})
    print("Lista de endereços criada em memória com sucesso.")
    return enderecos


def gerar_automoveis(lista_renda):
    carros_marcas_modelos = {
        "Chevrolet": ["Onix", "Prisma", "Cobalt", "Cruze", "S10", "Spin", "Tracker"],
        "Volkswagen": ["Gol", "Polo", "Jetta", "Virtus", "T-Cross", "Voyage", "Saveiro", "Nivus", "Amarok"],
        "Fiat": ["Uno", "Argo", "Cronos", "Mobi", "Strada", "Toro", "Siena", "Punto"],
        "Ford": ["Ka", "Fiesta", "Focus", "EcoSport", "Ranger", "Fusion"],
        "Renault": ["Kwid", "Sandero", "Logan", "Duster", "Captur", "Oroch", "Master", "Stepway", "Scenic", "Clio"],
        "Toyota": ["Corolla", "Etios", "Hilux", "Yaris", "RAV4", "SW4", "Camry", "Prius", "Land Cruiser", "C-HR"],
        "Hyundai": ["HB20", "Creta", "Tucson", "Santa Fe", "Elantra", "Azera", "i30", "Kona", "Veloster", "Sonata"],
        "Honda": ["Civic", "Fit", "HR-V", "City", "CR-V", "Accord", "WR-V"],
        "Nissan": ["Kicks", "Versa", "March", "Sentra", "Frontier", "X-Trail", "Altima", "Pathfinder"],
        "Jeep": ["Renegade", "Compass", "Wrangler", "Gladiator", "Cherokee", "Commander"],
        "BMW": ["Serie 3", "Serie 5", "X1", "X5"],
        "Audi": ["A3", "A4", "Q3", "Q5"]
    }
    montadoras_populares = ["Chevrolet", "Volkswagen", "Fiat", "Ford", "Renault"]
    montadoras_alto_padrao = ["Jeep", "BMW", "Audi"]
    automoveis = []
    for renda in lista_renda:
        if renda <= 30_000.:
            montadora = random.choice(montadoras_populares)
        elif renda >= 300_000.:
            montadora = random.choice(montadoras_alto_padrao)
        else:
            montadora = random.choice(list(carros_marcas_modelos.keys()))
        modelo = random.choice(carros_marcas_modelos[montadora])
        ano = random.randint(2010, 2024)
        cor = random.choice(["Preto", "Branco", "Prata", "Vermelho", "Azul", "Cinza"])
        placa = faker.license_plate()
        automoveis.append({"montadora": montadora,
                           "modelo": modelo,
                           "ano": ano,
                           "cor": cor,
                           "placa": placa})
    print("Lista de automóveis criada em memória com sucesso.")
    return automoveis


def gerar_pessoas(num):
    dados_sinteticos = []
    pessoas = gerar_pessoas_em_lote(num)
    renda = gerar_renda_anual_em_lote(num)
    enderecos = gerar_enderecos_por_renda(renda)
    automoveis = gerar_automoveis(renda)

    for p, r, e, a in zip(pessoas, renda, enderecos, automoveis):
        dados_sinteticos.append(
            p | {"renda_anual": r} | e | a
        )
    return dados_sinteticos


def salvar_banco_dados(dados):
    # Conectando ao banco de dados (ele será criado se não existir)
    conn = sqlite3.connect('MISTERIO_NOVA_LONDRES.sqlite')
    cur = conn.cursor()

    # Apagando tabelas se já existirem
    cur.execute("DROP TABLE IF EXISTS PESSOA")
    cur.execute("DROP TABLE IF EXISTS RECEITA_FEDERAL")
    cur.execute("DROP TABLE IF EXISTS DETRAN")
    cur.execute("DROP TABLE IF EXISTS REGISTRO_IMOVEIS")

    # Criando as tabelas
    cur.execute('''CREATE TABLE PESSOA (
        CPF TEXT PRIMARY KEY,
        NOME TEXT,
        SOBRENOME TEXT,
        SEXO TEXT,
        DATA_NASCIMENTO DATE
    )''')

    cur.execute('''CREATE TABLE RECEITA_FEDERAL (
        CPF TEXT PRIMARY KEY,
        RENDA_ANUAL REAL,
        FOREIGN KEY(CPF) REFERENCES PESSOA(CPF)
    )''')

    cur.execute('''CREATE TABLE DETRAN (
        CPF TEXT PRIMARY KEY,
        PLACA TEXT UNIQUE,
        MONTADORA TEXT,
        MODELO TEXT,
        ANO INTEGER,
        COR TEXT,
        FOREIGN KEY(CPF) REFERENCES PESSOA(CPF)
    )''')

    cur.execute('''CREATE TABLE REGISTRO_IMOVEIS (
        CPF TEXT PRIMARY KEY,
        RUA TEXT,
        END_NUMERO INTEGER,
        BAIRRO TEXT,
        CIDADE TEXT,
        ESTADO TEXT,
        FOREIGN KEY(CPF) REFERENCES PESSOA(CPF)
    )''')

    # Inserindo os dados nas tabelas
    for item in dados:
        # Inserindo na tabela PESSOA
        cur.execute('''INSERT OR IGNORE INTO PESSOA (CPF, NOME, SOBRENOME, SEXO, DATA_NASCIMENTO)
                       VALUES (?, ?, ?, ?, ?)''',
                    (item['cpf'], item['nome'], item['sobrenome'], item['sexo'],
                     item['data_nascimento'].strftime('%Y-%m-%d')))

        # Inserindo na tabela RECEITA_FEDERAL
        cur.execute('''INSERT INTO RECEITA_FEDERAL (CPF, RENDA_ANUAL)
                       VALUES (?, ?)''',
                    (item['cpf'], item['renda_anual']))

        # Inserindo na tabela DETRAN
        cur.execute('''INSERT OR IGNORE INTO DETRAN (CPF, PLACA, MONTADORA, MODELO, ANO, COR)
                       VALUES (?, ?, ?, ?, ?, ?)''',
                    (item['cpf'], item['placa'], item['montadora'], item['modelo'], item['ano'], item['cor']))

        # Inserindo na tabela REGISTRO_IMOVEIS
        cur.execute('''INSERT INTO REGISTRO_IMOVEIS (CPF, RUA, END_NUMERO, BAIRRO, CIDADE, ESTADO)
                       VALUES (?, ?, ?, ?, ?, ?)''',
                    (item['cpf'], item['rua'], item['end_numero'], item['bairro'], item['cidade'], item['estado']))

    # Salvando as alterações
    conn.commit()

    # Fechando a conexão com o banco de dados
    conn.close()
    print("Dados inseridos no banco de dados com sucesso!")


if __name__ == '__main__':
    pessoas = gerar_pessoas(10000)
    salvar_banco_dados(pessoas)
