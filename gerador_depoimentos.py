import sqlite3
import random
from faker import Faker
from datetime import datetime

random.seed(0)
Faker.seed(0)
faker = Faker('pt_BR')


def gerar_depoimentos_a_partir_cpfs(cpfs):
    # Listas de variáveis possíveis
    locais = ["rua", "jardim", "garagem", "sala de estar", "quarto", "cozinha", "escritório", "biblioteca", "parque",
              "mercado", "posto de gasolina", "escadaria", "Congresso Nacional", "pista de skate", "academia",
              "padaria", "relojoaria", "banco", "zoológico", "sala de aula", "escola", "lago", "casa do Patolino",
              "borracharia", "tribunal", "laboratório", "pula pula", "bar", "boliche", "show"]
    horas = ["14:00", "18:30", "22:15", "07:45", "16:50", "12:10", "23:30", "09:00", "03:45", "11:15", "8 da manhã",
             "10 horas mais ou menos", "23:55", "22 em ponto"]
    eventos = ["um assalto", "uma briga", "um furto", "um arrombamento", "um sequestro", "um disparo de arma",
               "um roubo", "um corre corre", "um vandalismo", "um ato suspeito", "um grito", "um poltergeist",
               "uma assombração", "uma facada", "uma briga", "uma cusparada", "um xingamento", "um tapa",
               "uma violação das liberdades individuais", "um ovni", "uma criança chorando", "um gato miando",
               "um crime ambiental", "um cachorro latindo", "uma flechada", "uma batida", "um ataque de ganso"]
    objetos = ["uma bolsa", "um telefone", "uma carteira", "um notebook", "uma chave", "um livro", "um documento",
               "um casaco", "uma mochila", "um relógio", "uma arma", "uma chave inglesa", "uma soqueira",
               "uma fantasia", "uma máscara", "uma criatura", "um dente", "uma Bíblia", "um computador", "um robô",
               "uma pistola", "um machado", "um envelope", "um cadáver"]
    atividades = ["conversando", "lendo", "trabalhando", "cozinhando", "correndo", "andando", "esperando", "observando",
                  "procurando algo", "descansando", "orando", "latindo", "mordendo", "gritando", "batendo", "girando",
                  "dançando", "mascando chiclete", "dormindo", "pedalando", "cantando", "roncando", "sonhando",
                  "roubando um pirulito de criancinha"]
    cores = ["vermelho", "azul", "verde", "amarelo", "preto", "branco", "cinza", "marrom", "roxo", "laranja",
             "cor de rosa", "cor de burro quando foge", "laranja", "multicolorido", "cerúleo"]
    veiculos = ["carro", "moto", "bicicleta", "caminhão", "van", "ônibus", "táxi", "triciclo", "patinete", "caminhão",
                "carroça", "trenó", "mobilete", "balão"]
    animais = ["cachorro", "gato", "papagiao", "cavalo", "coelho", "rato", "tartaruga", "cobra", "hamster", "lontra",
               "capivara", "urso", "lobo", "omça", "tucano", "formiga", "cobra", "pato", "ganso", "ganso violento"]
    comidas = ["sanduíche", "maçã", "pizza", "café", "bolo", "salada", "sopa", "suco", "chá", "biscoito", "hamburguer",
               "sushi", "poke", "lamen", "pão", "gelatina", "um pirulito"]
    reacoes = ["Fiquei assustado", "Fiquei nervoso", "Não soube o que fazer", "Corri para o outro lado",
               "Chamei a polícia", "Me escondi", "Tentei ajudar", "Fiquei em choque", "Observei à distância",
               "Fiquei paralisado", "Fingi que não era comigo", "Liguei pros bombeiros",
               "Resolvi tirar a carteira de trabalho", "Corri pra igreja", "Parei de beber", "Acordei para a vida",
               "Fiquei de boa", "Achei estranho", "Achei normal", "Larguei meu trabalho",
               "Tirei foto para postar na internet", "Tirei uma selfie", "Gravei um vídeo para o Tiktok",
               "Cancelei minha redes sociais"]
    coisas_inusitadas = ["um bilhete", "uma foto", "uma luva", "um sapato", "uma corda", "um chapéu", "uma máscara",
                         "um guarda-chuva", "um vidro quebrado", "um pedaço de tecido", "um ovni", "um mascote de gato",
                         "um pato de verdade", "uma sapatilha", "um tabuleiro de Banco Imobiliário", "um par de patins",
                         "uma caixa de som", "uma peruca"]
    comentarios = ["Não parecia algo comum", "Me deixou muito preocupado", "Nunca vi algo assim antes",
                   "Não fazia sentido", "Era algo estranho", "Me fez pensar no pior", "Foi difícil de acreditar",
                   "parecia suspeito", "Me causou calafrios", "Não sei o que estava acontecendo",
                   "Me fez voltar pra igreja", "Mudei de voto", "Me benzi", "Só Jesus na causa", "Uma maluquice",
                   "É de deixar o cidadão de bem indignado", "Sem noção", "Vai trabalhar", "Quem sou eu pra julgar",
                   "Vai que dá certo", "É o novo normal", "Tem gente que acha bonito", "Parei de beber",
                   "Fiquei emocionado", "Desmaiei"]
    pessoas = ["um suspeito", "uma figura estranha", "um maluco", "um homem", "uma mulher", "um bandido", "um ladrão",
               "um juiz suspeito", "um careca", "uma doida", "um doido", "um feiticeiro", "uma feiticeira",
               "um transeunte", "um policial", "um palhaço", "um político", "um deputado"]
    # Novos templates variados
    templates = [
        "Quando me deparei com {evento} no(a) {local}, não sabia o que fazer. {reacao}.",
        "Por volta das {hora}, algo chamou minha atenção no(a) {local}: {evento}. {comentario}.",
        "Enquanto {atividade} no(a) {local}, percebi {evento} acontecendo. {reacao}.",
        "{hora} estava marcado no relógio quando {evento} ocorreu no(a) {local}. {comentario}.",
        "Nunca vou esquecer de como {evento} aconteceu no(a) {local} enquanto eu estava {atividade}. {reacao}.",
        "Ao passar pelo(a) {local}, ouvi {evento}. {reacao}.",
        "{evento} no(a) {local} foi um choque para mim, especialmente por causa de {objeto} {cor} que encontrei depois. {comentario}.",
        "Eu estava distraído(a) no(a) {local} até que vi {pessoa} {evento} às {hora}. {reacao}.",
        "{evento} no(a) {local} mudou o rumo do meu dia. {comentario}.",
        "Jamais imaginaria que {evento} ocorreria no(a) {local}, e fiquei {reacao}.",
        "Enquanto eu estava {atividade} no(a) {local}, algo estranho aconteceu: {evento}. {comentario}.",
        "Passei pelo(a) {local} por volta das {hora} e me deparei com {evento}. {reacao}.",
        "O que mais me surpreendeu foi {evento} acontecendo no(a) {local} enquanto eu estava {atividade}.",
        "A última coisa que esperava ver no(a) {local} era {evento}. {reacao}.",
        "Estava tranquilo(a) no(a) {local} até que {evento} ocorreu. {comentario}.",
        "Enquanto {atividade} no(a) {local}, ouvi claramente {evento}. {reacao}.",
        "Às {hora}, eu estava no(a) {local} quando {evento} aconteceu. {comentario}.",
        "O que presenciei no(a) {local} às {hora} foi {evento}. Nunca vi algo assim antes.",
        "O silêncio do(a) {local} foi quebrado por {evento} às {hora}. {reacao}.",
        "Nunca vou esquecer de como {evento} aconteceu no(a) {local} enquanto eu estava {atividade}. {reacao}.",
        "{hora} estava marcado no relógio quando {evento} ocorreu no(a) {local}. {comentario}.",
        "Enquanto {atividade} no(a) {local}, percebi {evento} acontecendo. {reacao}.",
        "Ao passar pelo(a) {local}, ouvi {evento}. {reacao}.",
        "{evento} no(a) {local} foi um choque para mim, especialmente por causa de {objeto} {cor} que encontrei depois. {comentario}.",
        "No instante em que {evento} ocorreu no(a) {local}, senti que algo estava errado. {comentario}.",
        "Mal havia começado a {atividade} no(a) {local} quando {evento} me surpreendeu. {reacao}.",
        "Pouco antes das {hora}, notei {evento} no(a) {local}. {comentario}.",
        "Minha atenção foi imediatamente atraída para {evento} no(a) {local}. {reacao}.",
        "Nunca imaginei que testemunharia {evento} no(a) {local}. {comentario}.",
        "A atmosfera no(a) {local} mudou completamente quando {evento} aconteceu. {reacao}.",
        "O dia parecia normal até que {evento} aconteceu no(a) {local}. {comentario}.",
        "Me lembro claramente de {evento} no(a) {local} por volta das {hora}. {reacao}.",
        "O barulho de {evento} no(a) {local} foi o que primeiro chamou minha atenção. {comentario}.",
        "Assim que {evento} ocorreu no(a) {local}, soube que algo estava errado. {reacao}.",
        "Eu estava prestes a sair do(a) {local} quando {evento} aconteceu. {reacao}.",
        "Aconteceu tão rápido: {evento} no(a) {local} me pegou de surpresa. {comentario}.",
        "Enquanto {atividade} no(a) {local}, vi claramente {evento}. {reacao}.",
        "Por volta das {hora}, {evento} no(a) {local} me deixou perplexo(a). {comentario}.",
        "Tudo parecia tranquilo no(a) {local} até que {evento} ocorreu. {reacao}.",
        "Passei pelo(a) {local} e percebi {evento} acontecendo. {comentario}.",
        "Foi assustador ouvir {evento} vindo do(a) {local} às {hora}. {reacao}.",
        "Ao ouvir {evento} no(a) {local}, imediatamente soube que algo estava errado. {comentario}.",
        "O {evento} que ocorreu no(a) {local} foi algo que jamais esquecerei. {reacao}.",
        "Eu estava {atividade} no(a) {local} quando {evento} chamou minha atenção. {comentario}.",
        "Às {hora}, {evento} no(a) {local} quebrou o silêncio do dia. {reacao}.",
        "Meus instintos me disseram para agir quando vi {evento} no(a) {local}. {comentario}.",
        "Pouco depois de começar a {atividade} no(a) {local}, ouvi {evento}. {reacao}.",
        "Mal consegui acreditar no que estava vendo: {evento} no(a) {local}. {comentario}.",
        "Estava tudo calmo até que {evento} aconteceu no(a) {local}. {reacao}.",
        "Por volta das {hora}, percebi {evento} no(a) {local} enquanto estava {atividade}. {comentario}.",
        "A tranquilidade do(a) {local} foi interrompida por {evento}. {reacao}.",
        "Não consigo esquecer de como {evento} aconteceu no(a) {local}. {comentario}.",
        "Minha reação imediata ao ver {evento} no(a) {local} foi {reacao}.",
        "Nunca imaginei que testemunharia {evento} no(a) {local} às {hora}. {comentario}.",

        "Reparei que {pessoa} realizando {evento} no(a) {local}, não sabia o que fazer. Nunca vou esquecer que ela(a) estava segurando um {objeto} {cor}.",
        "Por volta das {hora}, algo chamou minha atenção no(a) {local}: um(a) {pessoa} com um {objeto}. {comentario}.",
        "Enquanto {atividade} um(a) {pessoa} no(a) {local}, percebi {evento} acontecendo. {reacao}.",
        "{hora} estava marcado no relógio quando eu vi {pessoa} tentando roubar um {objeto} no(a) {local}. {comentario}.",
        "Nunca vou esquecer de como {pessoa} saiu do {veiculo} {cor} no(a) {local} enquanto eu estava {atividade}. {reacao}.",
        "Eu reparei que o {veiculo} {cor} estava rondando o {local}, ouvi a {pessoa} tramando um crime. {reacao}.",
        "Ver {pessoa} no(a) {local} foi um choque para mim, especialmente por causa de {objeto} {cor} que encontrei depois. {comentario}.",
        "Eu estava distraído(a) brincando com {objeto} no(a) {local} até que {evento} aconteceu às {hora}. {reacao}.",
        "O {veiculo} {cor} no(a) {local} mudou o rumo do meu dia. {comentario}.",
        "Jamais imaginaria que {pessoa} faria {evento}, e fiquei {reacao}.",
        "Enquanto eu estava entrando no {veiculo} vi {pessoa} {evento}. {comentario}.",
        "Sabia que {pessoa} tinha culpa no cartório quando {evento} no {local} por volta das {hora}. {reacao}.",
        "O que mais me surpreendeu foi {pessoa} {evento} no(a) {local}. {comentario}.",
        "A última coisa que {pessoa} esperava era ver {objeto} {cor} no {local}. {reacao}.",
        "Eu vi {pessoa} arrombando {veiculo}. {comentario}.",
        "Em pleno {hora}, um {pessoa} saiu em disparada de um {veiculo} {cor}. {comentario}.",
    ]
    # Gerando 25 depoimentos variados
    depoimentos = []
    for cpf in cpfs:
        template = random.choice(templates)
        depoimento = template.format(
            local=random.choice(locais),
            hora=random.choice(horas),
            evento=random.choice(eventos),
            objeto=random.choice(objetos),
            atividade=random.choice(atividades),
            cor=random.choice(cores),
            veiculo=random.choice(veiculos),
            animal=random.choice(animais),
            comida=random.choice(comidas),
            reacao=random.choice(reacoes),
            coisas_inusitadas=random.choice(coisas_inusitadas),
            comentario=random.choice(comentarios),
            pessoa=random.choice(pessoas),
        )
        depoimentos.append({"cpf": cpf, "depoimento": depoimento,
                            "data_depoimento": faker.date_between(datetime(2024, 1, 1), datetime(2024, 6, 30))})
    return depoimentos


