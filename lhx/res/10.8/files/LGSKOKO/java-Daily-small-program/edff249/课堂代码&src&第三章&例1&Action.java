package ������.��1;

public class Action { //���̾籾������Ҫ������ʵ�壬��������ʵ����ı��������ﶼҪ����
	                  //ÿ��ϵͳ������ʵ���࣬�Լ����ڶ�ʵ�������������������̵���
	                  

	private Elephant aElephant;//ע�⣺���ﶼ�Ƕ����ͱ��������Ƕ���
	private IceBox aIceBox;
	private Person aPerson;
	
	private String name;
	
	
	
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	

	public Elephant getaElephant() {
		return aElephant;
	}

	public void setaElephant(Elephant aElephant) {
		this.aElephant = aElephant;
	}

	public IceBox getaIceBox() {
		return aIceBox;
	}

	public void setaIceBox(IceBox aIceBox) {
		this.aIceBox = aIceBox;
	}

	public Person getaPerson() {
		return aPerson;
	}

	public void setaPerson(Person aPerson) {
		this.aPerson = aPerson;
	}
    public void action(){
		
		aPerson.pull();
		aIceBox.open();
		aElephant.enter();
		aPerson.push();
		aIceBox.close();
	}
}
