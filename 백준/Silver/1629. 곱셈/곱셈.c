#include <stdio.h>

int a,c;

long long cal(int b) {
    if(b == 1) return a % c;
    long long half = cal(b/2);
    long long result = half * half % c;
    if(b % 2 == 1) return result * a % c;
    return result;
}

int main() {
    int b;
    scanf("%d %d %d", &a, &b, &c);
    printf("%lld\n", cal(b));
    return 0;
}