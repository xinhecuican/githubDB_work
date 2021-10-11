#include "pubuse.h" /* ��ʵ��һ��������ͬ */
typedef int QElemType; /* ������ʽ�����еĽ����һ������ */
#include "linkqueuedef.h"
#include "linkqueuealgo.h"
void visit(QElemType i)
  {
   printf("%d ", i);
  }
 void main()
{
int i;
QElemType d;
LinkQueue q;
	i = InitQueue(q);
	if (i)
	{
		printf("�ɹ��ع�����һ���ն���!\n");
		printf("�Ƿ�ն��У�%d(1:�� 0:��) ", QueueEmpty(q));
		printf("���еĳ���Ϊ%d\n", QueueLength(q));
		EnQueue(q, -5);
		EnQueue(q, 5);
		EnQueue(q, 10);
		printf("���� 3 ��Ԫ��(-5,5,10)��,���еĳ���Ϊ%d\n", QueueLength(q));
		printf("�Ƿ�ն��У�%d(1:�� 0:��) ", QueueEmpty(q));
		printf("���е�Ԫ������Ϊ��");
		QueueTraverse(q, visit);
		i = GetHead_Q(q, d);
		if (i == OK)
		{
			printf("��ͷԪ���ǣ�%d\n", d);
			DeQueue(q, d);
			printf("ɾ���˶�ͷԪ��%d\n", d);
			i = GetHead_Q(q, d);
		}
		if (i == OK)
		{
			printf("�µĶ�ͷԪ���ǣ�%d\n", d);
			ClearQueue(q);
			printf("��ն��к�,q.front=%u q.rear=%u q.front->next=%u\n", q.front, q.rear, q.front->next);
			DestroyQueue(q);
			printf("���ٶ��к�,q.front=%u q.rear=%u\n", q.front, q.rear);
		}
	}
}