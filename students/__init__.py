from connect_db import consult_db, insert_estudante
from visual import menu, line


def menu_estudante():
    while True:
        abas = ['ESTUDANTES CADASTRADOS', 'CADASTRAR NOVO ESTUDANTE', "SAIR"]
        escolha = menu(abas)
        if escolha == 'ESTUDANTES CADASTRADOS':
            dados = consult_db('select * from cadastro_estudante')
            print(line())
            for linha in dados:
                print(linha[0])
            print(line())
        elif escolha == 'CADASTRAR NOVO ESTUDANTE':
            cadastro_novo = []
            sumario = ['nome', 'data_nascimento', 'email_contato', 'telefone',
                       'data_admissao', 'nome_responsavel', 'contato_responsavel',
                       'id_turma', 'cpf']
            for i in sumario:
                dado = str(input(f'Preencha {i} do/a estudante: '))
                cadastro_novo.append(dado)
            insert_estudante(cadastro_novo)
        elif escolha == "SAIR":
            break


# Posso mudar a maneira como mostra os estudantes. Colocar a busca por nome