package 第十章.例2;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

//在内存中随机生成一个字节型的数组，将其写到一个文件中，然后在读取该文件并将文件内容显示在console中。

public class FileStream {

	private String fileName;
	public FileStream(String fileName){
		
		this.fileName = fileName;
	}
	public static void main(String[] args) throws IOException {
		
		byte buffer[] = new byte[100];			//16-17-19-23-34-41
		for(int i=0;i<buffer.length;i++){		//创建数据,从内存中生成
			
			buffer[i] = (byte)(Math.random()*100);//通过随机方法生成一组byte类型的数，存在数组中
		}
		
		FileStream fileStream = new FileStream("ByteFile.dat");
		fileStream.write2File(buffer);	//把内存中生成的字节数生成的字节数组写到一个叫ByteFile.dat的文件
										//FileStream表示
		fileStream.readFileContent();	//倒序法

	}
	private void readFileContent() throws IOException {
		
		FileInputStream fin = new FileInputStream(this.fileName);		//生成输入流对象，并且和文件名联系起来
		byte[] buffer1 = new byte[20];
		int count = 0;
		do{
			count = fin.read(buffer1);
			for(int i=0; i<count;i++){
				System.out.println(buffer1+" ");
			}
		}while(count != -1);
		
		fin.close();
	}
	private void write2File(byte[] buffer) throws IOException {//定义时 buffer的类型及数组表示都要有，调用时不用
		
		FileOutputStream fout = new FileOutputStream(this.fileName);	//将buffer以字节写入文件
		//Elephant  aElephant = new Elephant("泰国大象")
																		//FileoutputStream()写入文件中
																		//fout 文件字节输出流的对象
		fout.write(buffer);												//写buffer到 fout
																		//22-10-12-35使得
		fout.close();													//fileName对应 ByteFile.dat
		System.out.println("成功写入文件："+this.fileName);
	}

}
