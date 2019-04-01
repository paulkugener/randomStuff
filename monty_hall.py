from enum import Enum
import random, time

class Door(Enum):
    CAR = 1
    GOAT = 2

def playGame(swap):
	# create doors and shuffle
    deck = [Door.CAR, Door.GOAT, Door.GOAT]
    random.shuffle(deck)
    # player chooses a door at random
    playerPick = deck.pop(random.randrange(len(deck)))
    # host discards one of the remaining goats
    deck.remove(Door.GOAT)
    # player behaves according to his strategy
    if swap:
        if deck[0] == Door.CAR:
            #print("player wins!")
            return True
    else:
        if playerPick == Door.CAR:
            #print("player wins!")
            return True
    # print("player looses!")
    return False
    

def main():
    startTime = time.time()
    numberOfTests = 1_000_000
    noSwapNumberOfWins = 0
    swapNumberOfWins = 0

    print("running {:,} tests...".format(numberOfTests))

    for _ in range(numberOfTests):
        if playGame(False):
            noSwapNumberOfWins = noSwapNumberOfWins + 1
        if playGame(True):
            swapNumberOfWins = swapNumberOfWins + 1

    print("Strategy 1: no swap")
    print("noSwapNumberOfWins = {:,}".format(noSwapNumberOfWins))
    print("noSwapNumberOfWins / {:,} = {:.4f}".format(numberOfTests, noSwapNumberOfWins / numberOfTests))
    print("Strategy 2: swap")
    print("swapNumberOfWins = {:,}".format(swapNumberOfWins))
    print("swapNumberOfWins / {:,} = {:.4f}".format(numberOfTests, swapNumberOfWins / numberOfTests))
    print("elapsed time = {:.2f} sec".format(time.time() - startTime))


if __name__ == '__main__':
    main()
