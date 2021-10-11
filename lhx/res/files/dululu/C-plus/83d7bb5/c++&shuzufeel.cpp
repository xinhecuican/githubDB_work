#include <iostream> //框架
using namespace std;

int main()
{
    //创建二维数组
    int scores[3][3] =
        {
            {100, 100, 100},
            {90, 50, 100},
            {60, 70, 80}
        };
    //string name[3] = {"张三","李四","王五"};

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            //sum += scores[i][j];
            cout << scores[i][j] << " ";
            /* code */
        }
        //cout << " 第 "<< i+1 << "个人的总分为："<< sum << endl;
        cout << endl;
    }

    system("pause");
    return 0;
}
// . Shift + Alt + F 实现代码的对齐；.
