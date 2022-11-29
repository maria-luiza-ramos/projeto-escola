from visual import menu, header
from students import menu_estudante
from teacher import menu_professores
from team import menu_turmas




def menu_principal():
    while True:
        header('ESCOLA PRIMAVERA')
        escolha = menu(['ESTUDANTES', 'TURMAS', 'PROFESSORES', 'SAIR'])
        if escolha == "ESTUDANTES":
            menu_estudante()
        elif escolha == "TURMAS":
            menu_turmas()
        elif escolha == "PROFESSORES":
            menu_professores()
        elif escolha == "SAIR":
            print("FINALIZADO")
            break


if __name__ == "__main__":
    menu_principal()
