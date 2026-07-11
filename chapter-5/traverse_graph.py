graph = {
    "u": ["v", "x", "w"],
    "x": ["y", "w", "v", "u"],
    "v": ["w", "u", "x"],
    "w": ["x", "v", "u", "z", "y"],
    "y": ["x", "w", "z"],
    "z": ["w", "y"],
}


def traverse_graph(start, end):
    result = []
    backtrack(start, end, {start}, [start], result)
    return "\n".join(list(map(lambda arr: " -> ".join(arr), result)))


def backtrack(start, end, seen, path, result):
    for nei in graph[start]:
        if nei in seen:
            continue

        if nei == end:
            result.append([*path, end])
            continue

        path.append(nei)
        seen.add(nei)
        backtrack(nei, end, seen, path, result)
        seen.remove(nei)
        path.pop()


print(traverse_graph("y", "u"))
