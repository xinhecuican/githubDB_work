package 第二章.例1;

public class Assign {//public的类，类名和文件名必须相同。否则会出错

	public static void assign(){
						//现实中数据是分类型的，所以，反应现实的编程语言也要区分数据类型
						//基本数据类型，非对象类型，是当年java速度慢不得已为之。对象的存储要复杂。
		int x,y;       //变量在方法体内,属于局部变量，必须赋值，出了{}，就不可见了。int：整型 。 注意变量之间的分割用,
		float z=3.214f;{ //声明的同时，赋值，与上面不同.float类型的变量一般不用,赋值时带f。
		double w=3.1415; //double类型的变量常用作小数点类型的变量，赋值时没有d也可以。
						//double类型比float类型精度高，取值范围大。
		boolean t=true; //布尔类型，只有两个值，true和false 没有0和1的对应。
						//w和t在{}中，出了{}二者就不存在了，及变量存在是有界的。
		System.out.println(w+","+t);
		//System.out.println(w+t);//w是可加类型，t是非可加类型，如果像上句那样，中间交”,“,w和t就全转化为字符串了，
								//此时的+，就成为了字付串连接符。即+具有两层含义。加法，字符串之间的连接。
								//“”中的东西，原样输出。两边的变量值转化为字符串后输出。
		}
		char c;         //字符类型一般只在输入输出流，即读写文件时用。
		c= 'a';         //上句声明，本句赋值。
//		int x = 6;      //一个变量不能声明两次，解决方法：把int去掉。
		x = 6;
//		y = 1000；       //中文的分号，导致错误。
		y = 1000;
//		System.out.println("x="+x+","+"y="+y+","+"z="+z+","+"c="+c+","+w+t);
		System.out.println("x="+x+","+"y="+y+","+"z="+z+","+"c="+c);
						//w和t为什么有错，是因为出了{}看不到了，如果在他们自己的{}中输出就没错了。
						//can not be resolved a variable，不认识,也就是定义错误，看不见
						//System.out.println()在console即控制台中输出字符串,为了调试程序用
						//非字符串类型,自动转换为字符串
	}


	public static void main(String[] args) {
		
		Assign.assign();

	}

}
