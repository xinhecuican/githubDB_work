package µÚÊ®Ò»ÕÂ.Àý2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;

public class URLReader {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		URLReader ur = new URLReader();
		ur.readURL();
	}
	
	private void readURL()
	{
		try {
			URL myURL = new URL("http://www.baidu.com/");
			BufferedReader in = new BufferedReader(new InputStreamReader(myURL.openStream()));
			String inputLine;
			
			while((inputLine = in.readLine()) != null)
				System.out.println(inputLine);
			in.close();
		} catch (MalformedURLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}

}