def obter_lista_cpfs(db_path='MISTERIO_NOVA_LONDRES.sqlite', percent=0.1):
    conn = sqlite3.connect(db_path)  # Substitua pelo nome do seu arquivo de banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT CPF FROM RECEITA_FEDERAL")
    cpfs = [row[0] for row in cursor.fetchall()]

    # Determinando 10% dos CPF de forma aleatória e sem repetições
    quantidade_a_selecionar = max(1, int(percent * len(cpfs)))  # Garante que pelo menos 1 CPF será selecionado
    cpfs_selecionados = random.sample(cpfs, quantidade_a_selecionar)

    conn.close()
    return cpfs_selecionados


def salvar_depoimentos_no_banco(depoimentos, db_path='MISTERIO_NOVA_LONDRES.sqlite'):
    # Conectando ao banco de dados SQLite
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Dropar a tabela se ela já existir
    cursor.execute("DROP TABLE IF EXISTS DEPOIMENTOS")

    # Criar a nova tabela
    cursor.execute('''
        CREATE TABLE DEPOIMENTOS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cpf TEXT,
            depoimento TEXT,
            data_depoimento TEXT
        )
    ''')

    # Inserir os depoimentos na nova tabela
    for dep in depoimentos:
        cursor.execute('''
            INSERT INTO DEPOIMENTOS (cpf, depoimento, data_depoimento)
            VALUES (?, ?, ?)
        ''', (dep["cpf"], dep["depoimento"], dep["data_depoimento"].strftime('%Y-%m-%d')))

    # Salvar as mudanças e fechar a conexão
    conn.commit()
    conn.close()

    print(f"{len(depoimentos)} depoimentos foram inseridos na tabela DEPOIMENTOS.")


def gerar_depoimentos(db_path='MISTERIO_NOVA_LONDRES.sqlite', percent=0.2):
    cpfs = obter_lista_cpfs(db_path, percent)
    depoimentos = gerar_depoimentos_a_partir_cpfs(cpfs)
    salvar_depoimentos_no_banco(depoimentos, db_path)


if __name__ == '__main__':
    gerar_depoimentos()
