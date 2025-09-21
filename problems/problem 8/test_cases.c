#include <stdio.h>


long long fib(int n);

int failures=0;

void check(int n, long long expected) {
    long long output=fib(n);
    if (output==expected) {
        printf("PASS: n=%d\n", n);
    } else {
        printf("FAIL: n=%d Expected=%lld Got=%lld\n", n, expected, output);
        failures++;
    }
}

int main() {
    check(10,55);
    check(20,6765);
    check(45,1134903170LL);

    if (failures>0) return 1;
    return 0;
}
