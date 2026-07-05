class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))
        visited = [False] * (n + 1)
        visited[1] = True
        queue = deque([1])
        min_score = float('inf')

        while queue:
            node = queue.popleft()
            for neighbor, dist in graph[node]:
                min_score = min(min_score, dist)
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return min_score
            

            
                