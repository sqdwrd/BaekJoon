import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def main():
    k = int(input())
    cmd_queue = []
    for _ in range(k):
        cmd_queue.append(int(input()))

    result = process_next(cmd_queue)
    answer = 0

    for i in result:
        answer = answer + i

    return answer


def process_next(cmd_queue: list[int], numbers: list[int] = []):
    if len(cmd_queue) == 0:
        return numbers

    cmd = cmd_queue.pop(0)
    if (cmd == 0):
        numbers.pop()
    else:
        numbers.append(cmd)

    return process_next(cmd_queue, numbers)


if __name__ == "__main__":
    print(main())
