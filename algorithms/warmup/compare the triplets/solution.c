#include <stdio.h>

void solve(int a0, int a1, int a2, int b0, int b1, int b2){
    int a = (a0 > b0) + (a1 > b1) + (a2 > b2);
    int b = (a0 < b0) + (a1 < b1) + (a2 < b2);
    printf("%d %d\n", a, b);
}

int main() {
    int a0, a1, a2, b0, b1, b2; 
    scanf("%d %d %d", &a0, &a1, &a2);
    scanf("%d %d %d", &b0, &b1, &b2);
    
    solve(a0, a1, a2, b0, b1, b2);

    return 0;
}
