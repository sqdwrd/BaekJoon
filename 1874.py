import sys
input = sys.stdin.readline


def main():
    n = int(input())

    sample_queue = [i for i in range(1, n + 1)]
    stack = []
    current = 0
    cmd_queue = []

    for _ in range(n):
        target = int(input())
        while current < target:
            current = push(sample_queue, stack)
            cmd_queue.append("+")
        if (pop(stack) != target):
            print("NO")
            return 0

        cmd_queue.append("-")

    for i in cmd_queue:
        print(i)


def push(from_queue: list[int], to_stack: list[int]) -> int:
    current = from_queue.pop(0)
    to_stack.append(current)
    return current


def pop(stack: list[int]) -> int:
    return stack.pop()


if __name__ == "__main__":
    main()
