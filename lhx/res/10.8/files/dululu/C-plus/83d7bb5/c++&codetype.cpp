#include <iostream>  //���
using namespace std;

// 1.�޲��޷�
void test01()
{
    cout <<"This the first test type" << endl;
}


// 2.�в��޷�
void test02(int a)
{
    cout <<"a =" << a << endl;
}

// 3.�޲��з�
int test03()
{
    cout <<"This is test03 " << endl;
    return 1000;
}

// 4. �в��з�
int test04(int a)
{
cout <<"this is test04 a ="<< a << endl;
return a;
}

int main()
{
    test01();
    test02(100);

    int num1 = test03();
    cout << "num1= "<< num1 << endl;

    int num2 = test04(100000);
    cout <<"num2= "<<num2<< endl;

    system("pause");
    
}
