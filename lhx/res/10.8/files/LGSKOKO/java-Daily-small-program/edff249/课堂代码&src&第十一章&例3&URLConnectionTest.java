package µÚÊ®Ò»ÕÂ.Àý3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.util.Date;

public class URLConnectionTest {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		URLConnectionTest test = new URLConnectionTest();
		test.readByURLConnection();

	}
	
	private void readByURLConnection()
	{
		try {
			URL url = new URL("http://www.baidu.com");
			URLConnection conn = url.openConnection();
			BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
			//URL: MyURL.openStream() URLConnection:conn.getInputStream()
			
			System.out.println("contentLength="+conn.getContentLength());
			System.out.println("contentType="+conn.getContentType());
			System.out.println("contentEncoding="+conn.getContentEncoding());
			System.out.println("Date="+new Date(conn.getDate()));
			System.out.println("contentLength="+new Date(conn.getLastModified()));
			
			String line = br.readLine();
			while(line != null)
			{
				System.out.println(line);
				line = br.readLine();
			}
			
			br.close();
				
			
		} catch (MalformedURLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
