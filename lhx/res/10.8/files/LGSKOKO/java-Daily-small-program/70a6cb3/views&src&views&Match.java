package views;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Match {

	public void compare(){
	
		try {
			FileReader fr = new FileReader("url.txt");//��ȡ�Ѿ�ץȡ��ҳ����Ϣ�ļ�
			BufferedReader br = new BufferedReader(fr);
			
			FileWriter fw = new FileWriter("match.txt");//���ļ����������Ч�Ĳ�����ַ���ļ�
			BufferedWriter bw = new BufferedWriter(fw);
			
			String str ="";
			String readStr="";
			//��д������ʽ
			String regex="https://blog.csdn.net/\\w{1,}\\_\\d{1,}/article/details/\\d{1,}";
			
			Pattern p =  Pattern.compile(regex);//����������� ������Բ鿴Pattern��Matcher��������
			while(( readStr=br.readLine())!= null)
			{
				
				Matcher m = p.matcher(readStr);//����ƥ��
				 while (m.find()){
					 if(!str.contains(m.group()))
					 {
						 str +=m.group();
		                 str+="\r\n";
					 } 
	               }
			
			}
			bw.write(str);
			bw.flush();//��Ϊʹ�õ��ǻ����ַ�������ü�����仰 �������������δ�����Ὣ��Ϣд���ļ���
			//��Ҳ����Ϊʲô�е��˻���Ϊʲô�ҵ���Ϣû�ɹ�д���ļ���
			
			fr.close();
			br.close();
			fw.close();
			bw.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	

}
