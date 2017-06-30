#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, no_steps = 1; 
    scanf("%d",&n);
    
    char* step = (char*) malloc(sizeof(char) * n);
    
    while (no_steps <= n) {
        for (int i = 0; i < n - no_steps; i++) step[i] = ' ';
        for (int i = 0; i < no_steps; i++) step[n - no_steps + i] = '#';
        printf("%s\n", step);
        no_steps++;
    }
    
    free(step);
    return 0;
}
