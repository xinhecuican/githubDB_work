
#include<string.h>
#include<ctype.h>
#include<malloc.h>   
#include<limits.h>   
#include<stdio.h>
#include<stdlib.h>
#include<io.h>
#include<math.h>
#include<process.h>
/*函数结果状态代码*/
#define TRUE 1
#define FALSE 0
#define OK 1
#define ERROR 0
#define INFEASIBLE -1

typedef int Status; /* Status 是函数的类型,其值是函数结果状态代码，如 OK 等 */
typedef int Boolean; /* Boolean 是布尔类型,其值是 TRUE 或 FALSE */