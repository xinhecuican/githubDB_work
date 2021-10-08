package 第八章.例6;

public class Consumer extends Thread{

	private Buffer br;
	public Consumer(Buffer br){
		this.br = br;
	}
	
	public void run(){
		for(int i=0;i<5;i++){
			synchronized(br){
				char ch = br.get();
				
				if(ch != '\0'){
					System.out.println("消费者"+i+"消费了产品"+ch);
				}else{
					System.out.println("消费者"+i+"没有产品可以消费");
				}
			}
			
			try {
				sleep(5);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		}
	}
	
	public static void main(String[] args) {
		
		Buffer br  = new Buffer();
		Procedure p = new Procedure(br);
		Consumer c = new Consumer(br);
		p.start();
		c.start();
		
	}

}
