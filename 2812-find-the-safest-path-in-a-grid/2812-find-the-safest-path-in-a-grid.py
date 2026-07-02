from collections import deque
import heapq

class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        
        # If the start or end is a thief, safeness is 0
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
            
        # Step 1: Multi-source BFS to calculate distance to nearest thief for every cell
        dist = [[float('inf')] * n for _ in range(n)]
        q = deque()
        
        # Add all thieves to the queue
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))
                    
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # If within bounds and not yet visited
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
                    
        # Step 2: Use a Max-Heap to find the path with the maximum minimum safeness
        # Heap stores: (-safeness_factor, r, c) to simulate a max-heap in Python
        max_heap = [(-dist[0][0], 0, 0)]
        visited = set([(0, 0)])
        
        while max_heap:
            safe, r, c = heapq.heappop(max_heap)
            safe = -safe # Invert back to positive
            
            # Reached the destination
            if r == n - 1 and c == n - 1:
                return safe
                
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    # The safeness of a path is the minimum safeness of its cells
                    min_safe = min(safe, dist[nr][nc])
                    heapq.heappush(max_heap, (-min_safe, nr, nc))
                    
        return 0