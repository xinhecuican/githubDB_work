package 第十一章.例5;

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
	private DatagramPacket sendPacket,receivePacket;	//数据报对象
	private DatagramSocket sendSocket,receiveSocket;	//发送和接收数据报的套接字（Socket）对象
	private InetAddress sendIp;							//目的地址
	private int sendPort,receivePort;					//发送端口和接收端口
	private byte inBuff[],outBuff[];					//接收和发送数据的缓冲区
	private static final int BUFFSIZE = 1024;			//
	
	public UDPChat(){
		
		super();
		getContentPane().setLayout(null);
		setTitle("基于UDP的聊天程序");
		setBounds(100,100,500,375);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		 lblSendPort  = new JLabel();
		 lblSendPort.setName("lblSendPort");
		 lblSendPort.setText("发送端口");
		 lblSendPort.setBounds(24, 29, 60,15);
		 getContentPane().add(lblSendPort);
		 
		 lblReceivePort  = new JLabel();
		 lblReceivePort.setName("lblReceivePort");
		 lblReceivePort.setText("接收端口");
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
		 btnListen.setText("开始监听");
		 btnListen.setBounds(24, 95, 156, 46);
		 getContentPane().add(btnListen);
		 
		 textShowMessage = new JTextArea();
		 textShowMessage.setRows(80);
		 textShowMessage.setColumns(40);
		 textShowMessage.setText("开始监听");
		 textShowMessage.setName("textShowMessage");
		 textShowMessage.setBorder(new LineBorder(Color.black,1,false));
		 textShowMessage.setBounds(24,175, 156, 76);
		 getContentPane().add(textShowMessage);
		 
		 btnSend = new JButton();
		 btnSend.addActionListener(this);
		 btnSend.setName("btnSend");
		 btnSend.setText("发送");
		 btnSend.setBounds(24, 265, 156, 46);
		 getContentPane().add(btnSend);
		 
		 textSendMessage = new JTextArea();
		 textSendMessage.setRows(40);
		 textSendMessage.setColumns(20);
		 textSendMessage.setText("开始监听");
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
			textShowMessage.append("我说："+textSendMessage.getText()+"\n");
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
				textShowMessage.append(sendIp.getHostAddress()+"说："+message+"\n");
			}catch(IOException e){
				textShowMessage.append("接收数据出错\n");
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
