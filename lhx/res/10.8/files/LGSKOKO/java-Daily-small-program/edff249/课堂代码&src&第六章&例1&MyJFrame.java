package ������.��1;

//import JFrame;
import javax.swing.JFrame;

import java.awt.Color;


public class MyJFrame extends JFrame {

	public MyJFrame(){
		super("���ʵ��");
		this.setBounds(100,100,400,400);  //���Ͻ�����,��*��
		this.getContentPane().setBackground(Color.RED);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE); //������ �˳�
		this.setVisible(true);			
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		new MyJFrame();

	}

}
