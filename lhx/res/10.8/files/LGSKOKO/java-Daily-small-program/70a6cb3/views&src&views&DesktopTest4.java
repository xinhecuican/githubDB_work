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


	public ArrayList<String> strList = new ArrayList<String>();//����һ��String���͵ķ��ͼ���
	public int count = 0;	//����һ������  ������¼��һ���ж�����������ַ
	public int num =0;		//����һ������ ������¼����������˵ڼ������
	public int i=0;
	public Random random = new Random();
	private Gui gui;

	public void setGui(Gui gui) {
		this.gui = gui;
	}

	/*
	 * ���ô˷���ͨ��������ʽ����ƥ��
	 * ƥ����Ч�Ĳ�����ַ
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
	 * ͨ���˷�����ɴ���Ӧ��ַ��Ч��
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
	 * �˷���Ϊ��������ѭ��
	 * ����ʱ�����߳�
	 */
	public  void begin(int j1,Boolean b) {
		match();
		//���Ϊ�������������ʣ�����ȫ������
		if(b) {
			random(j1);
			
		}else {
			all(j1);
		}
		

	}
	
	/*
	 * �˷���Ϊȫ����������
	 */
	public void all(int j2) {
		while(true){
			
			try{
				if(i<count)
				{
					//int hhh = random.nextInt(3);	
					for(int k=0; k<j2;k++)
					  browse((String)strList.get(k));
					Thread.sleep(40000);//����ĵ�λ�Ǻ���  ��ÿ��������ַ�������ms
					System.out.println("��ɵ�"+i+"��forѭ��");
					
				}else{
					i=-1;
					num++;
					System.out.println("��ɵ�"+num+"�ַ���");
					
					// Runtime.getRuntime().exec("taskkill /F /IM firefox.exe");
					Thread.sleep(60000);//����ĵ�λ�Ǻ���  ���ÿ���ܵĲ��ı����������ms
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
					Thread.sleep(40000);//����ĵ�λ�Ǻ���  ��ÿ��������ַ�������ms
					System.out.println("��ɵ�"+i+"��forѭ��");
					
				}else{
					i=-1;
					num++;
					System.out.println("��ɵ�"+num+"�ַ���");
					// Runtime.getRuntime().exec("taskkill /F /IM firefox.exe");
					Thread.sleep(60000);//����ĵ�λ�Ǻ���  ���ÿ���ܵĲ��ı����������ms
				}				
			}catch(Exception e){
				e.printStackTrace();
			}
			i++;
		}
	}
	
	

}
