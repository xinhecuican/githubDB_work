package 第六章.例2;

//import JFrame;
import javax.swing.*;
import java.awt.Color;
import java.awt.FlowLayout;


public class MyFlowLayout extends JFrame {

	public MyFlowLayout(){				  //永远的构造方法
		
		super("流布局实例");			     //永远的super("")
		this.setBounds(100,100,300,200);  //左上角坐标,宽*高
		
		JButton jb1 = new JButton("button1");
		JButton jb2 = new JButton("button2");
		JButton jb3 = new JButton("button3");
		JButton jb4 = new JButton("button4");
		
		this.setLayout(new FlowLayout());	//FlowLayout() 和Color 都是在awt中
											//JFrame默认是BorderLayout 布局,边布局
											//如果没有本句 只能输出button4
											//设置流布局后 可以看到从左往右流动摆放
											//new FlowLayout()创建流布局对象
											//虚拟机自动安排位置
		
		this.add(jb1);
		this.add(jb2);
		this.add(jb3);
		this.add(jb4);
		
		this.getContentPane().setBackground(Color.BLUE);               //永远存在 
		this.setDefaultCloseOperation(EXIT_ON_CLOSE); //点击叉号 退出
		this.setVisible(true);						  //永远存在
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new MyFlowLayout();
	}

}
