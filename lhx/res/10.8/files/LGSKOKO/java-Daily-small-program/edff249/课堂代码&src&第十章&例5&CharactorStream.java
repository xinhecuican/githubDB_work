package 第十章.例5;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

//在内存中随机生成一个double型的数组，将其写到一个文件中，然后在从该文件读取出来，并将读取内容显示在console中。

public class CharactorStream {

	private String fileName;
	public CharactorStream(String fileName){
		
		this.fileName = fileName;
	}
	public static void main(String[] args) throws IOException {
		
		int buffer[] = new int[100];			//16-17-19-23-34-41
		for(int i=0;i<buffer.length;i++){		//创建数据,从内存中生成
			
			buffer[i] = (int) (Math.random()*100);//通过随机方法生成一组byte类型的数，存在数组中
		}
		
		CharactorStream fileStream = new CharactorStream("CharFile.dat");
		fileStream.write2File(buffer);	//把内存中生成的double数组写到一个叫DoubleFile.dat的文件
										//FileStream表示
		fileStream.readFileContent();	//倒序法

	}
	private void readFileContent() throws IOException {
		
		
		FileReader fin = new FileReader(this.fileName);		//生成输入流对象，并且和文件名联系起来
		
		BufferedReader din = new BufferedReader(fin);
		

		int count = 0;
		String aline = null;
		do{
			aline = din.readLine();
			if(aline != null){
				System.out.println(aline);
			}
		}while(aline != null);							//字符输入缓冲流结束的标志是 aline =null
		System.out.println("本次读入"+count+"行");
		System.out.println("本次读入"+count+"个双精度浮点数");
		din.close();
		

		
		fin.close();
	}
	private void write2File(int[] buffer) throws IOException {//定义时 buffer的类型及数组表示都要有，调用时不用
		
		FileWriter fout = new FileWriter(this.fileName);	//将buffer以字符形式写入文件
		//Elephant  aElephant = new Elephant("泰国大象")
																		//FileoutputStream()写入文件中
																		//字符输出流
		BufferedWriter dout = new BufferedWriter(fout);				//缓冲字符输出流，一次将所有字符写入
		for(int i=0; i<buffer.length;i++){
			dout.write(buffer[i]);								//跟字节流的writer(buffer），相同点是可以读写数组
														//不同点是底层读写的格式不同，byte和char类型
			if((i+1)%10 == 0) dout.newLine();
		}
																		//写buffer到 fout
		dout.close();																//22-10-12-35使得
		fout.close();													//fileName对应 ByteFile.dat
		System.out.println("成功写入文件："+this.fileName);
	}

}
