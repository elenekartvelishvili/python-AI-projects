
def dfs(graph, start):
    stack = [start]
    visited_order = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited_order:
            visited_order.append(vertex)
            print(vertex, visited_order)

            for neighbour in reversed(graph[vertex]):
                if neighbour not in stack or neighbour not in visited_order:
                    stack.append(neighbour)

    return visited_order


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs_result = dfs(graph, 'A')
print(dfs_result)
