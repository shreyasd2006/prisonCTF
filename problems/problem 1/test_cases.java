public class test_cases {
    private static int failures = 0;

    private static void check(String input, String expected) {
        String output = solution.firstNonRepeating(input);
        if (output.equals(expected)) {
            System.out.println("PASS: " + input);
        } else {
            System.out.println("FAIL: " + input + " Expected=" + expected + " Got=" + output);
            failures++;
        }
    }

    public static void main(String[] args) {
        check("leetcode", "l");
        check("aabb", "None");
        check("abcabcde", "d");
        check("aabbccddeeff", "None");
        check("swiss", "w");

        if (failures > 0) System.exit(1);
        else System.exit(0);
    }
}
