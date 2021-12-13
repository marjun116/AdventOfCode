def dfs(start, end, path, caves):
    path.append(start)
    if start == end:
        return [path]
    if start not in caves or end not in caves:
        return []
    paths = []
    for node in caves[start]:
        if not(node in path and node.islower()):
            paths.extend(dfs(node, end, path.copy(), caves))
    return paths


caves = {}
with open("../inputs/day12.txt") as fh:
    line = fh.readline()
    while line != '':
        v = line.strip().split('-')
        if v[0] not in caves:
            caves[v[0]] = [v[1]]
        else:
            caves[v[0]].append(v[1])
        if v[1] not in caves:
            caves[v[1]] = [v[0]]
        else:
            caves[v[1]].append(v[0])
        line = fh.readline()


result = dfs('start', 'end', [], caves)
print(len(result))
