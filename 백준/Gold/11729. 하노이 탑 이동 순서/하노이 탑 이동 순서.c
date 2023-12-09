#include <stdio.h>

int result,k;
int prog[10000000][2];

void push(int now, int next) {
    prog[result][0] = now;
    prog[result][1] = next;
    result++;
}

void move(int n, int now, int next) {
    if(n == 1) {
        push(now, next);
    } else {
        int p_next = 6 - now - next;
        move(n-1, now, p_next);
        push(now, next);
        move(n-1, p_next, next);
    }
}

int main() {
    scanf("%d", &k);
    
    move(k, 1, 3);
    
    printf("%d\n", result);
    for(int i=0; i<result; i++) {
        printf("%d %d\n", prog[i][0], prog[i][1]);
    }
    
    return 0;
}