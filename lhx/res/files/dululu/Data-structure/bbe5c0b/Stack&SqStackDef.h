#define STACK_INIT_SIZE 10 /* �洢�ռ��ʼ������ */
#define STACKINCREMENT 2 /* �洢�ռ�������� */
typedef struct SqStack
{
	SElemType* base; /* ��ջ����֮ǰ������֮��base ��ֵΪ NULL */
		SElemType* top; /* ջ��ָ�� */
		int stacksize; /* ��ǰ�ѷ���Ĵ洢�ռ䣬��Ԫ��Ϊ��λ */
}SqStack; /* ˳��ջ */ 
