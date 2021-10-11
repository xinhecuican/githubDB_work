package µÚ°ËÕÂ.Àı1;

public class PrintLetter extends Thread{

	private char letter;
	private int num;
	
	public PrintLetter(char ch, int num){
		
		letter = ch;
		this.num = num;
	}
	
	public void run(){
		
		for(int i=0; i<num; i++){
			
			System.out.print(letter);
		}
		System.out.println();
	}
	

}
