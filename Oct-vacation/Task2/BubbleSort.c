#include<stdio.h>

int *sort(int *temp,int len);

int main(){
    int array[]={1,3,2,5,6,9,4,8,7,0};
    int length=sizeof(array) / sizeof(array[0]);//获取数组长度
    int *arr1=sort(array,length);
    for(int i=0;i<=(length-1);i++){
        printf("%d",arr1[i]);
    }
    return 0;
}

//排序函数
int *sort(int *temp,int len){
    int MAX=0;
    static int arr[10];
    int a=0;
    for(int i=0;i<=(len-1);i+=1){
        for(int j=0;j<=(len-1);j+=1){
            if(temp[j]>MAX){
                MAX=temp[j];
                a=j;
            }
        }
        temp[a]=0;
        arr[i]=MAX;
        MAX=0;
    }
    return arr;
}