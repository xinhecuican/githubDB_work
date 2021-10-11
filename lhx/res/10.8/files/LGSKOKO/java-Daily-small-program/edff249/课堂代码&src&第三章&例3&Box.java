package ตฺศýีย.ภý3;

public abstract class Box {


	 protected double width,height;
	 protected String name;
	 
	 

	
	public Box(String name) {
		super();
		
		this.name = name;
	}

//	public String getName() {
//		return name;
//	}
//
//	public void setName(String name) {
//		this.name = name;
//	}

	

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
   public abstract void open();
	
	public abstract void close();
		
}
