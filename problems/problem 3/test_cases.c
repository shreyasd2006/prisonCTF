#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* twoSumPairs(int *arr, int n, int target);

int failures = 0;

void normalize(char *s) {

    char *lines[1000];
    int count=0;
    char *tok = strtok(s, "\n");
    while (tok) {
        lines[count++] = tok;
        tok = strtok(NULL, "\n");
    }
    for (int i=0; i<count; i++) {
        for (int j=i+1; j<count; j++) {
            if (strcmp(lines[i], lines[j])>0) {
                char *tmp = lines[i];
                lines[i] = lines[j];
                lines[j] = tmp;
            }
        }
    }
    s[0]='\0';
    for (int i=0; i<count; i++) {
        strcat(s, lines[i]);
        strcat(s, "\n");
    }
}

void check(int arr[], int n, int target, char *expected) {
    char *output = twoSumPairs(arr,n,target);
    normalize(output);
    normalize(expected);
    if (strcmp(output, expected)==0) {
        printf("PASS\n");
    } else {
        printf("FAIL Expected=\n%sGot=\n%s", expected, output);
        failures++;
    }
    free(output);
}

int main() {
    int arr1[] = {1,2,3,2,4};
    check(arr1, 5, 4, strdup("0 2\n1 3\n"));

    int arr2[] = {3,3,4,7,5,2};
    check(arr2, 6, 10, strdup("1 3\n2 4\n"));

    int arr3[] = {0,0,0,0};
    check(arr3, 4, 0, strdup("0 1\n0 2\n0 3\n1 2\n1 3\n2 3\n"));

    int arr4[] = {-1,-2,-3,-4,-5};
    check(arr4, 5, -8, strdup("2 4\n"));

    if (failures>0) return 1;
    return 0;
}
