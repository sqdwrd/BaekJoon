# https://acmicpc.net/problem/1966
'''
문서의 개수와 우선순위가 기록된 큐가 주어짐.
입력 큐 순서에서 M번째 문서는 몇 번째로 출력되는가?

우선순위가 가장 높은 문서를 찾으면서...
    1) 중요도가 낮은 문서는 맨 뒤로 pop(); push;
    2) 맨 앞의 문서의 중요도가 가장 높다면 pop();

큐에 원래 위치대로 인덱스를 기록하자. 2) 를 시행하면 카운터 증가. 타겟 인덱스에 대해 2)를 수행한다면 print(카운터);
'''



def main(len_data: int):
    if len_data == 0:
        return 0

    target = int(input().split()[1])
    queue = [[i, int(v)] for i, v in enumerate(input().split())]

    print(process_doc(queue, target))

    main(len_data - 1)


def process_doc(queue: list[list[int]], target_index, iteration_counter: int = 0) -> int:
    max_importance = find_max_importance(queue)

    if (queue[0][1] >= max_importance):
        processed = queue.pop(0)
        iteration_counter = iteration_counter + 1

        if (processed[0] == target_index):
            return iteration_counter
    else:
        queue.append(queue.pop(0))

    return process_doc(queue, target_index, iteration_counter)


def find_max_importance(queue: list[list[int]], importance_candidate: int = 0):
    importance_candidate = max(importance_candidate, queue[0][1])

    if len(queue) == 1:
        return importance_candidate

    return find_max_importance(queue[1:], importance_candidate)


if __name__ == "__main__":
    main(int(input()))
