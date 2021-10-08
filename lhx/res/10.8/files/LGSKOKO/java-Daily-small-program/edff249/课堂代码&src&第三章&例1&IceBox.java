package 第三章.例1;

public class IceBox {
	
	 double width,height;//private:只能在本类的方法当中使用,没有修饰，即默认类型，为本包的类中可用
	 private String name;
	public IceBox(String name) {
		super();
		this.name = name;
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

	public void open(){
		System.out.println("冰箱门打开");
	}
	
	public void close(){
		System.out.println("冰箱门关闭");
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
}
