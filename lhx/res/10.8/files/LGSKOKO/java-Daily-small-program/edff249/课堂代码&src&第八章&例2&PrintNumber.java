package �ڰ���.��2;

public class PrintNumber implements Runnable {//һ��ʼû�� extends Thread����̶�

	
	private int num;						//?�̳�Thread�����̳��̱߳��,��Ҫ�ṩʵ�֡�Runnable�ӿڵķ���
											//����Ϊ��ʱһ����Ҫ�̳��������� ��Javaֻ����̳�һ����
											//����һ��ͼ�ν����� ����̳�JFrame �����ܼ̳�Thread
	
	public PrintNumber( int num){
		
		
		this.num = num;
	}
	
	public void run(){
		
		for(int i=0; i<num; i++){
			   
			System.out.print(i);
		}
		
	}
	
	public static void main(String[] args) {
		
		PrintNumber t1 = new PrintNumber(50);
		PrintLetter t2 = new PrintLetter('a',50);
		
		new Thread(t1).start();			//extends Tread�� �˴����õ�start()������ ����Ϊstart������Tread����		
		new Thread(t2).start();			//����û�м̳�Threa�� ��� ���ܵ���start����
							//��μȴ����߳��̶߳����ֺ�t1�й��� ���á�������Ƥ���ǡ����ַ���
									
	}
	
	

}
