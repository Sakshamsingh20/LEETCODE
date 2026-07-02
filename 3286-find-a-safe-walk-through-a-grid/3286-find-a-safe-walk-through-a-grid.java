import java.util.*;

class Solution {
    public boolean findSafeWalk(List<List<Integer>> grid, int health) {

        int m = grid.size();
        int n = grid.get(0).size();

        // Health after entering the starting cell
        int startHealth = health - grid.get(0).get(0);

        if (startHealth <= 0) {
            return false;
        }

        Queue<int[]> queue = new LinkedList<>();

        // {row, col, remainingHealth}
        queue.offer(new int[]{0, 0, startHealth});

        // best[r][c] = maximum health with which we've reached (r,c)
        int[][] best = new int[m][n];

        for (int i = 0; i < m; i++) {
            Arrays.fill(best[i], -1);
        }

        best[0][0] = startHealth;

        int[] dr = {1, -1, 0, 0};
        int[] dc = {0, 0, 1, -1};

        while (!queue.isEmpty()) {

            int[] cur = queue.poll();

            int row = cur[0];
            int col = cur[1];
            int currHealth = cur[2];

            if (row == m - 1 && col == n - 1) {
                return true;
            }

            for (int i = 0; i < 4; i++) {

                int newRow = row + dr[i];
                int newCol = col + dc[i];

                if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n) {

                    int newHealth = currHealth - grid.get(newRow).get(newCol);

                    if (newHealth > 0 && newHealth > best[newRow][newCol]) {

                        best[newRow][newCol] = newHealth;

                        queue.offer(new int[]{newRow, newCol, newHealth});
                    }
                }
            }
        }

        return false;
    }
}