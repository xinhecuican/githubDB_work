package �ڰ���.��2;

public class PrintLetter implements Runnable{

	private char letter;
	private int num;
	
	public PrintLetter(char ch, int num){
		
		letter = ch;
		this.num = num;
	}
	
	public void run(){				//����þ�û��,PrintLetter���� ��ʾadd unimplemented methods
									//��˵�� run����������Runnable�ӿ��еķ���   ��ô,Tread���е�run�����أ�
									//ʵ���� Tread����JDK���Ѿ�ʵ���� Runnable�ӿ� ��ˣ�Thread���е�run()����Runnable
		
		for(int i=0; i<num; i++){
			
			System.out.print(letter);
		}
		
	}
	

}
