from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, reduce
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations, product
from math import ceil, comb, factorial, gcd, isclose, lcm

from algo import a_star, custsort, merge_ranges, sssp
from constants import EPSILON, HUGE
from helpers import adjacent, between, chunks, chunks_with_overlap, columns, digits, dimensions, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded, overlap, positives, rays, rays_from_inside, words


def parse(lines):
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if lines[y][x] == 'S':
                return y, x
    

def solve_a(lines):
    h, w = dimensions(lines)
    sy, sx = parse(lines)

    seen = defaultdict(set)
    numsteps = 64

    frontier = [(0, sy, sx)]

    for steps, y, x in frontier:
        if (y, x) in seen[steps]:
            continue

        seen[steps].add((y, x))

        if steps == numsteps:
            continue

        for ny, nx in neighs_bounded(y, x, 0, h-1, 0, w-1):
            if lines[ny][nx] == '#' or (ny, nx) in seen[steps+1]:
                continue

            frontier.append((steps+1, ny, nx))


    return len(seen[numsteps])


def solve_b(lines):
    h, w = dimensions(lines)
    sy, sx = parse(lines)

    seen = defaultdict(set)
    numsteps = 6

    this_gen = defaultdict(int)
    this_gen[(sy, sx)] = 1    
    next_gen = defaultdict(int)

    for step in range(numsteps+1):
        if step % 1000 == 0:
            print(step)
        if step == numsteps:
            return multall(this_gen.values())
        for pos, num in this_gen.items():
            y, x = pos

            for ny, nx in neighs(y, x):
                if lines[ny%h][nx%w] == '#':
                    continue

                next_gen[(ny%h, nx%w)] += num

        this_gen = next_gen
        next_gen = defaultdict(int)


def main():
    lines = []

    with open('21.txt') as f:
        for line in f.readlines():
            lines.append(line.rstrip())
            
    return (solve_a(lines), solve_b(lines))


if __name__ == '__main__':
    print(main())
