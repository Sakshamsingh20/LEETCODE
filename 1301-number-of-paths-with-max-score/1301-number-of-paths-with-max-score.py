
class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        MOD = 10**9 + 7
        n = len(board)
        
        # dp[r][c] will store [max_score, number_of_paths]
        # We use a padding of size n+1 to handle out-of-bounds gracefully.
        # Initialize with -1 score to represent unreachable cells.
        dp = [[[-1, 0] for _ in range(n + 1)] for _ in range(n + 1)]
        
        # Base case: Starting point at the bottom right
        dp[n - 1][n - 1] = [0, 1]
        
        # Traverse the board from bottom-right to top-left
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                # Skip the start cell (already initialized) and obstacles
                if board[r][c] == 'X' or (r == n - 1 and c == n - 1):
                    continue
                
                max_prev_score = -1
                total_ways = 0
                
                # Check the three possible cells we could have arrived from:
                # Bottom (Up move), Right (Left move), Bottom-Right (Diagonal move)
                for dr, dc in [(1, 0), (0, 1), (1, 1)]:
                    prev_score, prev_ways = dp[r + dr][c + dc]
                    
                    if prev_score != -1:
                        if prev_score > max_prev_score:
                            max_prev_score = prev_score
                            total_ways = prev_ways
                        elif prev_score == max_prev_score:
                            total_ways = (total_ways + prev_ways) % MOD
                
                # If the current cell is reachable from at least one valid previous cell
                if max_prev_score != -1:
                    # Treat 'E' as 0, otherwise add the numeric value of the cell
                    cell_value = 0 if board[r][c] == 'E' else int(board[r][c])
                    dp[r][c] = [max_prev_score + cell_value, total_ways]
                    
        ans_score, ans_ways = dp[0][0]
        
        # If the top-left cell is unreachable, return [0, 0]
        if ans_score == -1:
            return [0, 0]
            
        return [ans_score, ans_ways]