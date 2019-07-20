

class Person:
    def __init__(self, damage, health, armor):
        self.damage = damage
        self.health = health
        self.armor = armor

class Player(Person):
    def __init__(self, damage, health, armor):
        Person.__init__(self, damage, health, armor)
class Enemy(Person):
    def __init__(self, damage, health, armor):
        Person.__init__(self, damage, health, armor)


class Fight:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def _start(self, player, enemy):
        while player.health > 0 or enemy.health > 0:

            dam1 = enemy.health - (player.damage / enemy.armor)
            enemy.health = dam1
            dam2 = player.health - (enemy.damage / player.armor)
            player.health = dam2
            if enemy.health == 0:
                print('Вы победили!')
                break
            if player.health == 0:
                print('Вы проиграли!')
                break


player = Player(1, 5, 2)
enemy = Enemy(5, 10, 2)

new_fight = Fight(player, enemy)
new_fight._start(player, enemy)





