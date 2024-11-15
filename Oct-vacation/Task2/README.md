# Task 2

请补充个人信息后，在此完成报告！

@Author:  李心言
@Email:  1129200163@qq.com

学习排序方法选取了效率比较高并且易于理解的快速排序
编写了随机生成100个从0到100的整数并且将其从小到大排序的算法

学习出现问题的一点是:
```c
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
```
中
因为key选取的是数组里第一个数, 所以应该先将比key小的数放在key前, 不然min++后移动的数据不再是key就会出现bug
因此max--和min++的顺序不可颠倒
