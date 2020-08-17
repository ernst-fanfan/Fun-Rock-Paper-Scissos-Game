# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# menu
import random as rd
def menu():
    print('\n1-Play game')
    print('2-Exit')
    choice = input()
    if choice =='1' or choice == '2':
        return int(choice)
    else:
        print('Invalid input')
        return 3

# player loader
def player_loader(gamers):
    name = str(input('\nEnter player name: '))
    gamers[name] = {'score': 0, 'hand': 0}

# choice loader
def pick_hand(gamers, player):
    hand = -1
    print(player)
    while hand < 0 or hand > 3:
        hand = int(input('\nPick:\n1-Rock\n2-Paper\n3-Scissors\n:'))
        if (hand < 0 or hand > 3):
            print('Invalid input')
        else:
            gamers[player]['hand'] = choices[hand - 1]

# score
def score(gamers):
    players = list(gamers.keys())
    gamers[players[0]]['score'], gamers[players[1]]['score'] = compare(gamers[players[0]]['hand'], gamers[players[1]]['hand'])

# cpu
def cpu_pick(gamers, player):
    gamers[player]['hand'] = choices[rd.randint(0, 2)]

#compare
def compare(h1, h2):
    if h1 == 'rock' and h2 == 'paper':
        return [0,1]
    if h1 == 'paper' and h2 == 'scissors':
        return [0,1]
    if h1 == 'scissor' and h2 == 'rock':
        return [0,1]
    if h2 == 'rock' and h1 == 'paper':
        return [1,0]
    if h2 == 'paper' and h1 == 'scissors':
        return [1,0]
    if h2 == 'scissors' and h1 == 'rock':
        return [1,0]
    if h1 == h2:
        return [0,0]

# game manager
def game():
    play = True
    while play:
        gamers = {}
        c = menu()
        if c == 2:
            play = False
        elif c == 1:
            player_loader(gamers)
            gamers['cpu'] = {'score': 0, 'hand': 0}
            players = list(gamers.keys())
            for player in players:
                if player == 'cpu':
                    cpu_pick(gamers, player)
                else:
                    pick_hand(gamers, player)
            score(gamers)
            print(display(gamers))

#display msg
def display(gamers):
    msg = ''
    for player in list(gamers.keys()):
        if gamers[player]['score'] == 1:
            msg = msg + '{} has won!! '.format(player)
        else:
            msg = msg + '{} has lost!! '.format(player)
    if msg.count('lost') == 2:
        msg = 'It is a tie!!'
    return msg

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    choices = ['rock', 'paper', 'scissors']
    # intro
    print('***********************')
    print('*Rock, Paper, Scissors*')
    print('***********************')

    game()
