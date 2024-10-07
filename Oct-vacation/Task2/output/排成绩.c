#include <stdio.h>
#include <stdlib.h>

void print(int a[], int n, int i) {
    printf("结果为： ", i + 1);
    for (int j = 0; j < n; j++) {
        printf("%d  ", a[j]);
    }
    printf("\n");
}

void selectSort(int a[],int len) {
        int i,j,min,max,tmp;  
        for(i=0; i<len/2; i++){  // 做不超过n/2趟选择排序 
            min = max = i;  
            for(j=i+1; j<=len-1-i; j++){  
				//分别记录最大和最小关键字记录位置
                if(a[j] > a[max]){  
                    max = j;  
                    continue;  
                }  
                if(a[j] < a[min]){  
                    min = j;  
                }  
            }  
			//该交换操作还可分情况讨论以提高效率
            if(min != i){//当第一个为min值，不用交换  
                tmp=a[min];  a[min]=a[i];  a[i]=tmp;  
            }  
            if(max == len-1-i && min == i)//当第一个为max值，同时最后一个为min值，不再需要下面操作  
                continue;  
            if(max == i)//当第一个为max值，则交换后min的位置为max值  
                max = min;  
            if(max != len-1-i){//当最后一个为max值，不用交换  
                tmp=a[max];  a[max]=a[len-1-i];  a[len-1-i]=tmp;  
            }		
        }  
 }

int main() 
{
    int size;
    printf("班级人数为?\n");
    scanf("%d",&size);
    int *grade = (int *)malloc(size * sizeof(int)); // 动态数组内存分配

    if (grade == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    for (int i = 0; i < size; i++) {
        printf("第%d位同学的分数是?\n",i+1);
        scanf("%d", &grade[i]);
    }

    printf("请确认数据：");
    for (int i = 0; i < size; i++) {
        printf("%d ", grade[i]);
    }
    printf("\n\n");
    selectSort(grade, size);
    print(grade, size, size);
    return 0;
}