package 第六章.例14;			//！！！！！！！经常上机考试

import java.awt.event.*;
import javax.swing.*;

public class WindowRectangle extends JFrame implements ActionListener {

	
	JTextField tf_width,tf_length;	//在两个方法中用到
	JButton btn_area;
	JTextArea text;
	Rectangle rectangle;
	
	public WindowRectangle()         //构造方法用于静态图示
	{
		rectangle = new Rectangle();
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		JPanel p = new JPanel();
		this.add(p,"North");
		
		p.add(new JLabel("长度"));
		tf_length = new JTextField(5);
		p.add(tf_length);
		
		p.add(new JLabel("宽度"));
		tf_width = new JTextField(5);
		p.add(tf_width);
		
		btn_area = new JButton("计算面积");
		btn_area.addActionListener(this);
		p.add(btn_area);
		
		text = new JTextArea(5,20);
		this.add(text);
		
		this.setVisible(true);
		
	}
	
	public void actionPerformed(ActionEvent arg0)  //用于响应
	{
		try{
			int length = Integer.parseInt(tf_length.getText());
			int width = Integer.parseInt(tf_width.getText());
			rectangle.setLength(length);
			rectangle.setWidth(width);
			
			if(rectangle.isSquare())
				text.append("正方形的边长"+length+",面积"+rectangle.area()+"\n");
			else
				text.append("长方形的边长："+length+",宽"+width+",面积"+rectangle.area());
		}catch(Exception e){
			
			text.append("无法计算面积："+e.toString()+"\n");
		}
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
