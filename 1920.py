from typing import Optional


def main():
    input()

    samples = [int(x) for x in input().split()]
    samples.sort()

    input()

    # [[index, target], [index, target], ...]
    targets = [[i, int(x)] for i, x in enumerate(input().split())]
    targets.sort(key=(lambda x: x[1]))

    answer = find_all(samples, targets)

    for a in answer:
        assert a is not None
        print(a)


def find_all(samples: list[int], targets: list[list[int]]):
    answer: list[Optional[int]] = [None for _ in targets]

    for t in targets:
        while True:
            if (len(samples) == 0):
                answer[t[0]] = 0
                break

            if (samples[0]) == t[1]:
                answer[t[0]] = 1
                break
            elif samples[0] < t[1]:
                samples.pop(0)
            else:  # samples[0] > t
                answer[t[0]] = 0
                break
    return answer


if __name__ == "__main__":
    main()
