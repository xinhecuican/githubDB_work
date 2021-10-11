
Status InitBiTree(BiTree& T)
{ /* 操作结果: 构造空二叉树 T */
	T = NULL;
	return OK;
}
void DestroyBiTree(BiTree& T)
{ /* 初始条件: 二叉树 T 存在。操作结果: 销毁二叉树 T */
	if (T) /* 非空树 */
	{
		if (T->lchild) /* 有左孩子 */
		{
			DestroyBiTree(T->lchild); /* 销毁左孩子子树 */
		}
		if (T->rchild) /* 有右孩子 */
		{
			DestroyBiTree(T->rchild); /* 销毁右孩子子树 */
		}
	free(T); /* 释放根结点 */
	T = NULL; /* 空指针赋 0 */
	}
}
#define ClearBiTree DestroyBiTree
void CreateBiTree(BiTree& T)
{ /* 算法 6.4:按先序次序输入二叉树中结点的值（可为字符型或整型，在主程中 */
	TElemType ch;
#ifdef CHAR
		scanf("%c", &ch);
#endif
#ifdef INT
		scanf("%d", &ch);
#endif
		if (ch == Nil) /* 空 */
		{
			T = NULL;
		}
		else
		{
			T = (BiTree)malloc(sizeof(BiTNode));
			if (!T)
			{
				exit(OVERFLOW);
			}
			T->data = ch; /* 生成根结点 */
			CreateBiTree(T->lchild); /* 构造左子树 */
			CreateBiTree(T->rchild); /* 构造右子树 */
		}
}
Status BiTreeEmpty(BiTree T)
{ /* 初始条件: 二叉树 T 存在 */
/* 操作结果: 若 T 为空二叉树,则返回 TRUE,否则 FALSE */
	if (T)
	{
		return FALSE;
	}
	else
	{
		return TRUE;
	}
}
int BiTreeDepth(BiTree T)
{ /* 初始条件: 二叉树 T 存在。操作结果: 返回 T 的深度 */
	int i, j;
	if (!T)
	{
		return 0;
	}
	if (T->lchild)
	{
		i = BiTreeDepth(T->lchild);
	}
	else
	{
		i = 0;
	}
	if (T->rchild)
	{
		j = BiTreeDepth(T->rchild);
	}
	else
	{
		j = 0;
	}
	return i > j ? i + 1 : j + 1;
}
TElemType Root(BiTree T)
{ /* 初始条件: 二叉树 T 存在。操作结果: 返回 T 的根 */
	if (BiTreeEmpty(T))
	{
		return Nil;
	}
	else
	{
		return T->data;
	}
}
TElemType Value(BiTree p)
{ /* 初始条件: 二叉树 T 存在，p 指向 T 中某个结点 */
/* 操作结果: 返回 p 所指结点的值 */
	return p->data;
}
void Assign(BiTree p, TElemType value)
{ /* 给 p 所指结点赋值为 value */
	p->data = value;
}
void PreOrderTraverse(BiTree T, Status(*Visit)(TElemType))
{ /* 初始条件: 二叉树 T 存在,Visit 是对结点操作的应用函数。算法 6.1，有改动 */
/* 操作结果: 先序递归遍历 T,对每个结点调用函数 Visit 一次且仅一次 */
	if (T) /* T 不空 */
	{
		Visit(T->data); /* 先访问根结点 */
		PreOrderTraverse(T->lchild, Visit); /* 再先序遍历左子树 */
		PreOrderTraverse(T->rchild, Visit); /* 最后先序遍历右子树 */
	}
}
void InOrderTraverse(BiTree T, Status(*Visit)(TElemType))
{ /* 初始条件: 二叉树 T 存在,Visit 是对结点操作的应用函数 */
/* 操作结果: 中序递归遍历 T,对每个结点调用函数 Visit 一次且仅一次 */
	if (T)
	{
		InOrderTraverse(T->lchild, Visit); /* 先中序遍历左子树 */
		Visit(T->data); /* 再访问根结点 */
		InOrderTraverse(T->rchild, Visit); /* 最后中序遍历右子树 */
	}
}
void PostOrderTraverse(BiTree T, Status(*Visit)(TElemType))
{ /* 初始条件: 二叉树 T 存在,Visit 是对结点操作的应用函数 */
		/* 操作结果: 后序递归遍历 T,对每个结点调用函数 Visit 一次且仅一次 */
	if (T) /* T 不空 */
	{
		PostOrderTraverse(T->lchild, Visit); /* 先后序遍历左子树 */
		PostOrderTraverse(T->rchild, Visit); /* 再后序遍历右子树 */
		Visit(T->data); /* 最后访问根结点 */
	}
}
