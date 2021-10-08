package 第八章.例7;

import java.util.Random;

public class Procedure extends Thread {

	private Buffer br;
	Random r = new Random();			//服务器端程序一般不实例化对象，只有到客户端才实例化
										//因此此对象为工具，不可变。到客户端实例化的肯定是可变的
	
	public Procedure(Buffer br) {
		super();
		this.br = br;
	}
	
	public void run(){
		
		for(int i=0;i<5;i++){                   //用于产生线程
			                                    //在底层，字母A用整数65表示
			char ch = (char)(65+r.nextInt(20)); //生产ch，r.nextInt(20)包括0到19的随机整 数
			br.put(ch);                        //放入仓库
			System.out.println("生产者"+i+"生产了产品:"+ch);
			try{
				sleep(5);
			}catch(InterruptedException e){
				
				e.printStackTrace();
			}
			
		}
	}
}
