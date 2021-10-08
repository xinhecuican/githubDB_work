#include <iostream>  //框架
using namespace std;
// 找到最重的小猪的体重
int main()
{ //创建五只小猪的体重的数组
    int arr[5] = {300,350,200,400,250};
//从数组中找到最重的猪
int max =0;
for (int i = 0; i < 5; i++)
{
    if (arr[i] > max)
    {
        max = arr[i];
        /* code */
    }  
    /* code */
}
//打印最大值
cout <<"最重的小猪的体重为：" << max << endl;
    system("pause");
    return 0; 
}

// 循环加判断
