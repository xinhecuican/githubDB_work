package ������.��14;			//�������������������ϻ�����

import java.awt.event.*;
import javax.swing.*;

public class WindowRectangle extends JFrame implements ActionListener {

	
	JTextField tf_width,tf_length;	//�������������õ�
	JButton btn_area;
	JTextArea text;
	Rectangle rectangle;
	
	public WindowRectangle()         //���췽�����ھ�̬ͼʾ
	{
		rectangle = new Rectangle();
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		JPanel p = new JPanel();
		this.add(p,"North");
		
		p.add(new JLabel("����"));
		tf_length = new JTextField(5);
		p.add(tf_length);
		
		p.add(new JLabel("���"));
		tf_width = new JTextField(5);
		p.add(tf_width);
		
		btn_area = new JButton("�������");
		btn_area.addActionListener(this);
		p.add(btn_area);
		
		text = new JTextArea(5,20);
		this.add(text);
		
		this.setVisible(true);
		
	}
	
	public void actionPerformed(ActionEvent arg0)  //������Ӧ
	{
		try{
			int length = Integer.parseInt(tf_length.getText());
			int width = Integer.parseInt(tf_width.getText());
			rectangle.setLength(length);
			rectangle.setWidth(width);
			
			if(rectangle.isSquare())
				text.append("�����εı߳�"+length+",���"+rectangle.area()+"\n");
			else
				text.append("�����εı߳���"+length+",��"+width+",���"+rectangle.area());
		}catch(Exception e){
			
			text.append("�޷����������"+e.toString()+"\n");
		}
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
