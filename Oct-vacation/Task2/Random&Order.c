#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define Length 10

void bubbleSort(int arr[], int n) 
{
    for (int i = 0; i < n - 1; i++) 
    {
        for (int j = 0; j < n - 1 - i; j++) 
        {
            if (arr[j] > arr[j + 1]) 
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int arr[Length];
    srand(time(NULL));

    for (int i = 0; i < Length; i++) 
    {
        arr[i] = rand();
    }

    printf("ԭʼ������飺");
    for (int i = 0; i < Length; i++) 
    {
        printf("%d ", arr[i]);
    }
    printf("\n---------------------------------------------------------\n");

    // ����ð������
    bubbleSort(arr, Length);

    printf("���������飺");
    for (int i = 0; i < Length; i++) 
    {
        printf("%d ", arr[i]);
    }
    printf("\n---------------------------------------------------------\n");
    
    system("pause");
    return 0;
}