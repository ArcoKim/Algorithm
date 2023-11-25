#include <stdio.h>

int a,c;

int recursive(int n) {
    if(n == 1) {
        return a;
    }
    long long half = recursive(n/2);
    if(n % 2 == 0) {
        return half * half % c;
    }
    return half * half % c * a % c;
}

int main() {
    int b;
    scanf("%d %d %d", &a, &b, &c);
    a %= c;
    printf("%d\n", recursive(b));
    return 0;
}