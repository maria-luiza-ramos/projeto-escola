def line():
    return '-' * 30


def header(txt):
    print(line())
    print(txt.center(30))
    print(line())


def menu(list):
    for c, i in enumerate(list):
        print(f'{c + 1} - {i}')
    print(line())
    escolha = 0
    while escolha > len(list) or escolha < 1:
        escolha = int(input('Digite o n para acessar mais detalhes: '))
        if escolha > len(list) or escolha < 1:
            print("Opção invalida")
    return list[escolha - 1]
