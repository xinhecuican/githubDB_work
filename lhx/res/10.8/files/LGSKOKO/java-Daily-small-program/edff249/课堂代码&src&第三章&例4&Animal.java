package 第三章.例4;

public abstract class Animal {
	
	protected static int num;
	
	protected Box aBox;
	
	protected double width,height;
	
	protected String name;

	
	
	
// 构造方法
	public Animal(String name) {
		super();
		this.name = name;
		num++;
	}

//	获取和设置方法
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

//	相关动作方法
	public abstract void enter();
	
	public void set(double width,double height){
		
		this.width = width;
		this.height = height;
	}
	
	public void print(){//父类中有具体的方法,子类中没有,但上转型对象调用的是子类的方法
		
		System.out.println("动物共"+num+"个");
	}
	
	
}
