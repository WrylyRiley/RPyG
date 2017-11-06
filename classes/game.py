import random
import math
from classes.magic import Spell


class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack","Magic", "Items"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost




    def choose_action(self):
        print ("\n" + "    " + bcolors.BOLD + self.name + bcolors.ENDC)
        print((bcolors.OKBLUE + bcolors.BOLD + "    ACTIONS:" + bcolors.ENDC))
        i = 1
        for item in self.actions:
            print ("    " + str(i), ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print((bcolors.OKBLUE + bcolors.BOLD + "    MAGIC:" + bcolors.ENDC))
        for spell in self.magic:
            print("    " + str(i), ":", spell.name, "(cost:", str(spell.cost) + ")")
            i+=1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print("    " + str(i) + ".", item["item"].name, ":",
                  item["item"].description, ": (x" + str(item["quantity"]) + ")")
            i+=1

    def get_stats(self):
        hp_pct = (self.hp / self.maxhp) #HP Percentage
        mp_pct = (self.mp / self.maxmp) #MP Percentage
        hp_bar = math.ceil(25 * hp_pct) #Bar percentage, rounded up
        mp_bar = math.ceil(10 * mp_pct) #Bar percentage, rounded up
        hp_bar_white = 25 - hp_bar
        mp_bar_white = 10 - mp_bar

        hp_render = '  |'
        hp_render += '=' * hp_bar
        hp_render += ' ' * hp_bar_white
        hp_render += '|  '

        mp_render = '  |'
        mp_render += '=' * mp_bar
        mp_render += ' ' * mp_bar_white
        mp_render += '|'

        hp_num = str(self.hp) + "/" + str(self.maxhp)
        hp_gap = " " * (11 - len(hp_num))

        mp_num = str(self.mp) + "/" + str(self.maxmp)
        mp_gap = " " * (7 - len(mp_num))

        print("                     _________________________             __________")
        print(bcolors.BOLD + self.name + hp_gap + hp_num + bcolors.OKGREEN + hp_render + bcolors.ENDC + bcolors.BOLD + mp_gap + mp_num + bcolors.OKBLUE + mp_render + bcolors.ENDC)
