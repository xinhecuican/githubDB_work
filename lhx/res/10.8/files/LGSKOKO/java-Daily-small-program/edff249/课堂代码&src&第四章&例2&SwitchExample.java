package 第四章.例2;

public class SwitchExample { //给一个分数，判断其属于哪个等级。

	private int grade;

	 
	public void setGrade(int grade) {
		this.grade = grade;
	}
	
	public int getGrade() {
		return grade;
	}

	public void grade(){
		switch(grade/10)  //if的变种，if适用于后面括号中的结果是不确定的情形，switch适用于确定情形，而且整数
		                  //一般用于少量几种情形，带小数点的，不适合，无限的不适合，char类型也可
		                  //char表明看上去是字符，实际在底层是用整数表达
		                  //注意switch是语句，一定要放在方法中
		{
		case 6: System.out.println(this.getGrade()+"分属于及格");
		                                         //switch与case成对出现，冒号的作用
		                                         //每个case后要用break；否则两个case适用一种后续逻辑
		break;
		case 7:
		case 8: System.out.println(this.getGrade()+"分属于良好");
		break;
		case 9: System.out.println(this.getGrade()+"分属于优秀");
		break;
		case 10: System.out.println(this.getGrade()+"分属于满分");
		break;
		default:  System.out.println(this.getGrade()+"分属于不及格");//相当于if中最后一个else，出口
		                                                         //因为是出口，不和前面任一case并行
		break;
		}
			
	}
	
}
