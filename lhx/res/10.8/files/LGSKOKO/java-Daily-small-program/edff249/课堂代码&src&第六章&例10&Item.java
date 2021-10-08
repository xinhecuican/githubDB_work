package ������.��10;     //��ҵ�����������Ϊ�̶�����
import javax.swing.*;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

import java.awt.FlowLayout;
import java.awt.event.ActionEvent;//awt����ֻ����������� ��swing�е���� ���ǲ��ֹ����� �¼���������
import java.awt.event.ActionListener;//������� �з�Ӧ ActionListener �� Button һ����¼���Ӧ�ӿ�
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
									//������һ��actionPerformed���� ʵ��ActionListener���� ������д��
									//JFrame implements ActionListener ������д actionPerformed
//�ַ�������Ҳ��Object����
public class Item extends JFrame implements ActionListener{

	JComboBox comboBox_channel;
	JList list_shows;
	JLabel label;
	Object []channel ={"����һ̨","�����̨"};
	Object [][]shows ={{"��������","�����̸"},{"�����ռ�","�����뷨","���ð�Сʱ"}};
	
	public Item(){
		super("�б�����¼�ʾ��");
		
		this.setBounds(100, 100, 300, 200);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setLayout(new FlowLayout());
		comboBox_channel = new JComboBox(channel);
		this.add(comboBox_channel);
		list_shows = new JList(shows[0]);
		this.add(list_shows);
		
		label = new JLabel("");
		this.add(label);
		
		comboBox_channel.addItemListener(new ItemListener(){//�����ڲ���
			
			public void itemStateChanged(ItemEvent e){//������
				
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
				label.setText("��ѡ�е��ǣ�"+str);
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
