#include<stdio.h>
int main() {
   
    char key[] = "NewStar2024";

    char enc[] = {40,9,22,52,15,56,66,71,111,121,90,33,18,40,3,13,80,28,65,68,83,88,34,86,5,12,35,82,67,3,17,79 };
    for (int i = 0; i < 32; i++) {
        enc[i] ^= key[i % 11];
        printf("%c", enc[i]);
    }
}
