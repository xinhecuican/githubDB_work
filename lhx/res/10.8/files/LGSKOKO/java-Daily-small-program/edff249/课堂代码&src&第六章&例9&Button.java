package ������.��9;     //��ҵ�����������Ϊ�̶�����
import javax.swing.*;
import java.awt.event.ActionEvent;//awt����ֻ����������� ��swing�е���� ���ǲ��ֹ����� �¼���������
import java.awt.event.ActionListener;//������� �з�Ӧ ActionListener �� Button һ����¼���Ӧ�ӿ�
									//������һ��actionPerformed���� ʵ��ActionListener���� ������д��
									//JFrame implements ActionListener ������д actionPerformed

public class Button extends JFrame implements ActionListener{

	JLabel labelName;
	JLabel labelSex;
	JTextArea textArea;
	JButton btn_ok;
	JTextField text_name;
	JRadioButton rb[];
	JCheckBox cb[];
	String str = "";
	
	public Button(){
		super("��ť����¼�ʾ��");
		String []sex ={"male","female"};
		String []hobbies ={"sport","music"};
		this.setBounds(100, 100, 300, 200);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		textArea = new JTextArea(5,10);
		this.add(textArea,"West");
		JPanel panel = new JPanel();
		this.add(panel);
		
		 labelName = new JLabel("name:");
		panel.add(new JLabel("name"));
		text_name = new JTextField(12);
		panel.add(text_name);
		
		 labelSex = new JLabel("sex:");
		panel.add(new JLabel("sex:"));
		ButtonGroup bg =new ButtonGroup();  //��ѡ��ť�� ֻ��ѡһ�� �����ŵ�һ������
		rb = new JRadioButton[sex.length]; //������������ɵ�����,��35�е�����
											//��sec[]���� ����JRadioButton����
		for(int i=0; i<sex.length;i++){
			rb[i] = new JRadioButton(sex[i]);//sex[]�����е�Ԫ�طŵ�JRadioButton[]������
											//����Ҫ��"male" "female"�ŵ�һ����,bg
											//�ѵ���ѡ��ť��ӵ�panel��,ע�ⲻ��add(bg)
											//������ӵ�panel�У�������ӵ�ѡ��ť�� �����ÿ����ѡ��ť
			bg.add(rb[i]);
			panel.add(rb[i]);
			
		}
		panel.add(new JLabel("hobbies"));
		cb = new JCheckBox[hobbies.length];   //ͨ��hobbies[]����CheckBox[]
		for(int i=0;i<hobbies.length;i++){
			cb[i] = new JCheckBox(hobbies[i]);
			panel.add(cb[i]);
		}
		
		btn_ok = new JButton("ok");
		btn_ok.addActionListener(this); //����¼��ӿ�
		panel.add(btn_ok);
		this.setVisible(true);
		
		
	}
	
	
	public void actionPerformed(ActionEvent e){
		
		if(e.getSource()==btn_ok){       					//getSource()��ȡ�¼�Դ
			str+= labelName.getText()+"\n"+text_name.getText()+"\n"+ labelSex.getText(); //��ȡ�ı�����������ı�
			for(int i=0;i<rb.length;i++){
				if(rb[i].isSelected()){//isSelected ����������Ҫ��
					
					str+= rb[i].getText();
				}
			}
			str +="\n hobbies:";
			for(int i=0;i<cb.length;i++){
				if(cb[i].isSelected()) str +="\n"+ cb[i].getText();
			}
			textArea.append(str);			//append(str)���ı����������Ҫ��ʾ���ַ���
		}									//ѡ��btn_ok��ִ�е����ݵ��˲Ž����������۵�ѡ��ѡ��ť�Ļ�ȡ
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		new Button();
	}
	
}
