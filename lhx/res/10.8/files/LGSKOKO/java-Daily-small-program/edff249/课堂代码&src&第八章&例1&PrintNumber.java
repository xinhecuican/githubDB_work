package 第八章.例1;

public class PrintNumber extends Thread {//一开始没有 extends Thread输出固定

	
	private int num;
	
	public PrintNumber( int num){
		
		
		this.num = num;
	}
	
	public void run(){
		
		for(int i=0; i<num; i++){
			   
			System.out.print(i);
		}
		System.out.println();
	}
	
	public static void main(String[] args) {
		
		PrintNumber t1 = new PrintNumber(50);
		PrintLetter t2 = new PrintLetter('a',50);
//		t1.run();					//extends Thread 后 此处是run（），输出也固定
//		t2.run();
		t1.start();					//线程调用start()后  JVM自动调用run()，run（）是线程体，是Tread类中的方法
		t2.start();					//三个概念 线程类  线程对象   线程体
									//虚拟机自动调用的方法   main  actionPerformed run
									//不是对象.，不是对象调用。没有任何元素.它
									//几个线程？ 三个 t1 t2 main
									//多线程的好处：不是每个线程始终占用JVM或CPU
									//网络连接、数据库打开灯线程都需要时间，
									//此空闲时间如果CPU将改时间片分配给其他线程，就会最大程度提高效率
									//就像排队或者等烧开水时 背单词或者看手机
									//该类并没有定义start()方法 但是调用不出错，说明start（）是父类Tread的。
	}
	
	

}
