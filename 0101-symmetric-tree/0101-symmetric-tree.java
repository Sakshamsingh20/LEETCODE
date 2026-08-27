class Solution {

    public boolean isSymmetric(TreeNode root) {

        if (root == null) {
            return true;
        }

        return isMirror(root.left, root.right);
    }

    public boolean isMirror(TreeNode left, TreeNode right) {

        // Both positions are empty
        if (left == null && right == null) {
            return true;
        }

        // Only one position is empty
        if (left == null || right == null) {
            return false;
        }

        // Corresponding values must be equal
        if (left.val != right.val) {
            return false;
        }

        return isMirror(left.left, right.right)
                && isMirror(left.right, right.left);
    }
}