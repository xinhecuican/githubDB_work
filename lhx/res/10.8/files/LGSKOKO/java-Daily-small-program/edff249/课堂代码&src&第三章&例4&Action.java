package 第三章.例4;

public class Action {
	
//	成员变量
    private Animal aAnimal;
    private Box aBox;
    private Openning aOpenning;
    private Closing  aClosing;
    private String name;
    
   // 构造方法
	public Action(String name) {
		super();
		this.name = name;
	}

//	获取和设置相关成员变量
	public String getName() {
		return name;
	}


	public void setName(String name) {
		this.name = name;
	}
	
	public Animal getaAnimal() {
		return aAnimal;
	}


	public void setaAnimal(Animal aAnimal) {
		this.aAnimal = aAnimal;
	}


	public Box getaBox() {
		return aBox;
	}


	public void setaBox(Box aBox) {
		this.aBox = aBox;
	}




// action方法
	public void action(){
		System.out.println(this.name);
		aOpenning.controlOpen();
		aBox.open();
		aAnimal.enter();
		aAnimal.print();//aAnimal 第一个场景是大象,但是它是上转型对象,上转型对象调用的方法
						//子类的方法,但是这里子类没有这个方法，怎么办？继承下来,调用继承的
						//父类的方法，因此 print()中的num是父类的num 如果子类中也有定义
							//print（）那么，animal作为上转型对象调用的是子类的如
						//Elephant 的print（） 这个print()中的num就是Elephant
		                //的num了，不再是Animal中的num了,也就得不到了有几个动物了.只能得到几个大象了。
		    			// 上转型对象调用的同名的成员变量、同名的static方法是父类的成员变量和方法
						//上转型对象调用的同名实例方法（没有static修饰)，调用的是子类的方法
						//上转型对象调用的实例方法吐过子类没有，父类有调用的是父类的方法
						//但方法正的成员变量还是父类的。
		aClosing.controlClose();
		aBox.close();
	}

	
//	
	public Openning getaOpenning() {
		return aOpenning;
	}

	public void setaOpenning(Openning aOpenning) {
		this.aOpenning = aOpenning;
	}

	public Closing getaClosing() {
		return aClosing;
	}

	public void setaClosing(Closing aClosing) {
		this.aClosing = aClosing;
	}
	
	
    
    
    
}
