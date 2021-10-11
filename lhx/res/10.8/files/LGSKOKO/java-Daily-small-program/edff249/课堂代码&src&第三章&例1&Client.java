package 第三章.例1; //作业：电脑Computer，投影仪Projector，屏幕screen，Action，Client，
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
		Action aAction;
		Elephant taiguoxiang;
		IceBox xinfeibingxiang;
		Person lurenjia;
		
		                    
	    aAction = new Action();
	    //场景一：泰国大象，路人甲，新飞冰箱
	    taiguoxiang = new Elephant("泰国象");  //new表明大象已经牵过来，在内存中已给分配空间，默认值null已有
	                                     //如果没有带参的构造方法，java默认给无参的构造方法，Elephant（）
	                                     //之前我们并没有定义，也没有出错。但一旦定义了带参构造函数，系统不再
	                                     //默认给我们无参构造函数，此处构造方法再无参就会出错
	    xinfeibingxiang = new IceBox("新飞冰箱");      //冰箱已放好
	    lurenjia = new Person("路人甲");      //拉冰箱门的人已做好准备
	                                //以上都是现实中，或在内存中已存在的活生生的对象，但和剧本中的对象没有关联
	                                //Client类之外的类都是剧本，蓝图，规划图，计划书，抽象的，服务器类
		                            //Client类中目前的所有成员变量和Action中的虽然同名的成员变量不是一回事
	                                //谁建立Client类中成员变量和Action类中成员变量之间的关系
	                                //哪个类拥有这些成员变量，他的对象就调用set方法
     	 
	aAction.setaElephant(taiguoxiang)	;//双击选中setaElephant(),再右击，open declaration
	                                 //程序自动转到Action类中本方法的定义
	aAction.setaIceBox(xinfeibingxiang);
	aAction.setaPerson(lurenjia);
	
	taiguoxiang.setaIceBox(xinfeibingxiang);
	
	taiguoxiang.setWidth(1.0);
	taiguoxiang.setHeight(1.8);
	xinfeibingxiang.setHeight(2.0);
	xinfeibingxiang.setWidth(1.5);
	aAction.action();
	
	}                        
	
}
