package 第三章.例4;

public class Person implements Openning,Closing{  // 人的属性变量与大象进冰箱没有关系，所以不定义成员变量，只定义成员方法

	private String name;
	
	
	public Person(String name) {
	super();
	this.name = name;
}
	
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}


public void controlClose() {
	System.out.println("关闭");
}

public void controlOpen() {
	System.out.println(this.name+"打开");
	
}
}
