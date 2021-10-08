typedef struct QNode
{
	QElemType data;
		struct QNode* next;
}QNode, * QueuePtr;
typedef struct
	{
		QueuePtr front, rear; /* 队头、队尾指针 */
	}LinkQueue;
