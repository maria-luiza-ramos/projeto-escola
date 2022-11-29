from visual import menu, line
from connect_db import consult_db

# Fazer conexão com banco de dados
# Será que precisa criar turma por aqui ??
# Talvez seja melhor deixar o menu com turma 1, turma 2 e turma 3
# Quando cadastro no novo aluno como fazer o nome dele ir direto para banco da turma certa


def menu_turmas():
    while True:
        abas = ['TURMA 01', 'TURMA 02', 'TURMA 03', 'SAIR']

        escolha = menu(abas)

        if escolha == 'TURMA 01':
            turma_1 = consult_db('select * from turma_1')
            print(line())
            for c in turma_1:
                print(c[0])
            print(line())

        elif escolha == 'TURMA 02':
            turma_2 = consult_db('select * from turma_2')
            print(line())
            for l in turma_2:
                print(l[0])
            print(line())

        elif escolha == 'TURMA 03':
            dados = consult_db('select * from turma_3')
            print(line())
            for linha in dados:
                print(linha[0])
            print(line())

        elif escolha == 'SAIR':
            break
