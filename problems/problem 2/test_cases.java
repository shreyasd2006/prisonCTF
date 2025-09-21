public class test_cases {
    private static int failures = 0;

    private static void check(String[] arr, String expected) {
        String output = solution.longestCommonPrefix(arr);
        if (output.equals(expected)) {
            System.out.println("PASS");
        } else {
            System.out.println("FAIL Expected=" + expected + " Got=" + output);
            failures++;
        }
    }

    public static void main(String[] args) {
        check(new String[]{"flower","flow","flight"}, "fl");
        check(new String[]{"interspecies","interstellar","interstate","internet"}, "inter");
        check(new String[]{"dog","racecar","car"}, "");
        check(new String[]{"abcd","abc"}, "abc");

        if (failures > 0) System.exit(1);
        else System.exit(0);
    }
}
