package 第十章.例4;		//作业：从d盘建立两个text文件file1和file2，file1中有"今天"两个字，file2中有”java考试"
						//几个字，将file2中的“java考试"读到file1中，file2中的内容不变,file的内容变为"今天java考试".
						//也可以在程序中创建file1和file2，将file2中的内容拷贝到file1，需要先将file2中的内容读到
						//内存，然后从内存写到file1.

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

//在内存中随机生成一个double型的数组，将其写到一个文件中，然后在从该文件读取出来，并将读取内容显示在console中。

public class ObjectStream {

	private String fileName;
	public ObjectStream(String fileName){
		
		this.fileName = fileName;
	}
	public static void main(String[] args) throws IOException {
		
		
		ObjectStream fileStream = new ObjectStream("D:\\ObjFile.dat");
		MyInt[] myInt = new MyInt[10];
		for(int i=0;i<10;i++)
		{
			int v = (int)(Math.random()*100);
			myInt[i] = new MyInt(v);
		}
		fileStream.write2File(myInt);	//把内存中生成的double数组写到一个叫DoubleFile.dat的文件
										//FileStream表示
		fileStream.readFileContent();	//倒序法

	}
	private void readFileContent() throws IOException {
		
		
		FileInputStream fin = new FileInputStream(this.fileName);		//生成输入流对象，并且和文件名联系起来
		
		ObjectInputStream din = new ObjectInputStream(fin);
		int count = 0;
		while(true)
		{  try{
			MyInt myInt = (MyInt) din.readObject();		//从din中一个个读取，并返回，和read()同
			System.out.println(myInt.toString());
			count++;
			}catch(IOException ioe){
				System.out.println(ioe);
				break;							//读完，抛出EOFException
												//处理该异常，用break强制结束循环
			}catch(Exception e){				//读取对象结束也是抛出异常
				System.out.println(e);
				break;
			}
			
		}
		System.out.println("本次读入"+count+"个双精度浮点数");
		din.close();
		
//		byte[] buffer1 = new byte[20];
//		int count = 0;
//		do{
//			count = fin.read(buffer1);
//			for(int i=0; i<count;i++){
//				System.out.println(buffer1+" ");
//			}
//		}while(count != -1);
		
		fin.close();
	}
	private void write2File(Object[] obj) throws IOException {//定义时 buffer的类型及数组表示都要有，调用时不用
		
		FileOutputStream fout = new FileOutputStream(this.fileName);	//将buffer以字节写入文件
		//Elephant  aElephant = new Elephant("泰国大象")
																		//FileoutputStream()写入文件中
																		//fout 文件字节输出流的对象
		ObjectOutputStream dout = new ObjectOutputStream(fout);				//披着羊皮的狼，将输出流由字节转化为基本数据类型
		for(int i=0; i<obj.length;i++){
			dout.writeObject(obj[i]);								//writeDouble只能一次写一个double类型的数
		}
																		//写buffer到 fout
		dout.close();																//22-10-12-35使得
		fout.close();													//fileName对应 ByteFile.dat
		System.out.println("成功写入文件："+this.fileName);
	}
	
	

}
