#include <stdio.h>
#include <string.h>
#include <stdlib.h>


char* firstNonRepeating(char *s);

int failures = 0;

void check(char *input, char *expected) {
    char *output = firstNonRepeating(input);
    if (strcmp(output, expected) == 0) {
        printf("PASS: %s\n", input);
    } else {
        printf("FAIL: %s Expected=%s Got=%s\n", input, expected, output);
        failures++;
    }
}

int main() {
    check("leetcode", "l");
    check("aabb", "None");
    check("abcabcde", "d");
    check("aabbccddeeff", "None");
    check("swiss", "w");

    if (failures > 0) return 1;
    return 0;
}
