//给定一个长度为n的数列，将这个数列按从小到大的顺序排列。

# include <vector>
# include <iostream>
#include <algorithm>

void sort(std::vector<int> &nums )   //选择排序
{
    int n = nums.size();
    for(int i = 0; i < n-1; i+=1 )
    {
        int a = i;
        for (int j = i+1; j<n; j+=1)
        {
            if(nums[j] < nums [a])
                a =   j ;
        }
        std::swap(nums[i],nums[a]);
    }

}

int main()
{
    int n ;
    std::cin >> n ;     //输入数列长度

    std::vector<int> nums(n);    //初始化数组，把数列各项输入数组
    for (int i = 0; i < n; i+=1) 
    {  
        std::cin >> nums[i];  
    } 
    
    sort(nums);          //排序

    int size = nums.size() ;
    for (int i = 0; i < size; i+=1) 
    {  
        std::cout << nums[i] << " ";     // 使用循环遍历数组并输出每个元素  
    }  

}
