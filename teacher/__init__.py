from visual import menu, line
from connect_db import consult_db, insert_prof


def menu_professores():
    while True:
        abas = ['PROFESSORES CADASTRADOS', 'CADASTRAR NOVO PROFESSOR', 'SAIR']
        escolha = menu(abas)
        if escolha == 'PROFESSORES CADASTRADOS':
            dados = consult_db('select * from cadastro_prof')
            print(line())
            for linha in dados:
                print(linha[0])
            print(line())
        elif escolha == 'CADASTRAR NOVO PROFESSOR':
            cadastro_novo = []
            sumario = ['nome', 'data_nascimento', 'cpf', 'email_contato', 'telefone',
                       'endereco', 'categoria_salarial', 'ano_contratacao']
            for i in sumario:
                dado = str(input(f'Preencha {i} do/a professor: '))
                cadastro_novo.append(dado)
            insert_prof(cadastro_novo)
        elif escolha == 'SAIR':
            break
