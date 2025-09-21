#include <stdio.h>
#include <string.h>
#include <stdlib.h>


char* encrypt(char *s);

int failures=0;

void check(char *input, char *expected) {
    char *output = encrypt(input);
    if (strcmp(output, expected)==0) {
        printf("PASS\n");
    } else {
        printf("FAIL Input=%s Expected=%s Got=%s\n", input, expected, output);
        failures++;
    }
    free(output);
}

int main() {
    check("hello123","igopt321");
    check("programming2025!","qsphsbnnjoh5202!");
    check("AeiOu","DhpRx");
    check("testCASE123","uftuDBTF321");

    if (failures>0) return 1;
    return 0;
}
