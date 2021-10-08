package 第六章.例10;     //作业：将本例题改为固定布局
import javax.swing.*;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

import java.awt.FlowLayout;
import java.awt.event.ActionEvent;//awt包中只是组件不用了 用swing中的组件 但是布局管理器 事件还是在用
import java.awt.event.ActionListener;//单击组件 有反应 ActionListener 是 Button 一类的事件响应接口
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
									//里面有一个actionPerformed方法 实现ActionListener的类 必须重写它
									//JFrame implements ActionListener 必须重写 actionPerformed
//字符串类型也是Object类型
public class Item extends JFrame implements ActionListener{

	JComboBox comboBox_channel;
	JList list_shows;
	JLabel label;
	Object []channel ={"中央一台","中央二台"};
	Object [][]shows ={{"新闻联播","焦点访谈"},{"交换空间","经济与法","经济半小时"}};
	
	public Item(){
		super("列表组件事件示例");
		
		this.setBounds(100, 100, 300, 200);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setLayout(new FlowLayout());
		comboBox_channel = new JComboBox(channel);
		this.add(comboBox_channel);
		list_shows = new JList(shows[0]);
		this.add(list_shows);
		
		label = new JLabel("");
		this.add(label);
		
		comboBox_channel.addItemListener(new ItemListener(){//匿名内部类
			
			public void itemStateChanged(ItemEvent e){//类似于
				
				int i = comboBox_channel.getSelectedIndex();
				
				list_shows.setListData(shows[i]);
			}
		});
		
		list_shows.addListSelectionListener(new ListSelectionListener(){
			
			public void valueChanged(ListSelectionEvent e){
				
				String str = comboBox_channel.getSelectedItem().toString();
				if(!list_shows.isSelectionEmpty()){
					str = " "+list_shows.getSelectedValue();
				}
				label.setText("你选中的是："+str);
			}

			
	 });
	
	this.setVisible(true);
		
	}
	
	public void actionPerformed(ActionEvent arg0)
	{
		
	}
	
	public static void main(String[] args)
	{
		new Item();
	}
	
}
