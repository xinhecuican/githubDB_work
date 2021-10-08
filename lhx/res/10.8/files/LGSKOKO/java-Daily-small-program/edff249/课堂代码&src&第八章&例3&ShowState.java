package �ڰ���.��3;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;;

public class ShowState extends JFrame implements ActionListener, Runnable {

	JTextArea textArea;
	JButton button_start,button_interrupt,button_terminate;
	JTextField textField_state;
	JLabel label;
	Thread t;
	
	public ShowState(){
		
		super("��ʾ�߳�״̬");
		this.setSize(450, 300);
		this.setLocation(200,200);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		textArea = new JTextArea();
		textArea.setAutoscrolls(true);
		this.add(textArea);
		
		button_start = new JButton("����");
		button_start.addActionListener(this);
		
		button_interrupt = new JButton("�ж�");
		button_interrupt.addActionListener(this);
		
		button_terminate = new JButton("�߳̽�����");
		button_terminate.addActionListener(this);
		
		button_terminate.setEnabled(false);       //��ģ����û�з�Ӧ
		button_interrupt.setEnabled(false);
	
		t = new Thread(this);               
		                                     //Ϊʲô�����̶߳����ڱ��������������������� ����ͼ�ν���һ������
		                                     //�������thisû�м̳�Thread��ͨ�������߳�
		                                    //��������£��������µ��̶߳���t
		label = new JLabel("�߳�״̬");
		textField_state = new JTextField(""+t.getState(),10);
		textField_state.setEditable(false);    //�ı��в��ܱ༭����37�е�setEnabled��false������
		
		JPanel panel = new JPanel();
		panel.setLayout(new FlowLayout(0));  //��ӦLEFT��1=center��2=right��3=������ʼ����left 4=������������ right
		                                       //0 �������
		panel.add(button_start);
		panel.add(button_interrupt);
		panel.add(button_terminate);
		panel.add(label);
		panel.add(textField_state);
		
		this.add(panel,BorderLayout.SOUTH);     //����BorderLayout��Ĭ�Ͼ���
		this.setVisible(true);
	}
	
	

	public void actionPerformed(ActionEvent e) { //Ҫ�����¼���Ӧ���߳�����ͼ��Ԫ�ء�����������
		

		if(e.getSource()==button_start){
			
			t = new Thread(this);       //�߳��ж��Ժ�����������ڵ������������û�иþ䣬��û�з�Ӧ
			t.start();
			textField_state.setText(" "+t.getState());
			button_start.setEnabled(false);
			button_interrupt.setEnabled(true);
			
		}
		
		if(e.getSource()==button_interrupt){ //���߳���run�����У����ж��߳������߳���run�е�break����ϵ
			
			t.interrupt();                   //����run�����У������������жϡ������жϣ���Ҫ�������裺1���¼���Ӧ
			                                 //2����run�����������жϡ�
			                                 //interrupt�����ﲨ����start��run�����ﲨһ����
			textField_state.setText(" "+t.getState());
			button_start.setEnabled(true);
			button_terminate.setEnabled(true);
			button_interrupt.setEnabled(false);
		}
		if(e.getSource()==button_terminate){
			
			textField_state.setText(" "+t.getState());
		}
	}
	  public void run() {              //�߳��е�������������Ҫ��ʾ�̣߳���ͨ���߳̽�����������
	                                   //�����¼���Ӧ�������߳��С�
    	int i=1;
    	while(t.isAlive()&&!t.isInterrupted()){
    		
    		String str = "a";
    		if(i%20==0)
    			str+="\n";
    		i++;
    		textArea.append(str);   //û���߳�ʱ����actionPerformed�����У���������߳�������
    		                        //��Ҫ�ᵽrun������
    		try{
    			
    			t.sleep(100);      //interrupt--try\sleep--catch--break
    		}catch(InterruptedException e){
    			break;
    		}
    	}
	}

	public static void main(String[] args) {
		
		new ShowState();
	}

}
