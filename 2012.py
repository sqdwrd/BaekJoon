from sys import stdin

def input():
    return stdin.readline()

def diff(A: int, B: int) -> int:
    return abs(A - B)

def calculate_diff(l_aligned: list) -> int:
    sum = 0
    for a, b in zip(l_aligned, range(1, len(l_aligned) + 1)):
        sum += diff(a, b)
    return sum


def main():
    N = int(input())
    expections = []

    for _ in range(N):
        expections.append(int(input()))
    expections.sort()

    answer = calculate_diff(expections)
    print(answer)


if __name__ == "__main__":
    main()
