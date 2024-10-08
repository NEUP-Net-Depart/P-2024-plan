#include <stdio.h>

int *arr, start, end, left, right, mid;
void quickSort(int *arr,int start, int end)
{
    int left = end;
    int right = start;
    int mid = arr[left];

    while (left < right)
    {
        while((arr[right] > mid) && (right > left))
        {
            right--;
        }
        if (left < right)
        {
            arr[left] = arr[right];
            left++;
        }

        while((arr[left] < mid) && (left < right))
        {
            left++;
        }
        if(left < right)
        {
            arr[right] = arr[left];
            right--;
        }
    }
    mid = arr[right] ;
    quickSort(arr, start, left - 1);
    quickSort(arr, right + 1, end);
}

void printArray(int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main()
{
    int arr[5] = {3, 1, 2, 5, 4};
    int n = sizeof(arr) / sizeof(arr[0]);
    quickSort(arr, 0, n - 1);
    printArray(arr, n);
    return 0;
}
