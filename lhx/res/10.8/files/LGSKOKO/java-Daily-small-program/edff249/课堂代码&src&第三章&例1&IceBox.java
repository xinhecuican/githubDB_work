package ������.��1;

public class IceBox {
	
	 double width,height;//private:ֻ���ڱ���ķ�������ʹ��,û�����Σ���Ĭ�����ͣ�Ϊ���������п���
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
		System.out.println("�����Ŵ�");
	}
	
	public void close(){
		System.out.println("�����Źر�");
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
}
