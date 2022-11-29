import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


def connect_db():
    host = os.getenv("HOST")
    database = os.getenv("DATABASE")
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    connection = psycopg2.connect(host=host, database=database,
                                  user=user, password=password)
    return connection


def consult_db(dado):
    conectando = connect_db()
    open = conectando.cursor()
    open.execute(dado)
    recset = open.fetchall()
    registros = []
    for rec in recset:
        registros.append(rec)
    conectando.close()
    return registros


def insert_db(sql):
    conectando = connect_db()
    open = conectando.cursor()
    print(sql)
    try:
        open.execute(sql)
        conectando.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print('Error: %s' % error)
        conectando.rollback()
        open.close()
        return 1


def insert_estudante(estudante):
    insert_db('insert into cadastro_estudante'
              '(nome, data_nascimento, email_contato, telefone,'
              'data_admissao, nome_responsavel, contato_responsavel,id_turma, cpf) '
              'values '
              f'(\'{estudante[0]}\', \'{estudante[1]}\', \'{estudante[2]}\', \'{estudante[3]}\','
              f' \'{estudante[4]}\', \'{estudante[5]}\', \'{estudante[6]}\', \'{estudante[7]}\','
              f' \'{estudante[8]}\')'
              )


def insert_prof(prof):
    insert_db('insert into cadastro_prof'
              '(nome, data_nascimento, cpf, email_contato, telefone,'
              'endereco, categoria_salarial, ano_contratacao) '
              'values '
              f'(\'{prof[0]}\', \'{prof[1]}\', \'{prof[2]}\', \'{prof[3]}\','
              f' \'{prof[4]}\', \'{prof[5]}\', \'{prof[6]}\', \'{prof[7]}\')'
              )
