package teste;

import java.util.ArrayList;

public class Teste {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		ArrayList<String> stringList = new ArrayList<String>();
		stringList.add("Item");
		
		for (int i = 0; i < stringList.size(); i++ ){
			String item = stringList.get(i);
			System.out.print(item);
		}

	}

}
