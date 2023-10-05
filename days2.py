from os import system

system('cls')

number = int(input('Informe um dia da semana [1-7]: '))

match (number):
    case 1:
        print('Segunda-Feira')
    case 2:
        print('Terça-Feira')
    case 3:
        print('Quarta-Feira')
    case 4:
        print('Quinta-Feira')
    case 5:
        print('Sexta-Feira')
    case 6:
        print('Sabádo')
    case 7:
        print('Domingo')
    case _:
        print('Número inválido')
