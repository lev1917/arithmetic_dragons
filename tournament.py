# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    for i  in range(len(dragon_list)):
        if isinstance(dragon_list[i], Dragon):
            dragon=dragon_list[i]
            print('Вышел', dragon._color, 'дракон!')
            while dragon.is_alive() and hero.is_alive():
                print('Вопрос:', dragon.question())
                answer = annoying_input_int('Ответ:')
                if dragon.check_answer(answer):
                     hero.attack(dragon)
                     print('Верно! \n** дракон кричит от боли **')
                else:
                    dragon.attack(hero)
                    print('Ошибка! \n** вам нанесён удар... **')
            if dragon.is_alive():
                    break
            print('Дракон', dragon._color, 'повержен!\n')
        if isinstance(dragon_list[i],Troll):
            troll=dragon_list[i]
            print('вышел', troll.name, 'тролль')
            while troll.is_alive() and hero.is_alive():
                print('вопрос',troll.question())
                answer = annoying_input_int('Ответ:')
                if troll.check_answer(answer):
                    hero.attack(troll)
                    print('Ура! \n** тролль ранен')
                else:
                    troll.attack(hero)
                    print('Дурак!')
            if troll.is_alive():
                break
            print(troll.name, 'тролль повержен!')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        dragon_number = 4
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == 4)
        print('У Вас на пути', dragon_number, 'драконов и тролей!')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
