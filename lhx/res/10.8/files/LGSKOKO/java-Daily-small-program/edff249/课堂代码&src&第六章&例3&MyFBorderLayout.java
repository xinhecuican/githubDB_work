package 第六章.例3;

//import JFrame;
import javax.swing.*;
import java.awt.Color;


public class MyFBorderLayout extends JFrame {

	public MyFBorderLayout(){				  //永远的构造方法
		
		super("边布局实例");			     //永远的super("")
		this.setBounds(100,100,300,200);  //左上角坐标,宽*高
		
		JButton jb1 = new JButton("button1");
		JButton jb2 = new JButton("button2");
		JButton jb3 = new JButton("button3");
		JButton jb4 = new JButton("button4");
		
		//this.setLayout(new FlowLayout());	//FlowLayout() 和Color 都是在awt中
											//！！！JFrame默认是BorderLayout 布局,边布局
											//如果没有本句 只能输出button4
											//设置流布局后 可以看到从左往右流动摆放
											//new FlowLayout()创建流布局对象
											//虚拟机自动安排位置
		
		this.add(jb1,"North");				//北南占据全部的北部 南部  而东西不是顶天立地
		this.add(jb2,"South");
		this.add(jb3,"West");
		this.add(jb4,"East");
		this.add(new JButton("button5"),"Center");
		
		this.setBackground(Color.BLUE);               //永远存在 
		this.setDefaultCloseOperation(EXIT_ON_CLOSE); //点击叉号 退出
		this.setVisible(true);						  //永远存在
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new MyFBorderLayout();
	}

}
