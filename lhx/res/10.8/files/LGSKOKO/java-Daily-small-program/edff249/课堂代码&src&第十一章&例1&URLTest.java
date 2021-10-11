package 第十一章.例1;//线程、输入输出流、网络编程 考试

import java.net.MalformedURLException;
import java.net.URL;

public class URLTest {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		URLTest ut = new URLTest();
		ut.show();

	}
	
	private void show()
	{
		URL urlBase = null,urlNew = null;
		
		try {
			urlBase = new URL("http://www.oracle.com/");
			urlNew = new URL(urlBase,"index.html");
		} catch (MalformedURLException e) {
			
			e.printStackTrace();
		}
		
		System.out.println("protocol="+urlNew.getProtocol());
		System.out.println("host="+urlNew.getHost());
		System.out.println("prot="+urlNew.getPort());
		System.out.println("fileName="+urlNew.getFile());
		System.out.println("path="+urlNew.getPath());
		System.out.println("Authority="+urlNew.getAuthority());
	}

}
