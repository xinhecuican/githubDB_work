
Status InitBiTree(BiTree& T)
{ /* �������: ����ն����� T */
	T = NULL;
	return OK;
}
void DestroyBiTree(BiTree& T)
{ /* ��ʼ����: ������ T ���ڡ��������: ���ٶ����� T */
	if (T) /* �ǿ��� */
	{
		if (T->lchild) /* ������ */
		{
			DestroyBiTree(T->lchild); /* ������������ */
		}
		if (T->rchild) /* ���Һ��� */
		{
			DestroyBiTree(T->rchild); /* �����Һ������� */
		}
	free(T); /* �ͷŸ���� */
	T = NULL; /* ��ָ�븳 0 */
	}
}
#define ClearBiTree DestroyBiTree
void CreateBiTree(BiTree& T)
{ /* �㷨 6.4:�������������������н���ֵ����Ϊ�ַ��ͻ����ͣ��������� */
	TElemType ch;
#ifdef CHAR
		scanf("%c", &ch);
#endif
#ifdef INT
		scanf("%d", &ch);
#endif
		if (ch == Nil) /* �� */
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
			T->data = ch; /* ���ɸ���� */
			CreateBiTree(T->lchild); /* ���������� */
			CreateBiTree(T->rchild); /* ���������� */
		}
}
Status BiTreeEmpty(BiTree T)
{ /* ��ʼ����: ������ T ���� */
/* �������: �� T Ϊ�ն�����,�򷵻� TRUE,���� FALSE */
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
{ /* ��ʼ����: ������ T ���ڡ��������: ���� T ����� */
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
{ /* ��ʼ����: ������ T ���ڡ��������: ���� T �ĸ� */
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
{ /* ��ʼ����: ������ T ���ڣ�p ָ�� T ��ĳ����� */
/* �������: ���� p ��ָ����ֵ */
	return p->data;
}
void Assign(BiTree p, TElemType value)
{ /* �� p ��ָ��㸳ֵΪ value */
	p->data = value;
}
void PreOrderTraverse(BiTree T, Status(*Visit)(TElemType))
{ /* ��ʼ����: ������ T ����,Visit �ǶԽ�������Ӧ�ú������㷨 6.1���иĶ� */
/* �������: ����ݹ���� T,��ÿ�������ú��� Visit һ���ҽ�һ�� */
	if (T) /* T ���� */
	{
		Visit(T->data); /* �ȷ��ʸ���� */
		PreOrderTraverse(T->lchild, Visit); /* ��������������� */
		PreOrderTraverse(T->rchild, Visit); /* ���������������� */
	}
}
void InOrderTraverse(BiTree T, Status(*Visit)(TElemType))
{ /* ��ʼ����: ������ T ����,Visit �ǶԽ�������Ӧ�ú��� */
/* �������: ����ݹ���� T,��ÿ�������ú��� Visit һ���ҽ�һ�� */
	if (T)
	{
		InOrderTraverse(T->lchild, Visit); /* ��������������� */
		Visit(T->data); /* �ٷ��ʸ���� */
		InOrderTraverse(T->rchild, Visit); /* ���������������� */
	}
}
void PostOrderTraverse(BiTree T, Status(*Visit)(TElemType))
{ /* ��ʼ����: ������ T ����,Visit �ǶԽ�������Ӧ�ú��� */
		/* �������: ����ݹ���� T,��ÿ�������ú��� Visit һ���ҽ�һ�� */
	if (T) /* T ���� */
	{
		PostOrderTraverse(T->lchild, Visit); /* �Ⱥ������������ */
		PostOrderTraverse(T->rchild, Visit); /* �ٺ������������ */
		Visit(T->data); /* �����ʸ���� */
	}
}
