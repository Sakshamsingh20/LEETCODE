class Solution(object):
    def zigZagArrays(self, n, l, r):
      
        MOD = 10**9 + 7
        k = r - l + 1
        
        # S2[i] represents the number of valid length 2 sequences ending 
        # in value (l+i) where the last step was strictly increasing (UP).
        # Since A1 < A2, for a given A2 = i (0-indexed), there are exactly 'i' valid choices for A1.
        S2 = [i for i in range(k)]
        
        # Build the transition matrix M of size k x k.
        # M[i][j] = 1 if we can transition from a previous state j to current state i.
        M = [[0] * k for _ in range(k)]
        for i in range(k):
            for j in range(k - i, k):
                M[i][j] = 1
                
        # Helper function to multiply two k x k matrices
        def multiply(A, B):
            res = [[0] * k for _ in range(k)]
            for i in range(k):
                for j in range(k):
                    if A[i][j]:  # Slight optimization to skip zero multiplication
                        for m in range(k):
                            res[i][m] = (res[i][m] + A[i][j] * B[j][m]) % MOD
            return res
        
        # Helper function for Matrix Exponentiation (A^p)
        def power(A, p):
            res = [[0] * k for _ in range(k)]
            for i in range(k):
                res[i][i] = 1  # Identity matrix
            
            base = A
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                p //= 2
            return res
            
        # We start with base case of length 2, so we need to multiply by M^(n-2)
        P = power(M, n - 2)
        
        # Calculate final state counts by multiplying matrix P with vector S2
        total_up = 0
        for i in range(k):
            val = 0
            for j in range(k):
                val = (val + P[i][j] * S2[j]) % MOD
            total_up = (total_up + val) % MOD
            
        # The total number of valid configurations is exactly double the 'UP' configurations
        # because the 'DOWN' configurations are perfectly symmetric.
        return (2 * total_up) % MOD
        