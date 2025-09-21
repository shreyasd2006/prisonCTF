import java.util.*;

public class test_cases {
    private static int failures = 0;

    // normalize string: sort lines so order doesn't matter
    private static String normalize(String s) {
        s = s.trim();
        if (s.isEmpty()) return "";
        String[] lines = s.split("\\r?\\n");
        Arrays.sort(lines);
        return String.join("\n", lines) + "\n";
    }

    private static void check(int[] arr, int target, String expected) {
         String[] pairs = solution.twoSumPairs(arr, target);
        String output = String.join("\n", pairs) + "\n"; // convert array to string
        String normOut = normalize(output);
        String normExp = normalize(expected);

        if (normOut.equals(normExp)) {
            System.out.println("PASS");
        }   
        else {
            System.out.println("FAIL\nExpected:\n" + normExp + "Got:\n" + normOut);
            failures++;
        }
}


    public static void main(String[] args) {
        check(new int[]{1,2,3,2,4}, 4, "0 2\n1 3\n");
        check(new int[]{3,3,4,7,5,2}, 10, "1 3\n2 4\n");
        check(new int[]{0,0,0,0}, 0, "0 1\n0 2\n0 3\n1 2\n1 3\n2 3\n");
        check(new int[]{-1,-2,-3,-4,-5}, -8, "2 4\n");

        if (failures > 0) {
            System.exit(1); // non-zero = failure
        } else {
            System.exit(0); // zero = success
        }
    }
}
