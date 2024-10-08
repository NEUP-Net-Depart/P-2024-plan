#include <stdio.h>
#include <stdlib.h>
void bubblesolt(int arr[], int length)
{
   int x, y, temp;
   for (x = 0; x < length - 1; x++)
      for (y = 0; y < length - x - 1; y++)
         if (arr[y] > arr[y + 1])
         {
            temp = arr[y];
            arr[y] = arr[y + 1];
            arr[y + 1] = temp;
         }
}
int main()
{
   int arr[5] = {5, 1, 4, 2, 8};
   int length = sizeof(arr) / sizeof(arr[0]);
   bubblesolt(arr, length);
   int x;
   for (x = 0; x < length; x++)
      printf("%d", arr[x]);
   return 0;
}