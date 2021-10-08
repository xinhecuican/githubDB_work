package 第六章.例9;     //作业：将本例题改为固定布局
import javax.swing.*;
import java.awt.event.ActionEvent;//awt包中只是组件不用了 用swing中的组件 但是布局管理器 事件还是在用
import java.awt.event.ActionListener;//单击组件 有反应 ActionListener 是 Button 一类的事件响应接口
									//里面有一个actionPerformed方法 实现ActionListener的类 必须重写它
									//JFrame implements ActionListener 必须重写 actionPerformed

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
		super("按钮组件事件示例");
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
		ButtonGroup bg =new ButtonGroup();  //单选按钮中 只能选一个 方法放到一个组中
		rb = new JRadioButton[sex.length]; //数组与对象生成的区别,和35行的区别
											//用sec[]数组 生成JRadioButton数组
		for(int i=0; i<sex.length;i++){
			rb[i] = new JRadioButton(sex[i]);//sex[]数组中的元素放到JRadioButton[]数组中
											//首先要把"male" "female"放到一组中,bg
											//把单个选择按钮添加到panel中,注意不是add(bg)
											//即，添加到panel中，不是添加单选按钮组 是添加每个单选按钮
			bg.add(rb[i]);
			panel.add(rb[i]);
			
		}
		panel.add(new JLabel("hobbies"));
		cb = new JCheckBox[hobbies.length];   //通过hobbies[]生成CheckBox[]
		for(int i=0;i<hobbies.length;i++){
			cb[i] = new JCheckBox(hobbies[i]);
			panel.add(cb[i]);
		}
		
		btn_ok = new JButton("ok");
		btn_ok.addActionListener(this); //添加事件接口
		panel.add(btn_ok);
		this.setVisible(true);
		
		
	}
	
	
	public void actionPerformed(ActionEvent e){
		
		if(e.getSource()==btn_ok){       					//getSource()获取事件源
			str+= labelName.getText()+"\n"+text_name.getText()+"\n"+ labelSex.getText(); //获取文本行中输入的文本
			for(int i=0;i<rb.length;i++){
				if(rb[i].isSelected()){//isSelected ！！！考试要考
					
					str+= rb[i].getText();
				}
			}
			str +="\n hobbies:";
			for(int i=0;i<cb.length;i++){
				if(cb[i].isSelected()) str +="\n"+ cb[i].getText();
			}
			textArea.append(str);			//append(str)往文本区中添加需要显示的字符串
		}									//选中btn_ok，执行的内容到此才结束，即暴扣单选复选按钮的获取
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		new Button();
	}
	
}
