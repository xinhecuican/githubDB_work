package �ڰ���.��6;

import java.util.Random;

public class Procedure extends Thread {

	private Buffer br;
	Random r = new Random();
	
	public Procedure(Buffer br) {
		super();
		this.br = br;
	}
	
	public void run(){
		
		for(int i=0;i<5;i++){                   //���ڲ����߳�
			                                    //�ڵײ㣬��ĸA������65��ʾ
			char ch = (char)(65+r.nextInt(20)); //����ch��r.nextInt(20)����0��19������� ��
			br.put(ch);                        //����ֿ�
			System.out.println("������"+i+"�����˲�Ʒ:"+ch);
			try{
				sleep(5);
			}catch(InterruptedException e){
				
				e.printStackTrace();
			}
			
		}
	}
}
