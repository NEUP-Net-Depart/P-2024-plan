#include <stdio.h>

int l[] = {99, 51, 44, 66, 37, 66, 42, 70, 53, 24};
int length = sizeof(l) / sizeof(l[0]);
// 算长度

int main()
{
    int sl[length];
    for (int i = 0; i < length; i++)
    {
        sl[i] = l[i];
    }
    for (int i = 0; i < length - 1; i++)
    {
        // int temp = sl[i];
        int j = i;
        while (sl[j] >= sl[j + 1] && j >= 0)
        {
            // 小于就互换
            int temp = sl[j];
            sl[j] = sl[j + 1];
            sl[j + 1] = temp;
            j--;
        }
    }
    for (int s = 0; s < length; s++)
    {
        printf("%d,", sl[s]);
    }
}