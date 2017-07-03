#include <stdio.h>

int main() {
    int n, element, max = 0, count;
    scanf("%d", &n);
    
    for(int i = 0; i < n; i++){
        scanf("%d", &element);
        if (element > max) {
            max = element;
            count = 1;
        } else if (element == max) count++;
    }
    printf("%d\n", count);
    return 0;
}
