package views;


import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import java.awt.GridLayout;
import javax.swing.JLabel;
import javax.swing.JTextField;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.Color;
import javax.swing.JRadioButton;
import javax.swing.JButton;

public class Gui extends JFrame  implements ActionListener {

	private JPanel contentPane;
	private JTextField textField;//��¼������ַ
	private JTextField textField_1;//��¼����ƪ��
	private JRadioButton radioButton;//��ѡ��ť����¼�Ƿ��������
	private JButton start;//��ʼ��ť			
	private JButton stop;
	private DesktopTest4 dt;
	


	public void setDt(DesktopTest4 dt) {
		this.dt = dt;
	}

	/**
	 * Create the frame.
	 */
	public Gui() {
		setForeground(Color.RED);
		setIconImage(Toolkit.getDefaultToolkit().getImage("C:\\Users\\hhh\u674E\u5148\u751F\\Desktop\\hdImg_37062827837e2d79bb5a86b1cb5bdda415490926835.jpg"));
		setTitle("ˢ���ͷ��������Ķ���С����");
		
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(new GridLayout(2,1));
		
		JPanel panel = new JPanel();
		contentPane.add(panel);
		panel.setLayout(new GridLayout(3,1));
		
		JPanel panel_2 = new JPanel();
		panel.add(panel_2);
		
		JLabel label = new JLabel("\u535A\u5BA2\u7F51\u5740\uFF1A");
		panel_2.add(label);
		
		textField = new JTextField();
		panel_2.add(textField);
		textField.setColumns(30);
		
		JPanel panel_3 = new JPanel();
		panel.add(panel_3);
		
		JLabel label_1 = new JLabel("\u8BBF\u95EE\u7BC7\u6570\uFF1A");
		panel_3.add(label_1);
		
		textField_1 = new JTextField();
		panel_3.add(textField_1);
		textField_1.setColumns(10);
		
		JPanel panel_4 = new JPanel();
		panel.add(panel_4);
		
		JLabel label_2 = new JLabel("\u662F\u5426\u968F\u673A:");
		panel_4.add(label_2);
		
		 radioButton = new JRadioButton("\u968F\u673A\u8BBF\u95EE");
		panel_4.add(radioButton);
		
		JPanel panel2 = new JPanel();
		contentPane.add(panel2);
		panel2.setLayout(new GridLayout(1,2));
		
		JPanel panel_1 = new JPanel();
		panel2.add(panel_1);
		
		start = new JButton("\u5F00\u59CB");//��ʼ��ť
		panel_1.add(start);
		start.addActionListener(this);
		
		stop = new JButton("\u7ED3\u675F");//������ť
		stop.setEnabled(false);
		panel_1.add(stop);
		stop.addActionListener(this);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setVisible(true);						    //���û�����룬ͼ�ξ��޷���ʾ
	}
	
	// ������ť
	public void actionPerformed(ActionEvent e) {
		//�жϰ�ť��Ϣ��Դ
		if(e.getSource()== start){
			
			String str = textField.getText();
			Url url = new Url();
			url.openUrl(str);
			Match match = new Match();
			match.compare();
			int j =Integer.parseInt(textField_1.getText());//��ȡ����ƪ��
			Boolean b = false;
			if(radioButton.isSelected())				//�жϵ�ѡ��ť�Ƿ�ѡ��
				b =true;
			dt.begin(j,b);
			start.setEnabled(false);
			stop.setEnabled(true);
		}else if(e.getSource() == stop) {
			stop.setEnabled(false);
			start.setEnabled(true);
			
		}
		
	}

}
