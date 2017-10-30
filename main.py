from classes.game import Person, bcolors


magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True

print(bcolors.FAIL + bcolors.BOLD + "ENEMY ATTACKS!" + bcolors.ENDC)
while running:
    print("===========================")
    player.choose_action()
    index = int(input("Choose an action")) - 1
    print("You chose:", index)

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        index = int(input("Choose magic")) - 1


    enemy_choice = 0
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "Player HP:", player.get_hp())



    running = False