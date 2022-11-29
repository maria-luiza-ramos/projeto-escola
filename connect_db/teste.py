from connect_db import consult_db

if __name__ == "__main__":
    cadastro_novo = []
    sumario = ['nome', 'data_nascimento', 'email_contato', 'telefone',
               'data_admissao', 'nome_responsavel', 'contato_responsavel',
               'id_turma', 'cpf']
    for i in sumario:
        dado = str(input(f'Preencha {i} do/a estudante: '))
        cadastro_novo.append(dado)
    print(cadastro_novo)