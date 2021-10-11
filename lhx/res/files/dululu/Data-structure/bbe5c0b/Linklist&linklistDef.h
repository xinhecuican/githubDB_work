#pragma once

struct LNode
{
	ElemType data;
	struct LNode *next;
};
typedef struct LNode *LinkList;