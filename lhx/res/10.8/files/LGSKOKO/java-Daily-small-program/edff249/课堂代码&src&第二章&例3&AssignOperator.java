package �ڶ���.��3;

public class AssignOperator {

	public static void ass(){
		
		int a,b,c,m,n;
		a=b=c=5;      //�൱��a=��b=(c=5)); ��c=5;b=c;a=b;
					  //��ֵ����Զ����ظ�ֵ���ұߵ�ֵ��������������ձ����һ��ֵ
		System.out.println(a+","+b+","+c);
		m=4;n=2;
		m+=m*=n-=m*n;
		//��ֵ���,��������Ľ����,�����ȴ��ұ��ҵ�һ����ֵ���,n=n-m*n��
		//n=n-m*n����=�� �ұߵ����Ѿ���ֵ�� �ұߵ���δ��ֵ��. n=2-4*2=-6;
		//m*=�൱��m=m*;��������m=m*n=4*��-6��=-24;
		//m= m+m=4+��-24��=-20;
		// m=m+(m=m*(n=n-m*n)
		//��ֵ����и��涨,������ֵ��������(����)һ��ֵ
		System.out.println(m+","+n);
	}
	public static void main(String[] args) {
	
		AssignOperator.ass();

	}

}
