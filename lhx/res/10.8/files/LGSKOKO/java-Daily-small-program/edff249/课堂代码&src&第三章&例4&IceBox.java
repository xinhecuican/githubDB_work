package 第三章.例4;

public class IceBox extends Box{

	
	public IceBox(String name) {
		super(name);
	}
	
 

	
    public void open(){    //覆盖父类中的open（）
		
		System.out.println(this.name+"门打开");
	}
	
	public void close(){
		
		System.out.println(this.name+"门关闭");
	}
}

