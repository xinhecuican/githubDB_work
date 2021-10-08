package 第二章.例4;

public class SelfAdd {

	public static void self(){
		
		int j=2,i=3;
		j*=i-=(i++);//i++只有在有循环中有意义,及下一轮循环时,i+1，这里没有循环，所以i++没有意义
		            //j=j*=(i=i-(i++));j=j*(i=i-(i));j=j*0=0;
		
		System.out.println("j="+j+","+"i="+i);
		
		j=2;i=3;
		j*=i-=(++i);//j =j*(i =i-(++i)); j= 2*(i=3-(++3));j=-2;
					//++i与i++不一样
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
