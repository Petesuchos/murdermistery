from faker import Faker
import random

rendimentos_anuais = [10_000.0, 20_000.0, 30_000.0, 40_000.0, 50_000.0, 100_000.0, 200_000.0, 300_000.0, 500_000.0, 1_000_000.0]
rendimentos_anuais_pesos = [10, 25, 25, 10, 10, 7, 5, 4, 3, 1]

Faker.seed(0)
faker = Faker('pt_BR')

def sortear_rendimento(num):
    return random.choices(rendimentos_anuais,
                          weights=rendimentos_anuais_pesos,
                          k=num)

if __name__ == '__main__':
    n = 100
    for rendimento in sortear_rendimento(n):
        print(rendimento)