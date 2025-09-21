#include <stdio.h>


int maxPathSum(int **grid, int m, int n);

int failures = 0;

void check(int grid[][4], int m, int n, int expected) {
    int *ptrs[m];
    for (int i=0; i<m; i++) ptrs[i]=grid[i];
    int output = maxPathSum(ptrs,m,n);
    if (output==expected) {
        printf("PASS\n");
    } else {
        printf("FAIL Expected=%d Got=%d\n", expected, output);
        failures++;
    }
}

int main() {
    int g1[3][4]={{1,2,3,4},{2,2,1,1},{5,1,1,1}};
    check(g1,3,4,11);

    int g2[2][2]={{-1,2},{1,3}};
    check(g2,2,2,4);

    int g3[4][4]={{1,1,1,1},{1,1,1,1},{1,1,1,1},{1,1,1,9}};
    check(g3,4,4,15);

    if (failures>0) return 1;
    return 0;
}
