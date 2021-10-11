package views;

//import java.awt.Desktop;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
//import java.net.URI;
import java.net.URL;
import java.util.ArrayList;
import java.util.Random;

public class DesktopTest4 {


	public ArrayList<String> strList = new ArrayList<String>();//定义一个String类型的泛型集合
	public int count = 0;	//定义一个变量  用来记录你一共有多少条博文网址
	public int num =0;		//定义一个变量 用来记录你现在完成了第几遍便利
	public int i=0;
	public Random random = new Random();
	private Gui gui;

	public void setGui(Gui gui) {
		this.gui = gui;
	}

	/*
	 * 调用此方法通过正则表达式进行匹配
	 * 匹配有效的博文网址
	 */
	public void match(){
		
		try {
			
			FileReader fr = new FileReader("match.txt");
			BufferedReader br = new BufferedReader(fr);
			String str = "";
			
		    while((str = br.readLine())!= null){
		    	strList.add(str);
		    	count++;
					
				}
			 fr.close();
			 br.close();
			
		} catch (FileNotFoundException e) {
			
			e.printStackTrace();
		}catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	
	/*
	 * 通过此方法达成打开相应网址的效果
	 */
	public  void browse(String uri){
		
		try {
			URL url = new URL(uri);
			InputStream is =url.openStream();
			
		} catch (MalformedURLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	
	
	/*
	 * 此方法为进行无限循环
	 * 并定时休眠线程
	 */
	public  void begin(int j1,Boolean b) {
		match();
		//如果为真则采用随机访问，否则全部遍历
		if(b) {
			random(j1);
			
		}else {
			all(j1);
		}
		

	}
	
	/*
	 * 此方法为全部遍历方法
	 */
	public void all(int j2) {
		while(true){
			
			try{
				if(i<count)
				{
					//int hhh = random.nextInt(3);	
					for(int k=0; k<j2;k++)
					  browse((String)strList.get(k));
					Thread.sleep(40000);//这里的单位是毫秒  打开每个博文网址间隔多少ms
					System.out.println("完成第"+i+"个for循环");
					
				}else{
					i=-1;
					num++;
					System.out.println("完成第"+num+"轮访问");
					
					// Runtime.getRuntime().exec("taskkill /F /IM firefox.exe");
					Thread.sleep(60000);//这里的单位是毫秒  完成每次总的博文遍历间隔多少ms
				}				
			}catch(Exception e){
				e.printStackTrace();
			}
			i++;
		}
	}
	
	public void random(int j2) {
		while(true){
			
			try{
				if(i<count)
				{
					
					for(int k=0; k<j2;k++)
					{
						int hhh = random.nextInt(j2);
						browse((String)strList.get(hhh));
					}
					Thread.sleep(40000);//这里的单位是毫秒  打开每个博文网址间隔多少ms
					System.out.println("完成第"+i+"个for循环");
					
				}else{
					i=-1;
					num++;
					System.out.println("完成第"+num+"轮访问");
					// Runtime.getRuntime().exec("taskkill /F /IM firefox.exe");
					Thread.sleep(60000);//这里的单位是毫秒  完成每次总的博文遍历间隔多少ms
				}				
			}catch(Exception e){
				e.printStackTrace();
			}
			i++;
		}
	}
	
	

}
