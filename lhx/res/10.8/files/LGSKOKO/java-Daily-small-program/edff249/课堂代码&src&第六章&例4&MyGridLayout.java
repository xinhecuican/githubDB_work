package 第六章.例4;

//import JFrame;
import javax.swing.*;
import java.awt.Color;
import java.awt.GridLayout;


public class MyGridLayout extends JFrame {

	public MyGridLayout(){				  //永远的构造方法
		
		super("边布局实例");			     //永远的super("")
		this.setBounds(100,100,300,200);  //左上角坐标,宽*高
		
		JButton jb1 = new JButton("button1");
		JButton jb2 = new JButton("button2");
		JButton jb3 = new JButton("button3");
		JButton jb4 = new JButton("button4");
		
		this.setLayout(new GridLayout(3,1));	//3行1列
		
		this.add(jb1);				//默认把button1 放在第一行
		JPanel jp = new JPanel();   //JPanel 也是一个矩形容器 但JFranme是最外层容器
									//而JPanel不是最外层容器 只能放在别的容器里边
									//JFrame 默认布局BorderLayout 而JPanl的默认布局是FlowLayout
		
		this.add(jp);
		
		
		jp.add(jb3);
		jp.add(jb4);
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
		new MyGridLayout();
	}

}
