package ������.��4;

public class Person implements Openning,Closing{  // �˵����Ա�������������û�й�ϵ�����Բ������Ա������ֻ�����Ա����

	private String name;
	
	
	public Person(String name) {
	super();
	this.name = name;
}
	
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}


public void controlClose() {
	System.out.println("�ر�");
}

public void controlOpen() {
	System.out.println(this.name+"��");
	
}
}
