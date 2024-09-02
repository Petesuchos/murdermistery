import sqlite3
import random
from datetime import datetime, timedelta
from faker import Faker


def gerar_multas_aleatorias(db_path, data_inicio, data_fim, num_multas):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Inicializando o Faker para gerar dados aleatórios
    faker = Faker('pt_BR')


    cursor.execute("SELECT PLACA FROM DETRAN")
    placas = [row[0] for row in cursor.fetchall()]

    # Lendo as ruas distintas das tabelas REGISTRO_IMOVEIS
    cursor.execute("SELECT DISTINCT RUA FROM REGISTRO_IMOVEIS")
    ruas = [row[0] for row in cursor.fetchall()]

    # Gerando a lista de multas
    multas = []
    for _ in range(num_multas):
        # Gerar uma data aleatória entre as datas fornecidas
        data = faker.date_between(start_date=data_inicio, end_date=data_fim)

        # Gerar uma hora aleatória no formato HH:MM
        hora = faker.time(pattern="%H:%M")

        # Escolher uma placa aleatória
        placa = random.choice(placas)

        # Escolher uma rua aleatória
        rua = random.choice(ruas)

        # Gerar uma velocidade aleatória entre 70 e 120 km/h
        velocidade = random.randint(70, 120)

        # Adicionar a multa à lista
        multas.append({"data": data, "hora": hora, "placa": placa, "rua": rua, "velocidade": velocidade})
    conn.close()
    return multas

def gravar_multas_banco_dados(multas, db_path):
    # Conectando ao banco de dados SQLite
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Dropar a tabela MULTAS_TRANSITO se ela já existir
    cursor.execute("DROP TABLE IF EXISTS MULTAS_TRANSITO")

    # Criar a tabela MULTAS_TRANSITO
    cursor.execute('''
        CREATE TABLE MULTAS_TRANSITO (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            hora TEXT,
            placa TEXT,
            rua TEXT,
            velocidade INTEGER
        )
    ''')

    # Inserir as multas na tabela
    for multa in multas:
        id_aleatorio = random.randint(10000, 20000)
        cursor.execute('''
            INSERT OR IGNORE INTO MULTAS_TRANSITO (id, data, hora, placa, rua, velocidade)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (id_aleatorio, multa["data"], multa["hora"], multa["placa"], multa["rua"], multa["velocidade"]))

    # Salvar as mudanças e fechar a conexão
    conn.commit()
    conn.close()



if __name__ == '__main__':
    db_path = 'MISTERIO_NOVA_LONDRES.sqlite'
    data_inicio = datetime(2024,1,1)
    data_fim = datetime(2024,6,30)
    num_multas = 5000

    multas = gerar_multas_aleatorias(db_path, data_inicio, data_fim, num_multas)
    gravar_multas_banco_dados(multas, db_path)


