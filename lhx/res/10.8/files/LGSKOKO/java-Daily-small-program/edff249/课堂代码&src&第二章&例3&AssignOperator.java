package 第二章.例3;

public class AssignOperator {

	public static void ass(){
		
		int a,b,c,m,n;
		a=b=c=5;      //相当于a=（b=(c=5)); 或c=5;b=c;a=b;
					  //赋值语句自动返回赋值号右边的值，即整个语句最终变成了一个值
		System.out.println(a+","+b+","+c);
		m=4;n=2;
		m+=m*=n-=m*n;
		//赋值语句,从右往左的结合性,既优先从右边找第一个赋值语句,n=n-m*n；
		//n=n-m*n；中=号 右边的是已经赋值的 右边的是未赋值的. n=2-4*2=-6;
		//m*=相当于m=m*;接下来，m=m*n=4*（-6）=-24;
		//m= m+m=4+（-24）=-20;
		// m=m+(m=m*(n=n-m*n)
		//赋值语句有个规定,整个赋值语句最后变成(返回)一个值
		System.out.println(m+","+n);
	}
	public static void main(String[] args) {
	
		AssignOperator.ass();

	}

}
