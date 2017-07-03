#include <stdio.h>

int main() {
    int n, value, result = 0;
    
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        scanf("%d",&value);
        result += value;
    }
    
    printf("%d\n", result);
    return 0;
}
