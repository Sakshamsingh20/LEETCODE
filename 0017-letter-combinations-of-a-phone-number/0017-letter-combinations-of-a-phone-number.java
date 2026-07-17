import java.util.*;

class Solution {

    List<String> result = new ArrayList<>();

    String[] map = {
            "",      // 0
            "",      // 1
            "abc",   // 2
            "def",   // 3
            "ghi",   // 4
            "jkl",   // 5
            "mno",   // 6
            "pqrs",  // 7
            "tuv",   // 8
            "wxyz"   // 9
    };

    public List<String> letterCombinations(String digits) {

        if (digits == null || digits.length() == 0) {
            return result;
        }

        backtrack(digits, 0, new StringBuilder());

        return result;
    }

    private void backtrack(String digits, int index, StringBuilder current) {

        // Base case
        if (index == digits.length()) {
            result.add(current.toString());
            return;
        }

        // Get letters corresponding to current digit
        String letters = map[digits.charAt(index) - '0'];

        // Try every possible letter
        for (int i = 0; i < letters.length(); i++) {

            // Choose
            current.append(letters.charAt(i));

            // Explore
            backtrack(digits, index + 1, current);

            // Undo (Backtrack)
            current.deleteCharAt(current.length() - 1);
        }
    }
}