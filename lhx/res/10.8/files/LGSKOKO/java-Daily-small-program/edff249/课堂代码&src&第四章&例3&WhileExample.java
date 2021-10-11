package 第四章.例3;

public class WhileExample {
	
	private int startNum, sum, endNum;

	
	public void set (int starNum,int endNum) {
		this.startNum = starNum;
		this.endNum = endNum;
	}

	

	public void print(){
		System.out.println(this.startNum+ "到" + this.endNum + "之间的连加和：");
	}
	public void whileEx(){
		while (startNum<=endNum){
			sum +=startNum;
			startNum++;
		}
		System.out.println("sum ="+sum +",最后计数器多运行一次，值为"+startNum);
	}
	
}
