package 第三章.例3; //作业：电脑Computer，投影仪Projector，屏幕screen，Action，Client，
                  //电脑中成员变量String data，成员方法processData（）
                 //transferData(),投影仪中成员变量data，成员方法receiveData（）和projectData（），
                  //屏幕中的成员变量
                 //同样是data，成员方法是displayData（） 

public class Client {             //给main方法一个单独的类,作为java程序的入口，或客户端，测试
	                              //main方法外不能写代码，只能在main方法中写代码
	                              //main方法的作用之一是给所有成员变量赋值，比如，用户名，密码等

	public static void main(String[] args){  //main+alt+/
		                                     //main方法中具体指定各个实体，变量到底是谁。
		
		                    //main方法先调用过程类Action，过程类调用各个实体类
		Action aAction;       //面向抽象编程,一般的，第一次定义成父类时，被定义成抽象类
	                         //软件发布以后，如果想修改一个具体类，不要修改，要重新创建一个类
		Animal aAnimal;
		Box aBox;
		Person aPerson;       //让这个新类继承原先要被修改的具体类。
		
		aAction = new Action("场景一");
		
	    //场景一：泰国大象，路人甲，新飞冰箱
	    aAnimal = new Elephant("泰国象");  //上转型，子类类型的对象赋给了父亲类型的变量（注意此处是变量）
	                                     //Elephant aElephant = new Elephant();不是上转型
	                                     //Animal aAnimal = new Animal();出错。Animal是抽象类型，
	                                     //不能生成对象。
	                                     //父类类型的变量给赋了子类类型的值（对象）
	                                     //左边是父亲，右边是儿子，左边是父类类型变量
	                                     //右边是子类类型对象
	                                     //多态，父类类型变量可以被赋多个子类的对象
	                                     //aAnimal可以是大象，猫，狗
	    aAnimal.hhh();
	                                     //new表明大象已经牵过来，在内存中已给分配空间，默认值null已有
	                                     //如果没有带参的构造方法，java默认给无参的构造方法，Elephant（）
	                                     //之前我们并没有定义，也没有出错。但一旦定义了带参构造函数，系统不再
	                                     //默认给我们无参构造函数，此处构造方法再无参就会出错
	    aBox = new IceBox("新飞冰箱");    //冰箱已放好
	     
	    aPerson = new Person("路人甲");      //拉冰箱门的人已做好准备
	                                //以上都是现实中，或在内存中已存在的活生生的对象，但和剧本中的对象没有关联
	                                //Client类之外的类都是剧本，蓝图，规划图，计划书，抽象的，服务器类
		                            //Client类中目前的所有成员变量和Action中的虽然同名的成员变量不是一回事
	                                //谁建立Client类中成员变量和Action类中成员变量之间的关系
	                                //哪个类拥有这些成员变量，他的对象就调用set方法
     	 
	aAction.setaAnimal(aAnimal)	;//双击选中setaElephant(),再右击，open declaration
	                                 //程序自动转到Action类中本方法的定义
	aAction.setaBox(aBox);
	aAction.setaPerson(aPerson);
	

	
	aAnimal.setWidth(1.0);
	aAnimal.setHeight(1.8);
	aAnimal.setaBox(aBox);
	aBox.setWidth(1.5);
	aBox.setHeight(2.0);
	aAction.action();
	
	aAction = new Action("场景二");
	aAnimal = new Cat("波斯猫");
	aBox = new Cage("笼子");
	aPerson = new Person("路人乙");
	
	aAction.setaAnimal(aAnimal);
	aAction.setaBox(aBox);
	aAction.setaPerson(aPerson);
	
	aAnimal.setWidth(0.1);
	aAnimal.setHeight(0.4);
	aAnimal.setaBox(aBox);
	aBox.setWidth(0.6);
	aBox.setHeight(0.6);
	aAction.action();
	}                        
	
}
