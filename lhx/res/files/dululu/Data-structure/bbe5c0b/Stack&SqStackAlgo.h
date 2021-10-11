#pragma once
Status InitStack(SqStack& S)
{ /* ����һ����ջ S */
	S.base = (SElemType*)malloc(STACK_INIT_SIZE * sizeof(SElemType));
	if (!S.base)
	{
		exit(OVERFLOW);
	}/* �洢����ʧ�� */
	S.top = S.base;
	S.stacksize = STACK_INIT_SIZE;
	return OK;
}
Status DestroyStack(SqStack& S)
{ /* ����ջ S��S ���ٴ��� */
	free(S.base);
	S.base = NULL;
	S.top = NULL;
	S.stacksize = 0;
	return OK;
}
Status ClearStack(SqStack& S)
{ /* �� S ��Ϊ��ջ */
	S.top = S.base;
	return OK;
}
Status StackEmpty(SqStack S)
{ /* ��ջ S Ϊ��ջ���򷵻� TRUE�����򷵻� FALSE */
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
{ /* ���� S ��Ԫ�ظ�������ջ�ĳ��� */
	return S.top - S.base;
}
Status GetTop(SqStack S, SElemType& e)
{ /* ��ջ���գ����� e ���� S ��ջ��Ԫ�أ������� OK;���򷵻� ERROR */
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
{ /* ����Ԫ�� e Ϊ�µ�ջ��Ԫ�� */
	if (S.top - S.base >= S.stacksize) /* ջ����׷�Ӵ洢�ռ� */
	{
		S.base = (SElemType*)realloc(S.base, (S.stacksize + STACKINCREMENT) * sizeof(SElemType));
		if (!S.base)
		{
			exit(OVERFLOW);
		}/* �洢����ʧ�� */
		S.top = S.base + S.stacksize;
		S.stacksize += STACKINCREMENT;
	}
	*(S.top)++ = e;
	return OK;
}
Status Pop(SqStack& S, SElemType& e)
{ /* ��ջ���գ���ɾ�� S ��ջ��Ԫ�أ��� e ������ֵ�������� OK;���򷵻� ERROR */
	if (S.top == S.base)
	{
		return ERROR;
	}
	e = *--S.top;
	return OK;
}
Status StackTraverse(SqStack S, Status(*visit)(SElemType))
{ /* ��ջ�׵�ջ�����ζ�ջ��ÿ��Ԫ�ص��ú��� visit()�� */
/* һ�� visit()ʧ�ܣ������ʧ�� */
	while (S.top > S.base)
	{
		visit(*S.base++);
	}
	printf("\n");
	return OK;
}
void conversion10_8() 
{ /* �������������һ���Ǹ�ʮ������������ӡ��������ֵ�İ˽����� */
	SqStack s;
	unsigned n; /* �Ǹ����� */
	SElemType e;
	InitStack(s); /* ��ʼ��ջ */
	printf("Enter an number(>=0): ");
	scanf_s("%u", &n); /* ����Ǹ�ʮ�������� n */
	while (n) /* �� n ������ 0 */
	{
		Push(s, n % 8); /* ��ջ n ���� 8 ������(8 ���Ƶĵ�λ) */
		n = n / 8;
	}
	while (!StackEmpty(s)) /* ��ջ���� */
	{
		Pop(s, e); /* ����ջ��Ԫ���Ҹ�ֵ�� e */
		printf("%d", e); /* ��� e */
	}
printf("\n");
}
void conversion10_16()
{ /* �������������һ���Ǹ� 10 ������������ӡ��������ֵ�� 16 ������ */
	SqStack s;
	unsigned n; /* �Ǹ����� */
	SElemType e;
	InitStack(s); /* ��ʼ��ջ */
	printf("Enter an number(>=0): ");
	scanf_s("%u", &n); /* ����Ǹ�ʮ�������� n */
	while (n) /* �� n ������ 0 */
	{
		Push(s, n % 16); /* ��ջ n ���� 16 ������(16 ���Ƶĵ�λ) */
		n = n / 16;
	}
	while (!StackEmpty(s)) /* ��ջ���� */
	{
		Pop(s, e); /* ����ջ��Ԫ���Ҹ�ֵ�� e */
		if (e <= 9)
			printf("%d", e);
		else
			printf("%c", e + 55);
	}
printf("\n");
}
