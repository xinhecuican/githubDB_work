package 第八章.例2;

public class PrintLetter implements Runnable{

	private char letter;
	private int num;
	
	public PrintLetter(char ch, int num){
		
		letter = ch;
		this.num = num;
	}
	
	public void run(){				//如果该句没有,PrintLetter出错 显示add unimplemented methods
									//这说明 run（）方法是Runnable接口中的方法   那么,Tread类中的run（）呢？
									//实际上 Tread类在JDK中已经实现了 Runnable接口 因此，Thread类中的run()来自Runnable
		
		for(int i=0; i<num; i++){
			
			System.out.print(letter);
		}
		
	}
	

}
