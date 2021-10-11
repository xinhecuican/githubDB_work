package 第四章.例1; //输入月份，判断其属于的季节

public class Elself {

	private int month;      //输入的是可变的，可变的输入要有set/get方法，自变量才set、get
	private String season;  // season是需要获得的变量，不是设置或传参的变量，不用set/get方法
                           //因变量不能设置set/get 
	
	public void setMonth(int month) { //什么时候用set不用构造方法或其他方法传参
		this.month = month;           //set中只有this.**=**; 因为自动生成
	}                                 //当参数有多种情形需要判断时，用其他方法传参
                                      //一般统计对象个数的static变量放在构造方法中，其他稍微复杂的情形
	                                  //不放在构造中，因为构造方法有父类各个层级的连续调用，造成绑定
	                                  //直接赋值只适用于局部变量，成员变量不能直接赋值。
	                                  //如果成员变量是直接赋值，则必须是public的。黑客也可以编一个类在他的
	                                  //类中直接改你这个public的变量。 
	
	public int getMonth() {          
		return month;
	}

	public void judegeSeason(){                     //可不可以带month的参数，如果是，就不用set
		if(month == 12 || month ==1 || month == 2)  //注意==与=的区别，以及|和||的区别
			season = "Winter"; 
		else if (month == 3 || month ==4 || month == 5) //为什么else后面加一个if，else是否之前所有
			season = "Spring";                          //if和else 表示两种情形
		else if (month == 6 || month ==7 || month == 8) //if else if else 多种情形，最通用情形
			season = "Summer";                          //永远在最后加一个else，给程序一个例外出口
		                                                //if 之后只有一条语句，可以不加{}
		                                                //所有的if else if  else是一个整体，
		                                                //在season = "Spring"之后的语句如果不添加}
		                                                //就相当于之前if else if的整个出口，
		                                                //之后的else if 会出错
		else if (month == 9 || month ==10 || month == 11)
			season = "Autumn";
		else{
			season = "no season!";
		}
		System.out.println("month" + this.month + "belong to " + season);
		                             //this.month可以改为this.getMonth()
		                             //如果都用if任何，则最后的if是前面所有if的否

	}
}
