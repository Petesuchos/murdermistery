from faker import Faker
import sqlite3

Faker.seed(0)
faker = Faker('pt_BR')

banco_dados = 'misterio.sqlite'

def gerar_dados_pessoas(num):
    pessoa_data = []
    for i in range(num):
        nome = faker.name()
        cpf = faker.cpf()
        data_nascimento = faker.date_of_birth(minimum_age=18, maximum_age=60)
        pessoa_data.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento})
    return pessoa_data

def gravar_pessoas_banco(pessoas, drop= True):
    conn = sqlite3.connect(banco_dados)
    cursor = conn.cursor()
    if drop:
        cursor.execute('DROP TABLE IF EXISTS pessoas')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL UNIQUE,
            data_nascimento TEXT NOT NULL
        )
    ''')

    for pessoa in pessoas:
        cursor.execute('''
                INSERT OR IGNORE INTO pessoas (nome, cpf, data_nascimento)
                VALUES (?, ?, ?)
            ''', (pessoa["nome"], pessoa["cpf"], pessoa["data_nascimento"].isoformat()))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    num_records = 10000
    pessoas = gerar_dados_pessoas(num_records)
    gravar_pessoas_banco(pessoas)