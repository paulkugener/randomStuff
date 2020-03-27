# problem source: https://www.youtube.com/watch?v=sf5OrthVRPA
# We have a deck of playing cards. The deck gets shuffled.
# How likely is it that a queen is in the neighborhood of a king?

import random
import time

def play(proximity: int):
    deck = ["1h", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "10h", "Jh", "Qh", "Kh",
            "1t", "2t", "3t", "4t", "5t", "6t", "7t", "8t", "9t", "10t", "Jt", "Qt", "Kt",
            "1c", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "10c", "Jc", "Qc", "Kc",
            "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "Jp", "Qp", "Kp"
           ]
    random.shuffle(deck)
    for k in ["Kh", "Kt", "Kc", "Kp"]:
        idx = deck.index(k)
        neighbors = []
        for p in range(1, proximity+1):
            neighbors.append(max(0, idx-p))
            neighbors.append(min(len(deck)-1, idx+p))
        for n in neighbors:
            if deck[n].startswith("Q"):
                return True
    return False

def main():
    # do tests; compute average chance of being neighbors; print information
    start_time = time.time()
    num_tests = 1_000_000
    num_positif = 0

    print("running {:,} tests for different proximities...\n".format(num_tests))

    for p in [1,2,3,4]:
        print("test with proximity(" + str(p) + ")")
        start_time = time.time()
        num_positif = 0
        for _ in range(num_tests):
            if play(p):
                num_positif += 1

        print("num_positif = {:,}".format(num_positif))
        print("num_positif / {:,} = {:.4f}".format(num_tests, num_positif / num_tests))
        print("elapsed time = {:.2f} sec\n".format(time.time() - start_time))


if __name__ == '__main__':
    main()
