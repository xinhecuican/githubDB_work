package �ڰ���.��6;

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
					System.out.println("������"+i+"�����˲�Ʒ"+ch);
				}else{
					System.out.println("������"+i+"û�в�Ʒ��������");
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
