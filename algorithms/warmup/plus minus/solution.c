#include <stdio.h>

int main(){
    int n, element, total, positives = 0, negatives = 0, zeroes = 0; 
    scanf("%d",&n);
    
    for(int i = 0; i < n; i++) {
        scanf("%d", &element);
        if (element > 0) positives++;
        else if (element < 0) negatives++;
        else zeroes++;        
    }
    
    total = positives + negatives + zeroes;
    
    printf("%.6f\n", (1.0 * positives) / total);
    printf("%.6f\n", (1.0 * negatives) / total);
    printf("%.6f\n", (1.0 * zeroes) / total);
    
    return 0;
}
