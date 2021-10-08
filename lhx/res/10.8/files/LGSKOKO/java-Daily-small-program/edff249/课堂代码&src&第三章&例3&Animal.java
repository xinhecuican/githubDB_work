package 第三章.例3;

public abstract class Animal {
	
	protected Box aBox;
	protected String name;
	
	protected double width,height;   //子类该有的成员变量，父类必须有
	 
	

//	public String getName() {
//		return name;
//	}
//
//	public void setName(String name) {
//		this.name = name;
//	}
	public void hhh(){
		System.out.println("hhh");
	}

	
	

		public Box getaBox() {
			return aBox;
		}

		public void setaBox(Box aBox) {
			this.aBox = aBox;
		}

		

		public void setWidth(double width) {
			this.width = width;
		}

		

		public void setHeight(double height) {
			this.height = height;
		}
		
		public double getWidth() {
			return width;
		}
		
		public double getHeight() {
			return height;
		}

		public Animal(String name) {
			super();
			this.name = name;
		}
		public abstract void enter();  //抽象类中的方法最好是抽象方法，没有（）包围的方法体
        //目的是适应千变万化的子类的enter（）。子类的enter（）
        //除了不是abstract，方法体内容不同外，其他定义和父类的enter（）相同
	
		
}
