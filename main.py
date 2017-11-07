import random

from classes.game import Person, bcolors
from classes.inventory import Item
from classes.magic import Spell

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
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": megaelixer, "quantity": 2}, {"item": grenade, "quantity": 5}]

# Instantiate People
player1 = Person("Valos :", 460, 65, 60, 34, player_spells, player_items)
player2 = Person("Nick  :", 460, 65, 60, 34, player_spells, player_items)
player3 = Person("Robot :", 460, 65, 60, 34, player_spells, player_items)

players = [player1, player2, player3]

# Instantiate Enemies
enemy1 = Person("Magus :", 1200, 65, 45, 25, enemy_spells, [])
enemy2 = Person("Vern  :", 1000, 60, 55, 35, enemy_spells, [])

enemies = [enemy1, enemy2]


# Create action functions
# Attack
def attack(player_atk, is_enemy):
    print("You chose: Attack")
    dmg = player_atk.generate_damage()
    if is_enemy:
        players[random.randrange(0, len(players) - 1)].take_damage(dmg)
    else:
        enemies[choose_enemy()].take_damage(dmg)
    print(player_atk.name + " attacked for", dmg, "points of damage.")

    return True


# Magic
def magic(player_mag, is_enemy):
    if is_enemy:
        magic_choice = random.randrange(0, len(player_mag.magic) - 1)
    else:
        player_mag.choose_magic()
        while True:

            magic_choice = int(input("Choose magic:")) - 1

            if magic_choice is -1:
                return False

            if magic_choice < -1 or magic_choice > len(player_mag.magic) - 1:
                print(bcolors.BOLD + bcolors.FAIL + "Invalid entry, try again!" + bcolors.ENDC)
                continue

            break

    spell = player_mag.magic[magic_choice]
    magic_dmg = spell.generate_damage()

    current_mp = player_mag.get_mp()
    if spell.cost > current_mp:
        print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
        return False

    player_mag.reduce_mp(spell.cost)

    if spell.type is "white":
        player_mag.heal(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
    elif spell.type is "black":
        if is_enemy:
            players[random.randrange(0, len(players) - 1)].take_damage(magic_dmg)
        else:
            enemies[choose_enemy()].take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

    return True


# Items
def items(player_it, is_enemy):
    player_it.choose_item()
    item_choice = int(input("Choose Item: ")) - 1

    if item_choice is -1:
        return False

    item = player_it.items[item_choice]["item"]

    if player_it.items[item_choice]["quantity"] is 0:
        print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
        return False

    player_it.items[item_choice]["quantity"] -= 1

    if item.type is "potion":
        player_it.heal(item.prop)
        print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
    elif item.type is "elixer":
        if item.name is 'megaelixer':
            for player_all in players:
                player_all.hp = player_all.maxhp
                player_all.mp = player_all.maxmp
        player_it.hp = player.maxhp
        player_it.mp = player.maxmp
        print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP & MP" + bcolors.ENDC)

    elif item.type is "attack":
        if is_enemy:
            players[random.randrange(0, len(players) - 1)].take_damage(item.prop)
        else:
            enemies[choose_enemy()].take_damage(item.prop)
        print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage" + bcolors.ENDC)

    return True


def choose_enemy():
    i = 1
    for x in enemies:
        if x.hp > 0:
            print(str(i) + " : " + x.name)
            i += 1

    while True:
            try:
                choice = int(input("Choose an Enemy")) - 1
                if choice < 0 or choice > i:
                    print(bcolors.BOLD + bcolors.FAIL + "Invalid entry, try again!" + bcolors.ENDC)
                    continue
                break
            except ValueError:
                print(bcolors.BOLD + bcolors.FAIL + "Invalid entry, try again!" + bcolors.ENDC)
    return choice


# End game check
def end_game_check():
    global running
    player_sum = 0
    enemy_sum = 0
    for x in players:
        player_sum += x.hp
    for x in enemies:
        enemy_sum += x.hp
    if player_sum is 0:
        print(bcolors.OKGREEN + "All players have been defeated. enemies win!" + bcolors.ENDC)
        running = False
    if enemy_sum is 0:
        print(bcolors.FAIL + "All enemies have been defeated, players win!" + bcolors.ENDC)
        running = False


running = True

print(bcolors.FAIL + bcolors.BOLD + "ENEMY ATTACKS!" + bcolors.ENDC)
while running:
    print("===========================")
    print("\n")
    print("PLAYER    HP                                       MP")

    for player in players:
        player.get_stats()

    print("\n\n")
    print("ENEMY     HP                                       MP")

    for enemy in enemies:
        enemy.get_stats()

    print("\n")
    for player in players:
        if player.hp is 0:
            continue
        while True:
            action_result = True
            player.choose_action()
            while True:
                try:
                    index = int(input("Choose an action")) - 1
                    break
                except ValueError:
                    print(bcolors.BOLD + bcolors.FAIL + "Invalid entry, try again!" + bcolors.ENDC)
                    continue

            if index is 0:
                action_result = attack(player, False)

            elif index is 1:
                action_result = magic(player, False)

            elif index is 2:
                action_result = items(player, False)

            else:
                print(bcolors.BOLD + bcolors.FAIL + "Invalid selection, try again!" + bcolors.ENDC)
                continue

            if action_result is False:
                continue

            break

    end_game_check()
    if running is False:
        continue

    for enemy in enemies:
        if enemy.hp is 0:
            continue
        action_result = True
        action = random.randrange(0, 1)

        if action is 0:
            action_result = attack(enemy, True)
        elif action is 1:
            action_result = magic(enemy, True)

        if action_result is False:
            continue

    end_game_check()
    if running is False:
        continue
