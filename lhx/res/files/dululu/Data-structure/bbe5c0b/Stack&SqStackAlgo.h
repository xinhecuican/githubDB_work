#pragma once
Status InitStack(SqStack& S)
{ /* 构造一个空栈 S */
	S.base = (SElemType*)malloc(STACK_INIT_SIZE * sizeof(SElemType));
	if (!S.base)
	{
		exit(OVERFLOW);
	}/* 存储分配失败 */
	S.top = S.base;
	S.stacksize = STACK_INIT_SIZE;
	return OK;
}
Status DestroyStack(SqStack& S)
{ /* 销毁栈 S，S 不再存在 */
	free(S.base);
	S.base = NULL;
	S.top = NULL;
	S.stacksize = 0;
	return OK;
}
Status ClearStack(SqStack& S)
{ /* 把 S 置为空栈 */
	S.top = S.base;
	return OK;
}
Status StackEmpty(SqStack S)
{ /* 若栈 S 为空栈，则返回 TRUE，否则返回 FALSE */
	if (S.top == S.base)
	{
		return TRUE;

	}
	else
	{
		return FALSE;
	}
}
int StackLength(SqStack S)
{ /* 返回 S 的元素个数，即栈的长度 */
	return S.top - S.base;
}
Status GetTop(SqStack S, SElemType& e)
{ /* 若栈不空，则用 e 返回 S 的栈顶元素，并返回 OK;否则返回 ERROR */
	if (S.top > S.base)
	{
		e = *(S.top - 1);
		return OK;
	}
	else
	{
		return ERROR;
	}
}
Status Push(SqStack& S, SElemType e)
{ /* 插入元素 e 为新的栈顶元素 */
	if (S.top - S.base >= S.stacksize) /* 栈满，追加存储空间 */
	{
		S.base = (SElemType*)realloc(S.base, (S.stacksize + STACKINCREMENT) * sizeof(SElemType));
		if (!S.base)
		{
			exit(OVERFLOW);
		}/* 存储分配失败 */
		S.top = S.base + S.stacksize;
		S.stacksize += STACKINCREMENT;
	}
	*(S.top)++ = e;
	return OK;
}
Status Pop(SqStack& S, SElemType& e)
{ /* 若栈不空，则删除 S 的栈顶元素，用 e 返回其值，并返回 OK;否则返回 ERROR */
	if (S.top == S.base)
	{
		return ERROR;
	}
	e = *--S.top;
	return OK;
}
Status StackTraverse(SqStack S, Status(*visit)(SElemType))
{ /* 从栈底到栈顶依次对栈中每个元素调用函数 visit()。 */
/* 一旦 visit()失败，则操作失败 */
	while (S.top > S.base)
	{
		visit(*S.base++);
	}
	printf("\n");
	return OK;
}
void conversion10_8() 
{ /* 对于输入的任意一个非负十进制整数，打印输出与其等值的八进制数 */
	SqStack s;
	unsigned n; /* 非负整数 */
	SElemType e;
	InitStack(s); /* 初始化栈 */
	printf("Enter an number(>=0): ");
	scanf_s("%u", &n); /* 输入非负十进制整数 n */
	while (n) /* 当 n 不等于 0 */
	{
		Push(s, n % 8); /* 入栈 n 除以 8 的余数(8 进制的低位) */
		n = n / 8;
	}
	while (!StackEmpty(s)) /* 当栈不空 */
	{
		Pop(s, e); /* 弹出栈顶元素且赋值给 e */
		printf("%d", e); /* 输出 e */
	}
printf("\n");
}
void conversion10_16()
{ /* 对于输入的任意一个非负 10 进制整数，打印输出与其等值的 16 进制数 */
	SqStack s;
	unsigned n; /* 非负整数 */
	SElemType e;
	InitStack(s); /* 初始化栈 */
	printf("Enter an number(>=0): ");
	scanf_s("%u", &n); /* 输入非负十进制整数 n */
	while (n) /* 当 n 不等于 0 */
	{
		Push(s, n % 16); /* 入栈 n 除以 16 的余数(16 进制的低位) */
		n = n / 16;
	}
	while (!StackEmpty(s)) /* 当栈不空 */
	{
		Pop(s, e); /* 弹出栈顶元素且赋值给 e */
		if (e <= 9)
			printf("%d", e);
		else
			printf("%c", e + 55);
	}
printf("\n");
}
