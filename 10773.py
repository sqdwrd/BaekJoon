import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    k = int(input())
    result = process_next(k)

    answer = 0

    for i in result:
        answer = answer + i

    return answer


def process_next(k, numbers: list[int] = []):
    if k == 0:
        return numbers

    cmd = int(input())
    if (cmd == 0):
        numbers.pop()
    else:
        numbers.append(cmd)

    return process_next(k - 1, numbers)


if __name__ == "__main__":
    print(main())
