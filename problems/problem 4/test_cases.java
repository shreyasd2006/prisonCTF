public class test_cases {
    private static int failures = 0;

    private static void check(int[][] grid, int expected) {
        int output = solution.maxPathSum(grid);
        if (output==expected) {
            System.out.println("PASS");
        } else {
            System.out.println("FAIL Expected=" + expected + " Got=" + output);
            failures++;
        }
    }

    public static void main(String[] args) {
        check(new int[][]{{1,2,3,4},{2,2,1,1},{5,1,1,1}},11);
        check(new int[][]{{-1,2},{1,3}},4);
        check(new int[][]{{1,1,1,1},{1,1,1,1},{1,1,1,1},{1,1,1,9}},15);

        if (failures>0) System.exit(1);
        else System.exit(0);
    }
}
