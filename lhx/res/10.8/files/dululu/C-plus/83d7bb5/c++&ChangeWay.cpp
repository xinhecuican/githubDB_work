
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n[10];
    int i, j;
    int temp; //���ڻ�����Ҫ����������
    cout << "������ʮ�����֣�" << endl;
    for (i = 0; i < 10; i++)
    {
        cin >> n[i];
    }
    for (i = 0; i < 9; i++)
    { //������9��
        for (j = 0; j < 9 - i; j++)
        { //��ÿһ������10-i�������Ƚ�
            if (n[j] > n[j + 1])
            {
                temp = n[j];
                n[j] = n[j + 1];
                n[j + 1] = temp;
            }
        }
    }
    cout << "�����������ǣ�" << endl;
    for (i = 0; i < 10; i++)
    {
        cout << n[i] << ' ';
    }
    cout << endl;
    system("pause");
    return 0;
}



// ��ģ�һֱ�и������޷��������֮�������
// ɵ�ˣ����ǻ����뷨��