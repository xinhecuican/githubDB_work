package 第八章.例4;

public class Account {     //账户类

	
	private int balance;

	public Account(int balance) {
		super();
		this.balance = balance;
	}

	public int getBalance() {
		return balance;
	}

	public int withDraw(int amount){
		if(amount<0)
		{
			System.out.println("取款金额不能为负值");
			return 0;
		}
		else if(balance <amount){
			System.out.println("取款额超出余额");
			return 0;
		}
		else{
			balance = balance-amount;
			return amount;
		}
	}
	
}
