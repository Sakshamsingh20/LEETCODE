from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        
        if not edges:
            return -1
            
        # Step 1: Build the graph and calculate in-degrees
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        max_cost = -1
        
        for u, v, cost in edges:
            adj[u].append((v, cost))
            in_degree[v] += 1
            if cost > max_cost:
                max_cost = cost
                
        # Step 2: Precompute Topological Sort (Kahn's Algorithm)
        # We only need to do this once since the graph structure never changes.
        q = deque([i for i in range(n) if in_degree[i] == 0])
        topo_order = []
        
        while q:
            u = q.popleft()
            topo_order.append(u)
            for v, cost in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
                    
        # Step 3: Helper function to check if a specific min_cost is viable
        def check(min_allowed_cost: int) -> bool:
            # dist[i] stores the minimum total cost to reach node i
            dist = [float('inf')] * n
            dist[0] = 0
            
            for u in topo_order:
                # If a node is unreachable, or if it's offline, we skip it.
                # Nodes 0 and n-1 are guaranteed to be online per the problem.
                if dist[u] == float('inf') or not online[u]:
                    continue
                    
                for v, cost in adj[u]:
                    # Only traverse edges that meet the required threshold
                    if cost >= min_allowed_cost:
                        if dist[u] + cost < dist[v]:
                            dist[v] = dist[u] + cost
                            
            # Check if we reached the target node within the allowed budget 'k'
            return dist[n - 1] <= k

        # Step 4: Binary Search for the maximum minimum-edge cost
        ans = -1
        low = 0
        high = max_cost
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid        # This cost is viable, record it
                low = mid + 1    # Try to find a higher score
            else:
                high = mid - 1   # This cost is too restrictive
                
        return ans