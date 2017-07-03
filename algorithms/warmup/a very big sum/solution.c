#include <stdio.h>

int main() {
    char n;
    unsigned long result = 0, value;
    
    scanf("%hhi", &n);
    for(int i = 0; i < n; i++){
        scanf("%lu",&value);
        result += value;
    }
    
    printf("%lu\n", result);
    return 0;
}
