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
			FileReader fr = new FileReader("url.txt");//读取已经抓取的页面信息文件
			BufferedReader br = new BufferedReader(fr);
			
			FileWriter fw = new FileWriter("match.txt");//此文件用力存放有效的博文网址的文件
			BufferedWriter bw = new BufferedWriter(fw);
			
			String str ="";
			String readStr="";
			//编写正则表达式
			String regex="https://blog.csdn.net/\\w{1,}\\_\\d{1,}/article/details/\\d{1,}";
			
			Pattern p =  Pattern.compile(regex);//设置正则规则 不会可以查看Pattern和Matcher这两个类
			while(( readStr=br.readLine())!= null)
			{
				
				Matcher m = p.matcher(readStr);//进行匹配
				 while (m.find()){
					 if(!str.contains(m.group()))
					 {
						 str +=m.group();
		                 str+="\r\n";
					 } 
	               }
			
			}
			bw.write(str);
			bw.flush();//因为使用的是缓冲字符流，最好加上这句话 否则如果缓存区未满不会将信息写到文件中
			//这也就是为什么有的人会问为什么我的信息没成功写入文件中
			
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
