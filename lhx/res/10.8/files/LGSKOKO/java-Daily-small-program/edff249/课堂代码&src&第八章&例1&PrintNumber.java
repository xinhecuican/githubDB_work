package �ڰ���.��1;

public class PrintNumber extends Thread {//һ��ʼû�� extends Thread����̶�

	
	private int num;
	
	public PrintNumber( int num){
		
		
		this.num = num;
	}
	
	public void run(){
		
		for(int i=0; i<num; i++){
			   
			System.out.print(i);
		}
		System.out.println();
	}
	
	public static void main(String[] args) {
		
		PrintNumber t1 = new PrintNumber(50);
		PrintLetter t2 = new PrintLetter('a',50);
//		t1.run();					//extends Thread �� �˴���run���������Ҳ�̶�
//		t2.run();
		t1.start();					//�̵߳���start()��  JVM�Զ�����run()��run�������߳��壬��Tread���еķ���
		t2.start();					//�������� �߳���  �̶߳���   �߳���
									//������Զ����õķ���   main  actionPerformed run
									//���Ƕ���.�����Ƕ�����á�û���κ�Ԫ��.��
									//�����̣߳� ���� t1 t2 main
									//���̵߳ĺô�������ÿ���߳�ʼ��ռ��JVM��CPU
									//�������ӡ����ݿ�򿪵��̶߳���Ҫʱ�䣬
									//�˿���ʱ�����CPU����ʱ��Ƭ����������̣߳��ͻ����̶����Ч��
									//�����Ŷӻ��ߵ��տ�ˮʱ �����ʻ��߿��ֻ�
									//���ಢû�ж���start()���� ���ǵ��ò�����˵��start�����Ǹ���Tread�ġ�
	}
	
	

}
