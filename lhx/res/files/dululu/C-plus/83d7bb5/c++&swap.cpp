#include <iostream>  //框架
using namespace std;


void swap(int num1, int num2)
{
  cout << "交换之前： "<< endl;
  cout << "num1 = "<< num1 << endl;
  cout << "num2 = "<< num2 << endl;

  int temp = num1;
  num1 = num2;
  num2 = temp;

  cout << "交换之后： "<< endl;
  cout << "num1 = "<< num1 << endl;
  cout << "num2 = "<< num2 << endl;



 //返回值不需要的时候可以不写return
}


int main()
{
    int a =1;  // 实参
    int b =2;
    swap(a,b);   // 形参
// `形参`发生改变并不会影响`实参`的改变
    system("pause"); 
}

