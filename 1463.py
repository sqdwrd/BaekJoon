from typing import List
import sys

N = int(input())

mem: List[int] = [None for _ in range(N+1)]


def setMem(index, value):
    mem[index - 1] = value


def getMem(index):
    return mem[index - 1]


setMem(1, 0)


def getMinEpoch(n: int) -> int:
    value = sys.maxsize
    if (n % 2 == 0):
        case = getMem(int(n / 2)) + 1
        value = case

    if (n % 3 == 0):
        case = getMem(int(n / 3)) + 1
        if (case < value):
            value = case

    case = getMem(n - 1) + 1
    if (case < value):
        value = case

    assert value != sys.maxsize
    return value


for n in range(2, N+2):
    epoch = getMinEpoch(n)
    setMem(n, epoch)

print(getMem(N))
