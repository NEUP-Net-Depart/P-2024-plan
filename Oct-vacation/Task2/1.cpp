//冒泡排序算法的改进。相比原算法，要求当没有交换时，即排序完成停止排序
//将144,55,35,26,40,15,24,48进行排序
#include <list>
#include <string>
#include <array>
void Sort(std::array<int, 8>& nums) {
    int n=nums.size()-1;//获取列表的长度
    while(n>0){
        int pos=0;
        for(int j=0;j<n;j++)
            if(nums[j]>nums[j+1]){
                pos=j;//交换位置,并且记录在哪里交换
                int tmp =nums[j]; nums[j]=nums[j+1]; nums[j+1]=tmp;//引入临时变量，交换元素
            }
        n = pos;//更新结束位置
    }
}
int main() {
    std::array<int,8>nums={144,55,35,26,40,15,24,48};
    Sort(nums);
    int size =nums.size();
    for (int i = 0; i < size; ++i) {
        printf("%d ", nums[i]);
    }
}