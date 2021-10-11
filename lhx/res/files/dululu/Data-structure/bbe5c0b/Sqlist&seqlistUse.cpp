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
	/* 首先一定要初始化顺序表 */
	i = ListInit_Sq(L);
	if (i == 1) /* 创建空表 L 成功 */
	{
		for (j = 1; j <= 5; j++) /* 在表 L 中插入 5 个元素，每个元素的值分别为 2，4，6，8，10 */
		{
			i = ListInsert_Sq(L, j, 2 * j);
		}
		ListPrint_Sq(L); /*检验一下插入的结果，输出表 L 的内容 */
		ListInsert_Sq(L, 2,27);/* 随机指定插入点位置，假设在第二个元素前插入新的元素，其值为 20 */
		ListDelete_Sq(L, 4,&t);/* 随机指定删除点位置，假设对第四个元素进行删除 */
		printf("\n The Deleted value is %d", t);/* 检验一下删除点元素的值 */
		ListPrint_Sq(L);/* 检验一下插入和删除后的结果，输出表 La 的内容 */
		ListReverse_Sq(L);/* 将顺序表 La 的所有元素进行逆序 */
		ListPrint_Sq(L);/* 检验一下逆序的结果，输出表 L 的内容 */
	}
}

