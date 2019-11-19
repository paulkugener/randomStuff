#! python3

import random

# source: https://www.youtube.com/watch?v=a1DUUnhk3uE

class Prisoner:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

def play_game_rnd(prisoner_list, cards):
    random.shuffle(cards)
    for _ in range(0, 10):
        for p in prisoner_list:
            choice = random.sample(cards, 5)
            if p.name not in choice:
                return False
            else:
                pass
    return True

def play_game_with_strategy(prisoner_list, cards):
    random.shuffle(cards)
    for _ in range(0, 10):
        for p in prisoner_list:
            choice = []
            choice.append(cards[p.name])
            for _ in range(4):
                choice.append(cards[choice[-1]])
            if p.name not in choice:
                return False
            else:
                pass
    return True

if __name__ == "__main__":
    prisoner_list = []
    cards = []
    for i in range(0, 10):
        p = Prisoner(i)
        prisoner_list.append(p)
        cards.append(i)
    number_of_games = 1_000_000
    number_of_rnd_wins = 0
    number_of_strategy_wins = 0
    for g in range(number_of_games):
        if play_game_rnd(prisoner_list, cards):
            number_of_rnd_wins += 1
        if play_game_with_strategy(prisoner_list, cards):
            number_of_strategy_wins += 1
        print('game', g, 'of', number_of_games, '| rnd wins =', number_of_rnd_wins, '| strategy wins =', number_of_strategy_wins, end='\r', flush=True)
