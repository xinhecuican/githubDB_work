#define CHAR /* 字符型， 本例是采用字符型作为数据类型 */
/* #define INT /* 整型（二者选一） */
#include"pubuse.h" /* 与实验一的意义相同 */
#ifdef CHAR
typedef char TElemType;
TElemType Nil = ' '; /* 字符型以空格符为空 */
#endif
#ifdef INT
typedef int TElemType;
TElemType Nil = 0; /* 整型以 0 为空 */
#endif
#include"BinTreeDef.h" /* 二叉树链式存储结构定义 */
#include"BinTreeAlgo.h" /* 二叉树基本算法和扩展算法定义 */
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
	printf("构造空二叉树后,树空否？%d(1:是 0:否) 树的深度=%d\n", BiTreeEmpty(T), BiTreeDepth(T));
	e1 = Root(T);
	if (e1 != Nil)
#ifdef CHAR
		printf("二叉树的根为: %c\n", e1);
#endif
#ifdef INT
	printf("二叉树的根为: %d\n", e1);
#endif
	else
		printf("树空，无根\n");
#ifdef CHAR
	printf("请先序输入二叉树(如:ab 三个空格表示 a 为根结点,b 为左子树的二叉树)\n");
#endif
#ifdef INT
	printf("请先序输入二叉树(如:1 2 0 0 0 表示 1 为根结点,2 为左子树的二叉树)\n");
#endif
	CreateBiTree(T);
	printf("建立二叉树后,树空否？%d(1:是 0:否) 树的深度=%d\n", BiTreeEmpty(T), BiTreeDepth(T));
	e1 = Root(T);
	if (e1 != Nil)
#ifdef CHAR
		printf("二叉树的根为: %c\n", e1);
#endif
#ifdef INT
	printf("二叉树的根为: %d\n", e1);
#endif
	else
		printf("树空，无根\n");
	printf("中序递归遍历二叉树:\n");
	InOrderTraverse(T, visitT);
	printf("后序递归遍历二叉树:\n");
	PostOrderTraverse(T, visitT);
}