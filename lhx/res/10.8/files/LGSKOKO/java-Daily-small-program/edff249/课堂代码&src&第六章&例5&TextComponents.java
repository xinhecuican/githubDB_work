package 第六章.例5; //作业：1、改例5布局 让标签和右边的文本行等对齐  2、做图6-3


import javax.swing.*;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.GridLayout;


public class TextComponents extends JFrame {

	public TextComponents(){				  //永远的构造方法
		
		super("文本行和文本区示例");			     //永远的super("")
		this.setBounds(100,100,400,400);  //左上角坐标,宽*高
		
		
		
		JPanel jp1 = new JPanel();
		this.add(jp1);
		
		this.setLayout(new FlowLayout(FlowLayout.RIGHT));	//右对齐
		jp1.add(new JLabel("user"));                       //用户名
		jp1.add(new JTextField(20));
		
		JPanel jp2 = new JPanel();
		this.add(jp2);
		
		jp2.add(new JLabel("password"));					//密码
		jp2.add(new JPasswordField(20));
		
		
		JPanel jp3 = new JPanel();
		this.add(jp3);
		jp3.add(new JLabel("description"));
		jp3.add(new JTextArea("my function",5,20));
		
		
		this.setBackground(Color.BLUE);               //永远存在 
		this.setDefaultCloseOperation(EXIT_ON_CLOSE); //点击叉号 退出
		this.setVisible(true);						  //永远存在
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new TextComponents();
	}

}
