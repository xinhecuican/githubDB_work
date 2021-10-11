package 第十章.例4;

class MyInt implements java.io.Serializable{
	
	private int value;
	private String number;
	private static int count = 0;
	
	public MyInt(int v){
		this.number =""+this.count;
		this.value = v;
		this.count++;
	}
	
	public String toString(){
		return "第" + this.number+"个数字的值是："+this.value;
	}
}
