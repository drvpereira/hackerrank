#include <stdio.h>

int main() {
    int hour, minute, second;
    char half;
    scanf("%d:%d:%d%cM", &hour, &minute, &second, &half);
    
    if (hour != 12 && half == 'P' || hour == 12 && half == 'A') hour = (hour + 12) % 24;
    printf("%02d:%02d:%02d\n", hour, minute, second);
    
    return 0;
}
