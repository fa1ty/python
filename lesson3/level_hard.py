def damage_count(player_date, enemy_date):
    n = 1
    while player_date['health'] > 0 or enemy_date['health'] > 0:
        if n == 1:
            dam1 = enemy_date['health'] - player_date['damage']
            enemy_date['health'] = dam1
            if enemy_date['health'] == 0:
                print('Вы победили')
                break

        if n == 2:
            dam2 = player_date['health'] - (enemy_date['damage']/player_date['armor'])
            player_date['health'] = dam2
            if player_date['health'] == 0:
                print('Вы проиграли')
                break
        if n == 1:
            n == 2
        else:
            n == 1


player_name = input('Введите имя: ')
player_date = {'name': player_name, 'health': 100, 'armor': 1.2, 'damage': 50}
enemy_date = {'name': 'enemy', 'health': 2000, 'damage': 2}
damage_count(player_date, enemy_date)
