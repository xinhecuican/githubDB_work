package ������.��5; //��ҵ��1������5���� �ñ�ǩ���ұߵ��ı��еȶ���  2����ͼ6-3


import javax.swing.*;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.GridLayout;


public class TextComponents extends JFrame {

	public TextComponents(){				  //��Զ�Ĺ��췽��
		
		super("�ı��к��ı���ʾ��");			     //��Զ��super("")
		this.setBounds(100,100,400,400);  //���Ͻ�����,��*��
		
		
		
		JPanel jp1 = new JPanel();
		this.add(jp1);
		
		this.setLayout(new FlowLayout(FlowLayout.RIGHT));	//�Ҷ���
		jp1.add(new JLabel("user"));                       //�û���
		jp1.add(new JTextField(20));
		
		JPanel jp2 = new JPanel();
		this.add(jp2);
		
		jp2.add(new JLabel("password"));					//����
		jp2.add(new JPasswordField(20));
		
		
		JPanel jp3 = new JPanel();
		this.add(jp3);
		jp3.add(new JLabel("description"));
		jp3.add(new JTextArea("my function",5,20));
		
		
		this.setBackground(Color.BLUE);               //��Զ���� 
		this.setDefaultCloseOperation(EXIT_ON_CLOSE); //������ �˳�
		this.setVisible(true);						  //��Զ����
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new TextComponents();
	}

}
