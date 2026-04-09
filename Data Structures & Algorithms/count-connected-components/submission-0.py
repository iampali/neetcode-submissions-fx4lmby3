from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_list = defaultdict(list)

        for i in edges:
            adjacency_list[i[0]].append(i[1])
            adjacency_list[i[1]].append(i[0])

        print(adjacency_list)
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                queue = [i]
                count += 1
                while queue:
                    node = queue.pop(0)
                    for j in adjacency_list[node]:
                        if j not in visited:
                            visited.add(j)
                            queue.append(j)

        return count