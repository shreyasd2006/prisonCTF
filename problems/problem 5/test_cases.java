public class test_cases {
    private static int failures=0;

    private static void check(String input, String expected) {
        String output = solution.encrypt(input);
        if (output.equals(expected)) {
            System.out.println("PASS");
        } else {
            System.out.println("FAIL Input=" + input + " Expected=" + expected + " Got=" + output);
            failures++;
        }
    }

    public static void main(String[] args) {
        check("hello123","igopt321");
        check("programming2025!","qsphsbnnjoh5202!");
        check("AeiOu","DhpRx");
        check("testCASE123","uftuDBTF321");

        if (failures>0) System.exit(1);
        else System.exit(0);
    }
}
