#include <iostream> //���
using namespace std;

int main()
{
    //������ά����
    int scores[3][3] =
        {
            {100, 100, 100},
            {90, 50, 100},
            {60, 70, 80}
        };
    //string name[3] = {"����","����","����"};

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            //sum += scores[i][j];
            cout << scores[i][j] << " ";
            /* code */
        }
        //cout << " �� "<< i+1 << "���˵��ܷ�Ϊ��"<< sum << endl;
        cout << endl;
    }

    system("pause");
    return 0;
}
// . Shift + Alt + F ʵ�ִ���Ķ��룻.
