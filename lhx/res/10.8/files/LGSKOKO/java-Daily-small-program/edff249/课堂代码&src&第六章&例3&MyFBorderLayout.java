package ������.��3;

//import JFrame;
import javax.swing.*;
import java.awt.Color;


public class MyFBorderLayout extends JFrame {

	public MyFBorderLayout(){				  //��Զ�Ĺ��췽��
		
		super("�߲���ʵ��");			     //��Զ��super("")
		this.setBounds(100,100,300,200);  //���Ͻ�����,��*��
		
		JButton jb1 = new JButton("button1");
		JButton jb2 = new JButton("button2");
		JButton jb3 = new JButton("button3");
		JButton jb4 = new JButton("button4");
		
		//this.setLayout(new FlowLayout());	//FlowLayout() ��Color ������awt��
											//������JFrameĬ����BorderLayout ����,�߲���
											//���û�б��� ֻ�����button4
											//���������ֺ� ���Կ����������������ڷ�
											//new FlowLayout()���������ֶ���
											//������Զ�����λ��
		
		this.add(jb1,"North");				//����ռ��ȫ���ı��� �ϲ�  ���������Ƕ�������
		this.add(jb2,"South");
		this.add(jb3,"West");
		this.add(jb4,"East");
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
		new MyFBorderLayout();
	}

}
