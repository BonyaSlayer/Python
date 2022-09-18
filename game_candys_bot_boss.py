from random import randint, choice

greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
    'Основные правила игры: '
    'Нам будет дана 2021 конфета, '
    'за один ход мы можем взять не более 28 конфет, '    
    'Играем!')


messages = ['Ваша очередь брать конфеты', 'возьмите конфеты', 
            'сколько конфет возьмёте?', 'Берите пока не слипнется :) ', 'Ваш ход']


def hi_time():
    player1 = input('Имя игрока: ')
    player2 = 'Сладкоежка'
    print(f'Привет, а меня зовут {player2}')
    return [player1, player2]

def rules_of_game(players):
    n = 2021
    m = 28
    first = int(input(
        f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
    if first != 1:
        first = 0
    return [n, m, int(first)]

    
def play_game(rules, players, messages):
    count = rules[2]
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'a'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'
    else:
        letter = ''        
    while rules[0] > 0:
        if not count % 2:
            move = rules[0] % rules[1] + 1
            print(f'Я беру {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(f'Это много, можно взять не больше {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
                print(f'Попробуй еще раз')
                move = int(input())                                        
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{letter}')
        else: 
            print('Все конфеты разобраны')
        count += 1
    return players[count%2]

        

print(greeting)

players = hi_time()
rules = rules_of_game(players)



winer = play_game(rules,  players, messages)
if not winer:
    print('Никто не выиграл')
else: print(f'В игре победил {winer}!')