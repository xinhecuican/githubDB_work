package ������.��4;

public abstract class Animal {
	
	protected static int num;
	
	protected Box aBox;
	
	protected double width,height;
	
	protected String name;

	
	
	
// ���췽��
	public Animal(String name) {
		super();
		this.name = name;
		num++;
	}

//	��ȡ�����÷���
	public String getName() {
		return name;
	}


	public void setName(String name) {
		this.name = name;
	}	
	
	public Box getaBox() {
		return aBox;
	}

	public void setaBox(Box aBox) {
		this.aBox = aBox;
	}

	public double getWidth() {
		return width;
	}

	public void setWidth(double width) {
		this.width = width;
	}

	public double getHeight() {
		return height;
	}

	public void setHeight(double height) {
		this.height = height;
	}

//	��ض�������
	public abstract void enter();
	
	public void set(double width,double height){
		
		this.width = width;
		this.height = height;
	}
	
	public void print(){//�������о���ķ���,������û��,����ת�Ͷ�����õ�������ķ���
		
		System.out.println("���ﹲ"+num+"��");
	}
	
	
}
