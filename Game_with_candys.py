import random

greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
    'Основные правила игры: '
    'Нам будет дана 2021 конфета, '
    'за один ход мы можем взять не более 28 конфет, '    
    'Играем!')


messages = ['Ваша очередь брать конфеты', 'возьмите конфеты', 
            'сколько конфет возьмёте?', 'Берите пока не слипнется :) ', 'Ваш ход']


n = 2021
m = 28

def play_game(n, m, players, messages):
    count = 0
    if n%10 == 1 and 9 > n > 10: letter = 'a'
    elif 1 < n%10 < 5 and 9 > n > 10: letter = 'ы'
    else: letter = ''
    while n > 0:
        print(f'{players[count%2]}, {random.choice(messages)}')
        move = int(input())
        if move > n or move > m:
            print(f'Это много, можно взять не больше {m} конфет{letter}, у нас всего {n} конфет{letter}')
            attempt = 3
            while attempt > 0:
                if n >= move <= m:
                    break
                print(f'Попробуй еще раз, у тебя {attempt} попытки')
                move = int(input())
                attempt -=1
            else:
                return print(f'Не осталось попыток! Конец игры...')
        n = n - move
        if n > 0: print(f'Осталось {n} конфет{letter}')
        else: print('Все конфеты разобраны')
        count +=1
    return players[not count%2]

print(greeting)

player1 = input('Имя первого игрока: ')
player2 = input('Имя второго игрока: ')
players = [player1, player2]

winer = play_game(n, m, players, messages)
print(f'В игре победил {winer}!')                  