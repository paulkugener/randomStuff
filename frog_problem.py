# problem source: https://www.youtube.com/watch?v=ZLTyX4zL2Fc

import random
import time

def play():
    location = 0
    jump_counter = 0
    while location < 10:
        jump_counter += 1
        location = random.randint(location + 1, 10)
    #print("frog arrived at bank after", jump_counter, "jumps.")
    return jump_counter

def main():
    # do tests; compute average jumps to reach destination; print information
    start_time = time.time()
    num_tests = 10_000_000
    num_jumps = 0

    print("running {:,} tests...".format(num_tests))

    for _ in range(num_tests):
    	num_jumps += play()

    print("num_jumps = {:,}".format(num_jumps))
    print("num_jumps / {:,} = {:.4f}".format(num_tests, num_jumps / num_tests))
    print("elapsed time = {:.2f} sec".format(time.time() - start_time))


if __name__ == '__main__':
    main()
