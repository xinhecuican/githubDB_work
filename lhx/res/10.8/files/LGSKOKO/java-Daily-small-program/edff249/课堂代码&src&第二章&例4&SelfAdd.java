package �ڶ���.��4;

public class SelfAdd {

	public static void self(){
		
		int j=2,i=3;
		j*=i-=(i++);//i++ֻ������ѭ����������,����һ��ѭ��ʱ,i+1������û��ѭ��������i++û������
		            //j=j*=(i=i-(i++));j=j*(i=i-(i));j=j*0=0;
		
		System.out.println("j="+j+","+"i="+i);
		
		j=2;i=3;
		j*=i-=(++i);//j =j*(i =i-(++i)); j= 2*(i=3-(++3));j=-2;
					//++i��i++��һ��
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
