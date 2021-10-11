package 第八章.例4;

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
		String str = Thread.currentThread().getName()+"取款前余额："+account.getBalance();
		try{
			sleep(2000);
		}catch(InterruptedException e){
			e.printStackTrace();
		}
		System.out.println(str+"取款："+account.withDraw(amount)+"取款后余额："+account.getBalance());
	}
	}
	public static void main(String[] args) {
	
		Account a = new Account(500);
		for(int i=0;i<10;i++){
			(new MultiWithDraw(a,10+i)).start(); //10个线程，相当于10个取款人
		}
	}
}
