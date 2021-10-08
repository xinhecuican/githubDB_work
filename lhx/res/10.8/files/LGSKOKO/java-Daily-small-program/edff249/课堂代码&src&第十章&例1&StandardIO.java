package 第十章.例1;

import java.io.IOException;

public class StandardIO {

	int count = 0;
	byte buffer[];		//byte类型只有在内存中出现，现实中没有
	
	public StandardIO() throws IOException{//文件找不到等于程序员无法再程序中处理的，因此不用try/catch
										   //而用throws IOException 其义是推给虚拟机JVM处理这些异常
		do{
			System.out.println("请输入：");
			buffer = new byte[512];
			count = System.in.read(buffer);		//System.in是io包中的类		IOException
			System.out.println("输入的字节是：");
			for(int i=0;i<count;i++){
				
				System.out.println(buffer[i]);//in、out是静态变量
				System.out.println(" ");	  //out 是 printStream类型的 in 是INputStream类型的
											  
			}
			
			System.out.println();
			System.out.println("输入"+count+"个字节数");
		}while(count != 2);
	}
	
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		new StandardIO();

	}

}
