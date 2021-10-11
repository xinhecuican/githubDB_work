#define CHAR /* �ַ��ͣ� �����ǲ����ַ�����Ϊ�������� */
/* #define INT /* ���ͣ�����ѡһ�� */
#include"pubuse.h" /* ��ʵ��һ��������ͬ */
#ifdef CHAR
typedef char TElemType;
TElemType Nil = ' '; /* �ַ����Կո��Ϊ�� */
#endif
#ifdef INT
typedef int TElemType;
TElemType Nil = 0; /* ������ 0 Ϊ�� */
#endif
#include"BinTreeDef.h" /* ��������ʽ�洢�ṹ���� */
#include"BinTreeAlgo.h" /* �����������㷨����չ�㷨���� */
Status visitT(TElemType e)
{
#ifdef CHAR
		printf("%c ", e);
#endif
#ifdef INT
		printf("%d ", e);
#endif
		return OK;
}
void main()
{
	int i;
	BiTree T, p, c;
	TElemType e1, e2;

	InitBiTree(T);
	printf("����ն�������,���շ�%d(1:�� 0:��) �������=%d\n", BiTreeEmpty(T), BiTreeDepth(T));
	e1 = Root(T);
	if (e1 != Nil)
#ifdef CHAR
		printf("�������ĸ�Ϊ: %c\n", e1);
#endif
#ifdef INT
	printf("�������ĸ�Ϊ: %d\n", e1);
#endif
	else
		printf("���գ��޸�\n");
#ifdef CHAR
	printf("���������������(��:ab �����ո��ʾ a Ϊ�����,b Ϊ�������Ķ�����)\n");
#endif
#ifdef INT
	printf("���������������(��:1 2 0 0 0 ��ʾ 1 Ϊ�����,2 Ϊ�������Ķ�����)\n");
#endif
	CreateBiTree(T);
	printf("������������,���շ�%d(1:�� 0:��) �������=%d\n", BiTreeEmpty(T), BiTreeDepth(T));
	e1 = Root(T);
	if (e1 != Nil)
#ifdef CHAR
		printf("�������ĸ�Ϊ: %c\n", e1);
#endif
#ifdef INT
	printf("�������ĸ�Ϊ: %d\n", e1);
#endif
	else
		printf("���գ��޸�\n");
	printf("����ݹ����������:\n");
	InOrderTraverse(T, visitT);
	printf("����ݹ����������:\n");
	PostOrderTraverse(T, visitT);
}