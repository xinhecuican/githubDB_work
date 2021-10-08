package 第六章.例1;

//import JFrame;
import javax.swing.JFrame;

import java.awt.Color;


public class MyJFrame extends JFrame {

	public MyJFrame(){
		super("框架实例");
		this.setBounds(100,100,400,400);  //左上角坐标,宽*高
		this.getContentPane().setBackground(Color.RED);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE); //点击叉号 退出
		this.setVisible(true);			
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		new MyJFrame();

	}

}
