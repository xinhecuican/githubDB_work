#include <iostream> //���
using namespace std;

int main()
{
    int arr[9] = {2, 4, 0, 5, 7, 1, 3, 8, 9};
    cout << "����ǰ�� " << endl;
    for (int i = 0; i < 9; i++)
    {
        cout << arr[i] << ' ';//ÿ����֮�����һ���ո�
        /* code */
    }
    cout << endl;
    // ��ʼдð������
    for (int i = 0; i < 8; i++)
    {
        for (int j = 0; j < 8 - i; j++)
        {
            // �����һ�����ֱȵڶ������ִ󣬽�������
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    /* �ڲ�ѭ���Ա�*/
    cout << "�����" << endl;
    for (int i = 0; i < 9; i++)
    {
        cout << arr[i] << ' ';
    }
    cout << endl;

    // �������

    system("pause");
    return 0;
}

// ����һ����ĸ������