package �ڰ���.��4;

public class Account {     //�˻���

	
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
			System.out.println("ȡ�����Ϊ��ֵ");
			return 0;
		}
		else if(balance <amount){
			System.out.println("ȡ�������");
			return 0;
		}
		else{
			balance = balance-amount;
			return amount;
		}
	}
	
}
