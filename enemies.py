# coding: utf-8
# license: GPLv3
__author__ = 'Home'

from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer
    def question(self):
        self._color=''
        self.__quest=''
        return self.__quest


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest
class BlackDragon(Dragon):
    def __init__(self):
        self._health=500
        self._attack=50
        self._color='чёрный'
    def question(self):
           x = randint(1,100)
           y = randint(1,100)
           self.__quest= str(x)+'*'+str(y)
           self.set_answer(x*y)
           return self.__quest
class RedDragon(Dragon):
    def __init__(self):
        self._health=300
        self._attack=20
        self._color='красный'
    def question(self):
           x = randint(1,100)
           y = randint(1,100)
           self.__quest= str(x)+'-'+str(y)
           self.set_answer(x-y)
           return self.__quest

class Troll(Enemy):
    def set_answer(self,answer):
        self.__anwer=answer
    def check_answer(self,answer):
        return self.__anwer==answer
    def question(self):
        self.__quest=''
        self.name=''
        return self.__quest


class RandomTroll(Troll):
    def __init__(self):
        self._health=100
        self._attack=10
        self.name='рандомный'
    def question(self):
        x=randint(1,6)
        self.__quest='Угадай число от 1 до 5'
        self.set_answer(x)
        return self.__quest
enemy_types = [GreenDragon, RedDragon, BlackDragon,RandomTroll]

#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.


enemy_types = [GreenDragon, RedDragon, BlackDragon]
