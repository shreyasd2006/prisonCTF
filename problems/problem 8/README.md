Description:
Fix the performance issue in this C program. For large n, it takes too long. Implement memoization or DP.

int fib(int n) {
if (n == 0) return 0;
if (n == 1) return 1;
return fib(n-1) + fib(n-2);

}

int main() {
int n = 50;
printf("%d",fib(n));
return 0;
}

