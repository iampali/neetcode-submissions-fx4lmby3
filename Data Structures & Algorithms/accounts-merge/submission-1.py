from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict, deque

class Solution:
    def accountsMerge(self, accounts):
        graph = defaultdict(list)
        email_to_name = {}

        # Build graph
        for account in accounts:
            name = account[0]
            first_email = account[1]
            
            for email in account[1:]:
                email_to_name[email] = name
                graph[first_email].append(email)
                graph[email].append(first_email)

        visited = set()
        output = []

        def bfs(start):
            queue = deque([start])
            component = []
            visited.add(start)

            while queue:
                email = queue.popleft()
                component.append(email)

                for neighbor in graph[email]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            return component

        # Traverse graph
        for email in graph:
            if email not in visited:
                merged = bfs(email)
                merged.sort()
                merged.insert(0, email_to_name[email])
                output.append(merged)

        return output








