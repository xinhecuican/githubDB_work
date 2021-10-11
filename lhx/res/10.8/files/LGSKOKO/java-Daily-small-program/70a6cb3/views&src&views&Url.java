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
		URL myUrl = new URL(str);//��ָ����ַ
		
		InputStreamReader is =new InputStreamReader( myUrl.openStream(),"utf-8");
		//myUrl.openStream()�Ǵ����URL�����ӣ�������һ��InputStream�ԴӸ����Ӷ�ȡ
		// API�ĵ�˵����InputStreamReader���Ǵ��ֽ������ַ������Ž�������ʹ��ָ�����ַ�����ȡ�ֽڲ������ǽ���Ϊ�ַ���
		BufferedReader br = new BufferedReader(is);//��inputStramReaderת��ΪBufferReader
		
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
		bw.flush();//��Ϊʹ�õ��ǻ����ַ�������ü�����仰 �������������δ�����Ὣ��Ϣд���ļ���
		//��Ҳ����Ϊʲô�е��˻���Ϊʲô�ҵ���Ϣû�ɹ�д���ļ���
		
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
