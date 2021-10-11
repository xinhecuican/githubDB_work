#include <iostream>  //框架
using namespace std;

int main()
{
    int arry[10] = {0,1,3,4,5,6,7,8,1,3};
    cout <<"整个数组占用的内存空间为："<< sizeof(arry)<< endl;
    cout <<"每个元素所占用的内存空间为："<< sizeof(arry[1]) <<endl;
    system("pause");
    return 0; 
}