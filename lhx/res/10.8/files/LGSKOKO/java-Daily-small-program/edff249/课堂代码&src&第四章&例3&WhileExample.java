package ������.��3;

public class WhileExample {
	
	private int startNum, sum, endNum;

	
	public void set (int starNum,int endNum) {
		this.startNum = starNum;
		this.endNum = endNum;
	}

	

	public void print(){
		System.out.println(this.startNum+ "��" + this.endNum + "֮������Ӻͣ�");
	}
	public void whileEx(){
		while (startNum<=endNum){
			sum +=startNum;
			startNum++;
		}
		System.out.println("sum ="+sum +",��������������һ�Σ�ֵΪ"+startNum);
	}
	
}
