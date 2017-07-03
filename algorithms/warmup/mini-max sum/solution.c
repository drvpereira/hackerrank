#include <stdio.h>

#define ARRAY_SIZE 5
#define INFINITY 1000000001

int main() {
    unsigned int element, max = 0, min = INFINITY;
    unsigned long total = 0;
    
    for(int i = 0; i < ARRAY_SIZE; i++){
        scanf("%u", &element);
        total += element;
        if (element > max) max = element;
        if (element < min) min = element;
    }
    
    printf("%lu %lu\n", total - max, total - min);
    
    return 0;
}
