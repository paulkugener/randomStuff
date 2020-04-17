#!/usr/bin/python3

import math
import random

# estimate pi
# source: https://www.youtube.com/watch?v=pvimAM_SLic

def estimate_pi(n):
    num_point_circle = 0
    num_point_total = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            num_point_circle += 1
        num_point_total += 1
    return 4 * num_point_circle / num_point_total


if __name__ == "__main__":
    print(estimate_pi(1_000_000))
