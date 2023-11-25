#include <stdio.h>
#include <limits.h>

int main()
{
    int t, n, min, result;
    int prime[10001] = {0,};
    int max_size = 10000;

    scanf("%d", &t);

    for(int i=2; i<=max_size; i++) {
        if(!prime[i]) {
            for(int j=i+i; j<=max_size; j+=i) {
                prime[j] = 1;
            }
        }
    }
    for(int i=0; i<t; i++) {
        scanf("%d", &n);
        min = INT_MAX;
        result = 0;
        for(int j=2; j<=n/2; j++) {
            if(!prime[j] && !prime[n-j] && n-j*2 < min) {
                min = n-j*2;
                result = j;
            }
        }
        printf("%d %d\n", result, n - result);
    }

    return 0;
}
