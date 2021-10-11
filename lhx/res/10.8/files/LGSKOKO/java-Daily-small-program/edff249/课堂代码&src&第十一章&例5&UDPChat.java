package ��ʮһ��.��5;

import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.net.*;

import javax.swing.*;
import javax.swing.border.LineBorder;

public class UDPChat extends JFrame implements Runnable,ActionListener{
	
	private JLabel lblSendPort,lblReceivePort;
	private JTextField textSendPort,textReceivePort;
	private JTextArea textSendMessage,textShowMessage;
	private JButton btnListen,btnSend;
	private Thread myThread = null;
	private DatagramPacket sendPacket,receivePacket;	//���ݱ�����
	private DatagramSocket sendSocket,receiveSocket;	//���ͺͽ������ݱ����׽��֣�Socket������
	private InetAddress sendIp;							//Ŀ�ĵ�ַ
	private int sendPort,receivePort;					//���Ͷ˿ںͽ��ն˿�
	private byte inBuff[],outBuff[];					//���պͷ������ݵĻ�����
	private static final int BUFFSIZE = 1024;			//
	
	public UDPChat(){
		
		super();
		getContentPane().setLayout(null);
		setTitle("����UDP���������");
		setBounds(100,100,500,375);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		 lblSendPort  = new JLabel();
		 lblSendPort.setName("lblSendPort");
		 lblSendPort.setText("���Ͷ˿�");
		 lblSendPort.setBounds(24, 29, 60,15);
		 getContentPane().add(lblSendPort);
		 
		 lblReceivePort  = new JLabel();
		 lblReceivePort.setName("lblReceivePort");
		 lblReceivePort.setText("���ն˿�");
		 lblReceivePort.setBounds(24, 62, 60,15);
		 getContentPane().add(lblReceivePort);
		 
		 textSendPort  = new JTextField();
		 textSendPort.setName("textSendPort");
		 textSendPort.setBounds(90, 26, 90,21);
		 getContentPane().add(textSendPort);
		 
		 textReceivePort  = new JTextField();
		 textReceivePort.setName("textSendPort");
		 textReceivePort.setBounds(90, 59, 90,21);
		 getContentPane().add(textReceivePort);
		 
		 btnListen = new JButton();
		 btnListen.addActionListener(this);
		 btnListen.setName("btnListen");
		 btnListen.setText("��ʼ����");
		 btnListen.setBounds(24, 95, 156, 46);
		 getContentPane().add(btnListen);
		 
		 textShowMessage = new JTextArea();
		 textShowMessage.setRows(80);
		 textShowMessage.setColumns(40);
		 textShowMessage.setText("��ʼ����");
		 textShowMessage.setName("textShowMessage");
		 textShowMessage.setBorder(new LineBorder(Color.black,1,false));
		 textShowMessage.setBounds(24,175, 156, 76);
		 getContentPane().add(textShowMessage);
		 
		 btnSend = new JButton();
		 btnSend.addActionListener(this);
		 btnSend.setName("btnSend");
		 btnSend.setText("����");
		 btnSend.setBounds(24, 265, 156, 46);
		 getContentPane().add(btnSend);
		 
		 textSendMessage = new JTextArea();
		 textSendMessage.setRows(40);
		 textSendMessage.setColumns(20);
		 textSendMessage.setText("��ʼ����");
		 textSendMessage.setName("textSendMessage");
		 textSendMessage.setBorder(new LineBorder(Color.black,1,false));
		 textSendMessage.setBounds(196, 95, 156, 166);
		 getContentPane().add(textSendMessage);
		 
		 btnSend.setEnabled(false);
		 textShowMessage.setEditable(false);
		 textSendMessage.setEditable(false);


		 getContentPane().add(textShowMessage);
		 
		 
		 
		
	}
	
	

	public void actionPerformed(ActionEvent e)
	{
	try{
		if(e.getSource()==btnListen)
		{
			if(textSendPort.getText().trim() == null || textReceivePort.getText().trim() == null)
			{
				return;
			}
		
		inBuff = new byte[BUFFSIZE];
		sendPort = Integer.parseInt(textSendPort.getText().trim());
		sendIp = InetAddress.getByName("locahost");
		
		sendSocket = new DatagramSocket();
		receivePort = Integer.parseInt(textReceivePort.getText());
		receivePacket = new DatagramPacket(inBuff,BUFFSIZE);
		receiveSocket = new DatagramSocket(receivePort);
		myThread = new Thread(this);
		myThread.setPriority(myThread.MIN_PRIORITY);
		myThread.start();
		btnListen.setEnabled(false);
		btnSend.setEnabled(true);
		textSendMessage.setEditable(true);
		}else{
			outBuff = textSendMessage.getText().getBytes();
			sendPacket = new DatagramPacket(outBuff,outBuff.length,sendIp,sendPort);
			sendSocket.send(sendPacket);
			textShowMessage.append("��˵��"+textSendMessage.getText()+"\n");
			textSendMessage.setText(null);
		}

	}catch(Exception e1)
		{
			
		}
	}
	
	public void run()
	{
		String message = null;
		while(true){
			try{
				receiveSocket.receive(receivePacket);
				message = new String(receivePacket.getData(),0,receivePacket.getLength());
				textShowMessage.append(sendIp.getHostAddress()+"˵��"+message+"\n");
			}catch(IOException e){
				textShowMessage.append("�������ݳ���\n");
			}
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try{
		UDPChat frame = new UDPChat();
		frame.setVisible(true);
		}catch(Exception e)
		{
			e.printStackTrace();
		}
	}

}
