package ������.��4;

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
		

		System.out.println("�ر�");
	}

	public void controlOpen() {
	

		System.out.println("����");
	}

}
