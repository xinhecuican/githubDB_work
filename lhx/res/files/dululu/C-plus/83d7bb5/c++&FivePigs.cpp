#include <iostream>  //���
using namespace std;
// �ҵ����ص�С�������
int main()
{ //������ֻС������ص�����
    int arr[5] = {300,350,200,400,250};
//���������ҵ����ص���
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
//��ӡ���ֵ
cout <<"���ص�С�������Ϊ��" << max << endl;
    system("pause");
    return 0; 
}

// ѭ�����ж�
