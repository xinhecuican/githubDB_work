
Status ListInit_Sq(SqList& L)
{ /* 操作结果：构造一个空的顺序线性表 */
	L.elem = (ElemType*)malloc(LIST_INIT_SIZE * sizeof(ElemType));
	if (!L.elem)
	{
		exit(OVERFLOW); /* 存储分配失败 */
	}
	L.length = 0; /* 空表长度为 0 */
	L.listsize = LIST_INIT_SIZE; /* 初始存储容量 */
	return OK;
}
Status ListInsert_Sq(SqList& L, int i, ElemType e) 
{ 
/* 操作结果：在 L 中第 i 个位置之前插入新的数据元素 e，L 的长度加 1 */
	ElemType* newbase, * q, * p;
	if (i<1 || i>L.length + 1) /* i 值不合法 */
	{
		return ERROR;
	}
	if (L.length >= L.listsize) /* 当前存储空间已满,增加分配 */
	{
		newbase = (ElemType*)realloc(L.elem, (L.listsize + LISTINCREMENT) * sizeof(ElemType));
		if (!newbase) 
		{
			exit(OVERFLOW); /* 存储分配失败 */
		}
		L.elem = newbase;
		L.listsize += LISTINCREMENT; /* 增加存储容量 */
	}
	q = L.elem + i - 1; /* q 为插入位置 */
	for (p = L.elem + L.length - 1; p >= q; --p) /* 插入位置及之后的元素右移 */
	{
		*(p + 1) = *p;
	}
	*q = e; /* 插入 e */
	++L.length; /* 表长增 1 */
	return OK;
}
Status ListDelete_Sq(SqList& L, int i, ElemType* e) /* 算法 2. 5 */
{ /* 初始条件：顺序线性表 L 已存在，1≤i≤ListLength(L) */
/* 操作结果：删除 L 的第 i 个数据元素，并用 e 返回其值，L 的长度减 1 */
	ElemType* p, * q;
	if (i<1 || i>L.length) /* i 值不合法 */
	{
		return ERROR;
	}
	p = L.elem + i - 1; /* p 为被删除元素的位置 */
	*e = *p; /* 被删除元素的值赋给 e */
	q = L.elem + L.length - 1; /* 表尾元素的位置 */
	for (++p; p <= q; ++p) /* 被删除元素之后的元素左移 */
	{
		*(p - 1) = *p;
	}
	L.length--; /* 表长减 1 */
	return OK;
}
Status ListReverse_Sq(SqList& L)
{ /* 初始条件：顺序线性表 L 已存在 */
/* 操作结果：依次对 L 的数据元素成对交换*/
	ElemType t;
	int i;
	for (i = 0; i < L.length / 2; i++)
	{
		t = L.elem[i];
		L.elem[i] = L.elem[L.length - i - 1];
		L.elem[L.length - i - 1] = t;
	}
	printf("\n");
	return OK;
}
Status ListPrint_Sq(SqList L)
{ /* 初始条件：顺序线性表 L 已存在 */
/* 操作结果：依次对 L 的数据元素输出*/
	int i;
	printf("\n");
	for (i = 0; i < L.length; i++)
	{
	printf("%d ", L.elem[i]);
	}
	return OK;
}