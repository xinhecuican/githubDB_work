package 第十章.例3;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

//在内存中随机生成一个double型的数组，将其写到一个文件中，然后在从该文件读取出来，并将读取内容显示在console中。

public class DataStream {

	private String fileName;
	public DataStream(String fileName){
		
		this.fileName = fileName;
	}
	public static void main(String[] args) throws IOException {
		
		double buffer[] = new double[100];			//16-17-19-23-34-41
		for(int i=0;i<buffer.length;i++){		//创建数据,从内存中生成
			
			buffer[i] = (Math.random()*100);//通过随机方法生成一组byte类型的数，存在数组中
		}
		
		DataStream fileStream = new DataStream("DoubleFile.dat");
		fileStream.write2File(buffer);	//把内存中生成的double数组写到一个叫DoubleFile.dat的文件
										//FileStream表示
		fileStream.readFileContent();	//倒序法

	}
	private void readFileContent() throws IOException {
		
		
		FileInputStream fin = new FileInputStream(this.fileName);		//生成输入流对象，并且和文件名联系起来
		
		DataInputStream din = new DataInputStream(fin);
		int count = 0;
		while(true)
		{  try{
			double i = din.readDouble();		//从din中一个个读取，并返回，和read()同
			System.out.println(i+" ");
			count++;
			}catch(EOFException ioe){
				break;							//读完，抛出EOFException
												//处理该异常，用break强制结束循环
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
	private void write2File(double[] buffer) throws IOException {//定义时 buffer的类型及数组表示都要有，调用时不用
		
		FileOutputStream fout = new FileOutputStream(this.fileName);	//将buffer以字节写入文件
		//Elephant  aElephant = new Elephant("泰国大象")
																		//FileoutputStream()写入文件中
																		//fout 文件字节输出流的对象
		DataOutputStream dout = new DataOutputStream(fout);				//披着羊皮的狼，将输出流由字节转化为基本数据类型
		for(int i=0; i<buffer.length;i++){
			dout.writeDouble(buffer[i]);							//writeDouble只能一次写一个double类型的数
		}	
																		//写buffer到 fout
		dout.close();																//22-10-12-35使得
		fout.close();													//fileName对应 ByteFile.dat
		System.out.println("成功写入文件："+this.fileName);
	}

}
