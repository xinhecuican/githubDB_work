package 第三章.例4;

public class Electricity implements Openning, Closing {

	private String name;
	
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Electricity(String name) {
		super();
		this.name = name;
	}

	public void controlClose() {
		

		System.out.println("关闭");
	}

	public void controlOpen() {
	

		System.out.println("开门");
	}

}
