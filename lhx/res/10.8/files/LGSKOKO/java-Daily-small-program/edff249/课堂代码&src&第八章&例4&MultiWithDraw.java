package �ڰ���.��4;

public class MultiWithDraw extends Thread{


	private Account account;
	private int amount;
	
	public MultiWithDraw(Account account, int amount) {
		super();
		this.account = account;
		this.amount = amount;
	}

	public void run(){
		
		synchronized(account){
		String str = Thread.currentThread().getName()+"ȡ��ǰ��"+account.getBalance();
		try{
			sleep(2000);
		}catch(InterruptedException e){
			e.printStackTrace();
		}
		System.out.println(str+"ȡ�"+account.withDraw(amount)+"ȡ�����"+account.getBalance());
	}
	}
	public static void main(String[] args) {
	
		Account a = new Account(500);
		for(int i=0;i<10;i++){
			(new MultiWithDraw(a,10+i)).start(); //10���̣߳��൱��10��ȡ����
		}
	}
}
