package ������.��4;

//import JFrame;
import javax.swing.*;
import java.awt.Color;
import java.awt.GridLayout;


public class MyGridLayout extends JFrame {

	public MyGridLayout(){				  //��Զ�Ĺ��췽��
		
		super("�߲���ʵ��");			     //��Զ��super("")
		this.setBounds(100,100,300,200);  //���Ͻ�����,��*��
		
		JButton jb1 = new JButton("button1");
		JButton jb2 = new JButton("button2");
		JButton jb3 = new JButton("button3");
		JButton jb4 = new JButton("button4");
		
		this.setLayout(new GridLayout(3,1));	//3��1��
		
		this.add(jb1);				//Ĭ�ϰ�button1 ���ڵ�һ��
		JPanel jp = new JPanel();   //JPanel Ҳ��һ���������� ��JFranme�����������
									//��JPanel������������� ֻ�ܷ��ڱ���������
									//JFrame Ĭ�ϲ���BorderLayout ��JPanl��Ĭ�ϲ�����FlowLayout
		
		this.add(jp);
		
		
		jp.add(jb3);
		jp.add(jb4);
		this.add(new JButton("button5"),"Center");
		
		this.setBackground(Color.BLUE);               //��Զ���� 
		this.setDefaultCloseOperation(EXIT_ON_CLOSE); //������ �˳�
		this.setVisible(true);						  //��Զ����
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new MyGridLayout();
	}

}
