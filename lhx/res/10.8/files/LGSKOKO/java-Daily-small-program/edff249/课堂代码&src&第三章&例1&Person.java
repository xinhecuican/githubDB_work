package 第三章.例1;

public class Person {  // 人的属性变量与大象进冰箱没有关系，所以不定义成员变量，只定义成员方法

	private String name;
	
	
	public Person(String name) {
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

	public void pull() { //平常我们说人开门关门，那么开门和关门定义在冰箱还是人的类中？
		//原则：开门关门用到的尺寸属于哪个类，就定义在那个类中。这里属于冰箱。所以，开门关门的方法定义在冰箱中，而不是人这个类中。
		//再比如，购物车中买两只钢笔，钢笔的数量可以+1，但是钢笔的种类不能+1，compareID（）方法必须放在货物这个类中，
		//public class Goods{public void compareID（String ID）{if（this.ID==ID）}}
        //而不是购物车这个类中。因为货物中有ID号。成员变量和成员方法是一对孪生兄弟，同时属于一个类
		//因为方法是处理变量的。方法属于A类，成员变量属于B类，无法操作。
		System.out.println(this.name+"拉门");

	}
public void push(){
	
	System.out.println(this.name+"推门");
}
}
