package 第三章.例4;

public class Cat extends Animal{ 

	private static int num;
	public Cat(String name) {     //父类中有的构造方法，子类也要有
		super(name);             //super就是Animal的意思
		num++;
	}

	//private double width;  //默认创建的是int 类型，改为double类型
	//private double height;
    //private IceBox aIceBox; //默认创建的是Object类型，要改为IceBox类型
    //private String name;
    
	
	
	
	public void enter(){//把鼠标放在红色波浪线上，显示Create field "width",
		
		 if((width<aBox.width)&&(height<aBox.height))
		 
			System.out.println(this.name+"悄无声息的进入");
		    System.out.println(this.width);
	        System.out.println(this.height);
	        
	        System.out.println(aBox.width); 
	        System.out.println(aBox.height);
	        System.out.println("猫"+num+"只");
	}
}
