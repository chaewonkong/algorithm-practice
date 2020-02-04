"""
BFS and DFS

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

[입력]
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 
탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

[출력]
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
"""
# from collections import deque


# def dfs(matrix, n, v):
#     visited = []

#     def search(v):
#         if v not in visited:
#             visited.append(v)

#         for i in range(1, n):
#             if matrix[v][i] == 1 and i not in visited:
#                 visited.append(i)
#                 search(i)
#         return

#     search(v)
#     return " ".join(map(str, visited))


# def bfs(matrix, n, v):
#     visited = [v]
#     dq = deque([v])

#     while dq:
#         v = dq.popleft()
#         for i in range(1, n):
#             if matrix[v][i] == 1 and i not in visited:
#                 visited.append(i)
#                 dq.append(i)

#     return " ".join(map(str, visited))


# if __name__ == "__main__":
#     N, M, V = map(int, input().split())
#     matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
#     for _ in range(M):
#         i, j = map(int, input().split())
#         matrix[i][j] = matrix[j][i] = 1

#     print(dfs(matrix, N+1, V))
#     print(bfs(matrix, N+1, V))


# Practice 2
from collections import deque


def dfs(matrix, start):
    visited = [start]
    n = len(matrix)

    def search(v):
        if v not in visited:
            visited.append(v)
        for i in range(n):
            if matrix[v][i] == 1 and i not in visited:
                visited.append(i)
                search(i)
        return

    search(start)
    return " ".join(map(str, visited))


def bfs(matrix, start):
    queue = deque([start])
    n = len(matrix)
    visited = [start]

    while queue:
        v = queue.popleft()

        for i in range(n):
            if matrix[i][v] == 1 and i not in visited:
                visited.append(i)
                queue.append(i)

    return " ".join(map(str, visited))


if __name__ == "__main__":
    [N, M, V] = map(int, input().split())
    matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        i, j = map(int, input().split())
        matrix[i][j] = matrix[j][i] = 1
    print(dfs(matrix, V))
