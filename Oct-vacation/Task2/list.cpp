#include <iostream>
#include <stdlib.h>

void Swap(int *a, int *b) { //交换函数, 辅助Divide函数
    int temp = *a;
    *a = *b;
    *b = temp;
}

int Divide(int array[], int min, int max) {        //使用快速排序, 这部分为分离的操作
    int key = array[min];
    while (min < max) {
        while (min < max && array[max] >= key)      //将所有大于key的数放在key后
            max--;
        Swap(&array[min], &array[max]);
        while (min < max && array[min] <= key)      //将所有小于key的数放在key前
            min++;
        Swap(&array[min], &array[max]);
    }
    return min;
}

void List(int array[], int min, int max) {
    if (min < max) {
        int lastMin = Divide(array, min, max);      //找到分界点
        List(array, min, lastMin - 1);              //递归分界点前部分进行排序
        List(array, lastMin + 1, max);              //递归分界点后部分进行排序
    }
}
int main()                                          //随机生成100个从0到100的整数,并将其排序
{
    srand(time(NULL));
    int array[100];
    for (int i = 0; i < 100; i++) {
        array[i] = rand()%100;
        printf("%d ", array[i]);
    }
    List(array, 0, 99);
    printf("\n排序后的结果为: \n");
    for (int i = 0; i < 100; i++) {
        printf("%d ", array[i]);
    }
}