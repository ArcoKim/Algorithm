#include <stdio.h>
#include <limits.h>

int prime[1000001] = {0,};

int main()
{
    int n, result;
    int max_size = 1000000;

    for(int i=2; i<=max_size; i++) {
        if(!prime[i]) {
            for(int j=i+i; j<=max_size; j+=i) {
                prime[j] = 1;
            }
        }
    }

    while(1) {
        scanf("%d", &n);
        if(!n) break;
        for(int j=3; j<=n/2; j++) {
            if(!prime[j] && !prime[n-j]) {
                result = j;
                break;
            }
        }
        printf("%d = %d + %d\n", n, result, n - result);
    }

    return 0;
}
