from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        graph = defaultdict(list)

        def check_similar(a, b):
            count = 0
            for i, j in zip(a, b):
                if i != j:
                    count += 1
            return count == 1

        n = len(wordList)
        for i in range(n):
            for j in range(i+1, n):
                if check_similar(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])

        print(graph)

    
        queue = deque()
        queue.append((beginWord, 0))
        visited = set()
        visited.add(beginWord)


        while queue:
            curr, level = queue.popleft()
            if curr == endWord:
                return level + 1
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    queue.append((neighbor, level + 1))
                    visited.add(neighbor)
        
        return 0
        

