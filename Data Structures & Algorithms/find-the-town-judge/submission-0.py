class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adjancency_list = {}
        indegree = [0] * n
        for i, j in trust:
            adjancency_list[i] = j
            indegree[j-1] += 1
        print(adjancency_list)
        print(indegree)

        count_0 = 0
        count_judge = 0
        index_judge = -1 

        for index, i in enumerate(indegree):
            if i == 0:
                count_0 += 1
            else:
                count_judge += 1
                index_judge = index 
        
        if count_0 == n - 1 and count_judge == 1:
            return index_judge + 1
        else:
            return -1
            
        
