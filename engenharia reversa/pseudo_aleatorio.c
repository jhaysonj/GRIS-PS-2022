#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main () {
    int i = 0;
    int sVar1 = 0;
    char buffer[200];
    int seed = 0;
    

    for(unsigned w = 0; w < ~(unsigned)0; w++){

        
        snprintf(buffer, 200, "trusting_nobel%u%u", w, 37*w);

    

        seed = 0;
        i = 0;
        while(1){
            sVar1 = strlen(buffer);
            if ( (sVar1 >> 2) <= (ulong)(long)i) break;
            seed = seed + *(int *)(buffer + (long)i * 4);
            i = i + 1;
        }

        srand(seed);

        int sucesso = 0;
        for (int k = 0; k < 5; k++){
            if ( (rand() % 100) < 5 ){
                sucesso++;
            } 
        }

        if (sucesso >= 4){
            printf("%s\n", buffer);
            break;
        }
    }

    
    return(0);
}