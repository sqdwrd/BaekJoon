class Graph:
    def __init__(self):
        self.graph: list[list[Node]] = []
        nmv = input().split(" ")
        n = int(nmv[0])
        m = int(nmv[1])
        self.v = int(nmv[2])

        for i in range(n):
            self.graph.append([])

        for i in range(m):
            vertex = input()
            self.graph[int(vertex.split(" ")[0])].append(Node(int(vertex.split(" ")[1])))
            self.graph[int(vertex.split(" ")[1])].append(Node(int(vertex.split(" ")[0])))

    def dfs(self):
        queue = [self.v]

        while True:
            self.graph[queue[len(queue) - 1]]

    def get_min_child_not_visited(self, parent: int):
        min_child: Node = Node(1001)
        for i in range(len(self.graph[parent])):
            if not self.graph[parent][i].visited and min_child.num > self.graph[parent][i].num:
                min_child = self.graph[parent][i]
        return min_child




class Node:
    def __init__(self, num: int):
        self.num = num
        self.visited = False
