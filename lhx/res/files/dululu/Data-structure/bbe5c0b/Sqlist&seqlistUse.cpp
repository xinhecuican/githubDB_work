#include"pubuse.h" 
typedef int ElemType; 
#include"seqlistDef.h" 
#include"seqlistAlgo.h" 
void main()
{
	SqList L;
	Status i;
	int j;
	ElemType t;
	/* ����һ��Ҫ��ʼ��˳��� */
	i = ListInit_Sq(L);
	if (i == 1) /* �����ձ� L �ɹ� */
	{
		for (j = 1; j <= 5; j++) /* �ڱ� L �в��� 5 ��Ԫ�أ�ÿ��Ԫ�ص�ֵ�ֱ�Ϊ 2��4��6��8��10 */
		{
			i = ListInsert_Sq(L, j, 2 * j);
		}
		ListPrint_Sq(L); /*����һ�²���Ľ��������� L ������ */
		ListInsert_Sq(L, 2,27);/* ���ָ�������λ�ã������ڵڶ���Ԫ��ǰ�����µ�Ԫ�أ���ֵΪ 20 */
		ListDelete_Sq(L, 4,&t);/* ���ָ��ɾ����λ�ã�����Ե��ĸ�Ԫ�ؽ���ɾ�� */
		printf("\n The Deleted value is %d", t);/* ����һ��ɾ����Ԫ�ص�ֵ */
		ListPrint_Sq(L);/* ����һ�²����ɾ����Ľ��������� La ������ */
		ListReverse_Sq(L);/* ��˳��� La ������Ԫ�ؽ������� */
		ListPrint_Sq(L);/* ����һ������Ľ��������� L ������ */
	}
}

