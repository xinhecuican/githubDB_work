package ��ʮһ��.��4;//����Ҳ��Ҫ�����������

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class Client {

	public static final int PORT = 5566;
	
	public static void main(String[] args) {
		
		Client client = new Client();
		client.run();

	}
	
	private void run()
	{
		
		try {
			//ServerSocket serverSocket = new ServerSocket(PORT);
			Socket socket = new Socket("127.0.0.1",PORT);//�ֽ�������
			BufferedReader fromServerIn = new BufferedReader(new InputStreamReader(socket.getInputStream()));
							//�������˵������������տͻ��˷��͵���Ϣ,���Ž���������Ϣ
			PrintWriter toServerOut = new PrintWriter(socket.getOutputStream());//����������console���
			
			BufferedReader keyBordin = new BufferedReader(new InputStreamReader(System.in));//���տ���̨����
			
			String message = null,answer = null;
			message = keyBordin.readLine();			//��ȡ����̨��������Ϣ,��Ϊ�ͻ����ȷ�������
			while(!"bye".equals(message)&&message!=null)		
			{
				toServerOut.println(message);
				toServerOut.flush();
				System.out.println("server say"+fromServerIn.readLine());
				message = keyBordin.readLine();			//��ȡ����̨��������Ϣ,��Ϊ�ͻ����ȷ�������
			}
			System.out.println("Client say: bye");
			
			
			fromServerIn.close();
			toServerOut.close();
			socket.close();
			
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			System.out.println("�ͻ��ˣ���Ϣ���£�");
			e.printStackTrace();
		}
	}

}
