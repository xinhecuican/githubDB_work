package 第十一章.例4;//考试也主要考查这个类型

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
			Socket socket = new Socket("127.0.0.1",PORT);//字节流对象
			BufferedReader fromServerIn = new BufferedReader(new InputStreamReader(socket.getInputStream()));
							//服务器端的输入流，接收客户端发送的信息,等着接收请求信息
			PrintWriter toServerOut = new PrintWriter(socket.getOutputStream());//打字用于向console输出
			
			BufferedReader keyBordin = new BufferedReader(new InputStreamReader(System.in));//接收控制台输入
			
			String message = null,answer = null;
			message = keyBordin.readLine();			//读取控制台发来的消息,因为客户端先发起请求
			while(!"bye".equals(message)&&message!=null)		
			{
				toServerOut.println(message);
				toServerOut.flush();
				System.out.println("server say"+fromServerIn.readLine());
				message = keyBordin.readLine();			//读取控制台发来的消息,因为客户端先发起请求
			}
			System.out.println("Client say: bye");
			
			
			fromServerIn.close();
			toServerOut.close();
			socket.close();
			
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			System.out.println("客户端，信息如下：");
			e.printStackTrace();
		}
	}

}
