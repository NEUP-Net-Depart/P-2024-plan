# Task 2

请补充个人信息后，在此完成报告！

```@Author:  24网络部林荣强
@Email:  3500954350@qq.com
实现冒泡排序
#include<stdio.h>
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // 交换元素
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
//用冒泡排序将身高进行排序
int main(){
    int height[]={180,175,169,181,176,169,185};
    int len=sizeof(height)/sizeof(height[0]);
    printf("height:\n");
    for(int i=0;i<len;i++){
        printf("%d ",height[i]);
    }
    bubbleSort(height,len);
        printf("\nsorted height\n");
    for(int i=0;i<len;i++){
        printf("%d ",height[i]);
    }
}
```