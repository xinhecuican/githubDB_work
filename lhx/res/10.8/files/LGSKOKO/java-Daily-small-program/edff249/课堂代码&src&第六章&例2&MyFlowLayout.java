package ������.��2;

//import JFrame;
import javax.swing.*;
import java.awt.Color;
import java.awt.FlowLayout;


public class MyFlowLayout extends JFrame {

	public MyFlowLayout(){				  //��Զ�Ĺ��췽��
		
		super("������ʵ��");			     //��Զ��super("")
		this.setBounds(100,100,300,200);  //���Ͻ�����,��*��
		
		JButton jb1 = new JButton("button1");
		JButton jb2 = new JButton("button2");
		JButton jb3 = new JButton("button3");
		JButton jb4 = new JButton("button4");
		
		this.setLayout(new FlowLayout());	//FlowLayout() ��Color ������awt��
											//JFrameĬ����BorderLayout ����,�߲���
											//���û�б��� ֻ�����button4
											//���������ֺ� ���Կ����������������ڷ�
											//new FlowLayout()���������ֶ���
											//������Զ�����λ��
		
		this.add(jb1);
		this.add(jb2);
		this.add(jb3);
		this.add(jb4);
		
		this.getContentPane().setBackground(Color.BLUE);               //��Զ���� 
		this.setDefaultCloseOperation(EXIT_ON_CLOSE); //������ �˳�
		this.setVisible(true);						  //��Զ����
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new MyFlowLayout();
	}

}
