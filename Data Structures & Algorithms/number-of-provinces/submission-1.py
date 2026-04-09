class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0

        for i in range(len(isConnected)):
            if i not in visited:
                count += 1
                queue = [i]
                while queue:
                    curr = queue.pop(0)
                    for neighbor in range(len(isConnected[curr])):
                        if neighbor not in visited and isConnected[curr][neighbor]:
                            visited.add(neighbor)
                            queue.append(neighbor)

        print(visited)
        
        return count

