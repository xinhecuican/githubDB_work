package 第八章.例7;//信号变量的提出 。 局部变量，成员变量、参数变量，this，super,循环变量、下标变量、信号变量
				//期末考试中填空
public class Buffer {        //仓库

	private char chBuffer;
	private boolean empty = true;
	
	public synchronized void put(char ch){   //往仓库中放产品ch
		while(!empty){
			
			try {
				wait();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		chBuffer = ch;                       //ch变成仓库中的chBuffer
		empty = false;
		notify();							//饭做好了 过来吃吧  通知另外一个课程
	}
	
	public synchronized char get(){     
		
		while(empty){
			
			try {
				wait();						//没有饭，只能等。
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		char chr = chBuffer;                //从仓库中提取chBuffer给chr
		chBuffer ='\0';                     //仓库设置为空
		empty = true;
		notify();							//空了 通知生产者生产，叫饭。
		return chr;                         //将从仓库中提取的chr返回
	}
}
