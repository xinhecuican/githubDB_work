package views;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;



public class Url {
	
 public void openUrl(String str)
 {
	 try {
		URL myUrl = new URL(str);//打开指定网址
		
		InputStreamReader is =new InputStreamReader( myUrl.openStream(),"utf-8");
		//myUrl.openStream()是打开与此URL的连接，并返回一个InputStream以从该连接读取
		// API文档说明：InputStreamReader类是从字节流到字符流的桥接器：它使用指定的字符集读取字节并将它们解码为字符。
		BufferedReader br = new BufferedReader(is);//将inputStramReader转化为BufferReader
		
		FileWriter fw = new FileWriter("url.txt");
		BufferedWriter bw = new BufferedWriter(fw);
		
		
		String str1 ="";
		String str2="";
		while((str1=br.readLine())!= null)
		{
			str2+=str1;
			str2+="\r\n";
			
		}
		
		bw.write(str2);
		bw.flush();//因为使用的是缓冲字符流，最好加上这句话 否则如果缓存区未满不会将信息写到文件中
		//这也就是为什么有的人会问为什么我的信息没成功写入文件中
		
		is.close();
		br.close();
		fw.close();
		bw.close();
		
	} catch (MalformedURLException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	} catch (IOException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
 }
 
   

}
