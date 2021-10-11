package 第三章.例4;

public class Cage extends Box {
	
	public  Cage(String name) {    //父类中有的构造方法，子类也要有
		super(name);             //super就是Animal的意思
		
	}


	public void open() {
		System.out.println(this.name+"门打开");

	}

	public void close() {
		System.out.println(this.name+"门关闭");

	}

}
