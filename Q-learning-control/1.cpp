#include <stdio.h>
int main(){
    int i;
    long long j;
    for(i = 1, j = 1;i <= 20; j *= i++);
        printf("%lld", j); 
    return 0;   
}