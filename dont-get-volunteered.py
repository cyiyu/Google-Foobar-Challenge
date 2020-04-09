import math
from Queue import Queue


def findIndex(node):
    row = math.floor(node / 8)
    col = node % 8
    return row, col


def get_neighbours(row, col):
    neighbours = []
    possible = [(row - 2, col - 1), (row - 2, col + 1), (row - 1, col + 2), (row + 1, col + 2),
                (row + 2, col + 1), (row + 2, col - 1), (row + 1, col - 2), (row - 1, col - 2)]
    for row_n, col_n in possible:
        pos = (row_n, col_n)
        if (0 <= row_n <= 7) and (0 <= col_n <= 7):
            neighbours.append(pos)
    return neighbours


def solution(src, dest):
    if src == dest:
        return 0
    start = findIndex(src)
    end = findIndex(dest)
    q = Queue()
    q.put((start, 0))
    visited = [start]
    while True:
        m, count = q.get()
        if m == end:
            return count
        neighbours = get_neighbours(m[0], m[1])
        for n in neighbours:
            if n not in visited:
                visited.append(n)
                q.put((n, count + 1))
