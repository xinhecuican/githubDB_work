package ������.��14;

public class Rectangle { //ʵ���� model�� MVC�е�m
	
	private int length;
	private int width;
	public Rectangle()
	{
		
	}
	
	
	public int getLength() {
		return length;
	}
	public void setLength(int length) {
		this.length = length;
	}
	public int getWidth() {
		return width;
	}
	public void setWidth(int width) {
		this.width = width;
	}
	
	public boolean isSquare(){
		
		return (width==length?true:false);
	}
	
	public int area(){
		
		return width*length;
	}

}
