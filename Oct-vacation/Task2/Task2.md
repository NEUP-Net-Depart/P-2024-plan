### 1.C++的列表方法

std::list\<T> list={...}，其中T是存储的数据类型，选用int

### 2.C++的循环方法及构建函数

1. do {

   } while()来实现循环

2. void构建函数，其意思为不返回任何值。

3. (std::list\<int>& nums){

   这是函数的参数列表，表示该函数接收一个参数。`std::list\<int>&：`这是参数的类型，表示该参数是一个 `std::list\<int> `类型的引用。引用意味着函数内部对参数的修改将直接影响到原始列表。``nums：``这是参数的名称，用于在函数内部标识这个特定的列表对象。

   } （后边发现没法使用）

4. 列表访问:

   ```C++
   void Sort(std::list<int>& nums) {
       int n=nums.size();//获取列表的长度
       int end = n-1;
       while(end>0){
           int pos=0;
           for(int j=0;j<end;++j){
               if(nums[j]>nums[j+1]){
                   pos=j//交换位置,并且记录在哪里交换
                   int tmp =nums[j]; nums[j]=nums[j+1]; nums[j+1]=tmp;//引入临时变量，交换元素
               }
               end = pos;//更新结束位置
           }
       }
   }
   ```

   不能这样访问。(不能用nums[i]的方式访问)

5. 使用数组可以访问，其中函数中要写``void Sort(std::array<int, 8>& nums) ``其中std::array可以确定一个数组（包括长度，内容等）。

   **`std::array<int, 8>&`**：这是函数的参数类型。它表示一个对 `std::array<int, 8>` 类型数组的引用。`std::array<int, 8>` 是一个包含 8 个整数的数组，而 `&` 符号表示该参数是一个引用，而不是一个值的副本。这意味着在函数内部对数组的修改将直接影响到调用函数时传入的数组。
