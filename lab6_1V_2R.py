from collections import defaultdict

def topological_sort(dependencies):
    graph = defaultdict(list)
    all_docs = set()

    for u, v in dependencies:
        graph[v].append(u)
        all_docs.update([u, v])

    for v in graph:
        graph[v].sort()

    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for nxt in graph[node]:
            if nxt not in visited:
                dfs(nxt)
        stack.append(node)

    for doc in sorted(all_docs):
        if doc not in visited:
            dfs(doc)

    return stack[::-1]
