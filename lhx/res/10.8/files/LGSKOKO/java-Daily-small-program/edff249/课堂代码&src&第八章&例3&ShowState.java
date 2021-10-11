package 第八章.例3;

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
		
		super("演示线程状态");
		this.setSize(450, 300);
		this.setLocation(200,200);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		textArea = new JTextArea();
		textArea.setAutoscrolls(true);
		this.add(textArea);
		
		button_start = new JButton("启动");
		button_start.addActionListener(this);
		
		button_interrupt = new JButton("中断");
		button_interrupt.addActionListener(this);
		
		button_terminate = new JButton("线程结束后");
		button_terminate.addActionListener(this);
		
		button_terminate.setEnabled(false);       //虚的，点击没有反应
		button_interrupt.setEnabled(false);
	
		t = new Thread(this);               
		                                     //为什么生成线程对象在本方法而不在其他方法？ 随着图形界面一起生成
		                                     //本类对象this没有继承Thread，通过披上线程
		                                    //对象的外衣，创建了新的线程对象t
		label = new JLabel("线程状态");
		textField_state = new JTextField(""+t.getState(),10);
		textField_state.setEditable(false);    //文本行不能编辑，和37行的setEnabled（false）区别
		
		JPanel panel = new JPanel();
		panel.setLayout(new FlowLayout(0));  //对应LEFT，1=center，2=right，3=容器开始方向，left 4=容器结束方向 right
		                                       //0 是左对齐
		panel.add(button_start);
		panel.add(button_interrupt);
		panel.add(button_terminate);
		panel.add(label);
		panel.add(textField_state);
		
		this.add(panel,BorderLayout.SOUTH);     //否则，BorderLayout是默认居中
		this.setVisible(true);
	}
	
	

	public void actionPerformed(ActionEvent e) { //要区分事件响应和线程运行图形元素“动”的区别
		

		if(e.getSource()==button_start){
			
			t = new Thread(this);       //线程中断以后，死亡，如果在点击“启动”，没有该句，就没有反应
			t.start();
			textField_state.setText(" "+t.getState());
			button_start.setEnabled(false);
			button_interrupt.setEnabled(true);
			
		}
		
		if(e.getSource()==button_interrupt){ //非线程体run（）中，能中断线程吗，与线程体run中的break的联系
			
			t.interrupt();                   //不在run（）中，不是真正的中断。真正中断，需要两个步骤：1、事件响应
			                                 //2、在run（）中真正中断。
			                                 //interrupt暗送秋波，跟start与run暗送秋波一样。
			textField_state.setText(" "+t.getState());
			button_start.setEnabled(true);
			button_terminate.setEnabled(true);
			button_interrupt.setEnabled(false);
		}
		if(e.getSource()==button_terminate){
			
			textField_state.setText(" "+t.getState());
		}
	}
	  public void run() {              //线程中的内容是我们想要演示线程，或通过线程解决问题的内容
	                                   //其他事件响应不放在线程中。
    	int i=1;
    	while(t.isAlive()&&!t.isInterrupted()){
    		
    		String str = "a";
    		if(i%20==0)
    			str+="\n";
    		i++;
    		textArea.append(str);   //没有线程时，在actionPerformed方法中，但如果想线程运作，
    		                        //就要提到run方法中
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
