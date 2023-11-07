import sys
input = sys.stdin.readline


def main():
    k = int(input())
    queue = []
    for _ in range(k):
        cmd = int(input())

        if cmd == 0:
            queue.pop()
        else:
            queue.append(cmd)

    answer = 0
    for i in queue:
        answer = answer + i

    return answer


if __name__ == "__main__":
    print(main())
