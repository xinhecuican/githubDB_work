package 第六章.例14;

public class Rectangle { //实体类 model类 MVC中的m
	
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
