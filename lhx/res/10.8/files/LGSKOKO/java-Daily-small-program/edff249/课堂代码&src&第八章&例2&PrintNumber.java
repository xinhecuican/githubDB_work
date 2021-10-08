package 第八章.例2;

public class PrintNumber implements Runnable {//一开始没有 extends Thread输出固定

	
	private int num;						//?继承Thread类就像继承线程编程,还要提供实现·Runnable接口的方法
											//是因为有时一个类要继承其他的类 而Java只允许继承一个类
											//比如一个图形界面类 必须继承JFrame 而不能继承Thread
	
	public PrintNumber( int num){
		
		
		this.num = num;
	}
	
	public void run(){
		
		for(int i=0; i<num; i++){
			   
			System.out.print(i);
		}
		
	}
	
	public static void main(String[] args) {
		
		PrintNumber t1 = new PrintNumber(50);
		PrintLetter t2 = new PrintLetter('a',50);
		
		new Thread(t1).start();			//extends Tread后 此处调用的start()不出错 是因为start（）是Tread类中		
		new Thread(t2).start();			//该类没有继承Threa， 因此 不能调用start（）
							//如何既创建线程线程对象，又和t1有关联 采用“披着羊皮的狼”这种方法
									
	}
	
	

}
