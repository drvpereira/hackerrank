#include <stdio.h>
#include <stdlib.h>

int main(){
    int n; 
    scanf("%d",&n);
    
    int element, sum = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            scanf("%d", &element);
            if (j == i && j != (n - i - 1)) {                
                sum += element;
            } else if (j != i && j == (n - i - 1)) {
                sum -= element;
            }
        }
    }
    
    printf("%d\n", abs(sum));
    return 0;
}
