package ������.��3;

public class Action { //���̾籾������Ҫ������ʵ�壬��������ʵ����ı��������ﶼҪ����
	                  //ÿ��ϵͳ������ʵ���࣬�Լ����ڶ�ʵ�������������������̵���
	                  //���޸Ĺرգ������ӿ��ţ�ע�⣬���ﶼ�Ƕ����ͱ��������Ƕ���
	                  

	private Animal aAnimal;
	private Box aBox;
	private Person aPerson;
	private String name;
	
	 public Action(String name) {
			super();
			this.name = name;
		}

	public Animal getaAnimal() {
		return aAnimal;
	}

	public void setaAnimal(Animal aAnimal) {
		this.aAnimal = aAnimal;
	}

	
	
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	

	//public Elephant getaElephant() {
	//	return aElephant;
	//}

	//public void setaElephant(Elephant aElephant) {
	//	this.aElephant = aElephant;
	//}

	
	public Box getaBox() {
		return aBox;
	}

	public void setaBox(Box aBox) {
		this.aBox = aBox;
	}
    public Person getaPerson(){
		return aPerson;
	}
	
    public void setaPerson(Person aPerson) {
		this.aPerson = aPerson;
	}

	public void action(){
		System.out.println(this.getName());
		aPerson.pull();
		aBox.open();
		aAnimal.enter();    //���������
		aPerson.push();
		aBox.close();
	}
}
