package 第七章.例2;

public class Elephant {

	private int age;
	
	public void setAge(int i) throws Exception{//throws后面紧接异常类
											   //throws的意思：老娘不管了，本方法不处理异常
											   //处理异常的责任甩给上级方法，即调用该方法的方法
											//throws的位置在方法声明中方法名的后面 {之前
		if(age>0 &&age<150)
			this.age = age;
		else
			throw new Exception("非法年龄数据");	//throw 后面紧接异常对象  Exception是异常类
												//throw的位置在程序中
	}
	
	public static void main(String[] args) throws Exception  {
														//mian方法如果后跟throws，就将异常处理的责任推给虚拟机
														//实际上，所有的throws都是将责任推给虚拟机（JVM)
														//?一般情况下，程序无法处理的异常都推给JVM
														//包括文件找不到，网络连接不上，这些都是程序员在程序中无法处理的
														//凡程序员在程序中能够处理的错误，应该用try{}catch(Exception e){}									
		// TODO Auto-generated method stub
		Elephant aElephant = new Elephant();
		aElephant.setAge(250);
	}

}
