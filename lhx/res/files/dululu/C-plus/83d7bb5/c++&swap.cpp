#include <iostream>  //���
using namespace std;


void swap(int num1, int num2)
{
  cout << "����֮ǰ�� "<< endl;
  cout << "num1 = "<< num1 << endl;
  cout << "num2 = "<< num2 << endl;

  int temp = num1;
  num1 = num2;
  num2 = temp;

  cout << "����֮�� "<< endl;
  cout << "num1 = "<< num1 << endl;
  cout << "num2 = "<< num2 << endl;



 //����ֵ����Ҫ��ʱ����Բ�дreturn
}


int main()
{
    int a =1;  // ʵ��
    int b =2;
    swap(a,b);   // �β�
// `�β�`�����ı䲢����Ӱ��`ʵ��`�ĸı�
    system("pause"); 
}

