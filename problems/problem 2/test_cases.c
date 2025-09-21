#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* longestCommonPrefix(char **strs, int n);

int failures = 0;

void check(char *arr[], int n, char *expected) {
    char *output = longestCommonPrefix(arr, n);
    if (strcmp(output, expected) == 0) {
        printf("PASS\n");
    } else {
        printf("FAIL Expected=%s Got=%s\n", expected, output);
        failures++;
    }
}

int main() {
    char *arr1[] = {"flower","flow","flight"};
    check(arr1, 3, "fl");

    char *arr2[] = {"interspecies","interstellar","interstate","internet"};
    check(arr2, 4, "inter");

    char *arr3[] = {"dog","racecar","car"};
    check(arr3, 3, "");

    char *arr4[] = {"abcd","abc"};
    check(arr4, 2, "abc");

    if (failures > 0) return 1;
    return 0;
}
