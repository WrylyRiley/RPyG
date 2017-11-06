from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random





# Create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "White")


# Create some items
potion = Item("Potion", "potion", "heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
megaelixer = Item("Mega-Elixer", "elixer", "Fully restores HP/MP of all party members", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

# Create player spells
player_spells = [fire, thunder, blizzard, meteor, cure, cura]
enemy_spells = [fire, thunder, blizzard]
player_items = [{"item":potion, "quantity": 15},{"item":hipotion, "quantity": 5},
                {"item":superpotion, "quantity": 5},{"item":elixer, "quantity": 5},
                {"item":megaelixer, "quantity": 2},{"item":grenade, "quantity": 5}]


# Instantiate People
player1 = Person("Valos :", 460, 65, 60, 34, player_spells, player_items)
player2 = Person("Nick  :", 460, 65, 60, 34, player_spells, player_items)
player3 = Person("Robot :", 460, 65, 60, 34, player_spells, player_items)

players= [player1, player2, player3]

# Instantiate Enemies
enemy1 = Person("Magus :", 1200, 65, 45, 25, enemy_spells, [])
enemy2 = Person("Vern  :", 1000, 60, 55, 35, enemy_spells, [])

enemies = [enemy1, enemy2]


# Create action functions

def attack(player, target):
    print("You chose: Attack")
    dmg = player.generate_damage()
    enemies[target].take_damage(dmg)
    print(player.name + " attacked for", dmg, "points of damage.")

    return True

def magic(player, target, is_enemy):
    magic_choice = 0

    if is_enemy is False:
        player.choose_magic()
        magic_choice = int(input("Choose magic:")) - 1

        if magic_choice == -1:
            return False
    else:
        magic_choice = random.randrange(0, player.magic.length - 1)

    print("You chose: Magic")

    spell = player.magic[magic_choice]
    magic_dmg = spell.generate_damage()

    current_mp = player.get_mp()
    if spell.cost > current_mp:
        print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
        return False

    player.reduce_mp(spell.cost)

    if spell.type == "white":
        player.heal(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
    elif spell.type == "black":
        enemies[target].take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

    return True


def items(player):
    player.choose_item()
    item_choice = int(input("Choose Item: ")) - 1

    if item_choice == -1:
        return False

    item = player.items[item_choice]["item"]

    if player.items[item_choice]["quantity"] == 0:
        print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
        return False

    player.items[item_choice]["quantity"] -= 1

    if item.type == "potion":
        player.heal(item.prop)
        print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
    elif item.type == "elixer":
        if (item.name == 'megaelixer'):
            for player_all in players:
                player_all.hp = player_all.maxhp
                player_all.mp = player_all.maxmp
        player.hp = player.maxhp
        player.mp = player.maxmp
        print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP & MP" + bcolors.ENDC)

    elif item.type == "attack":
        enemies[target].take_damage(item.prop)
        print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage" + bcolors.ENDC)

    return True

def end_game_check():
    player_sum = 0
    enemy_sum = 0
    for player in players:
        player_sum + player.hp
    for enemy in enemies:
        enemy_sum += enemy.hp
    if player_sum == 0:
        print(bcolors.OKGREEN + "All players have been defeated. enemies win!" + bcolors.ENDC)
        running = False
    if enemy_sum == 0:
        print(bcolors.FAIL + "All enemies have been defeated, players win!" + bcolors.ENDC)
        running = False

running = True

print(bcolors.FAIL + bcolors.BOLD + "ENEMY ATTACKS!" + bcolors.ENDC)
while running:
    print("===========================")

    print("\n\n")
    print("PLAYER    HP                                       MP")

    for player in players:
        player.get_stats()

    print("\n\n")
    print("ENEMY     HP                                       MP")

    for enemy in enemies:
        enemy.get_stats()

    print("\n")

    for player in players:
        player.choose_action()
        index = int(input("Choose an action")) - 1
        target = int(input("Choose an Enemy")) - 1
        action_result = True


        if index == 0:
            action_result = attack(player, target)

        elif index == 1:
            action_result = magic(player, target, False)

        elif (index == 2):
            action_result = items(player)

        if action_result == False:
            continue

    end_game_check()
    if running == False:
        continue

    for enemy in enemies:
        action_result - True
        action = random.randrange(0, 1)
        target = random.randrange(0, len(players) - 1)

        if action is 0:
            action_result = attack(enemy, target)
        elif action is 1:
            action_result = magic(enemy, target, True)

        if action_result == False:
            continue


    end_game_check()
    if running == False:
        continue




