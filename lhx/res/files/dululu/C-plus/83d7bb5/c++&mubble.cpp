#include <iostream> //框架
using namespace std;

int main()
{
    int arr[9] = {2, 4, 0, 5, 7, 1, 3, 8, 9};
    cout << "排序前： " << endl;
    for (int i = 0; i < 9; i++)
    {
        cout << arr[i] << ' ';//每个数之间输出一个空格
        /* code */
    }
    cout << endl;
    // 开始写冒泡排序
    for (int i = 0; i < 8; i++)
    {
        for (int j = 0; j < 8 - i; j++)
        {
            // 如果第一个数字比第二个数字大，交换数字
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    /* 内层循环对比*/
    cout << "排序后：" << endl;
    for (int i = 0; i < 9; i++)
    {
        cout << arr[i] << ' ';
    }
    cout << endl;

    // 排序后结果

    system("pause");
    return 0;
}

// 错了一个字母，服了