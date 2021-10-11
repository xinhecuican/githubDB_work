package �ڰ���.��7;//�źű�������� �� �ֲ���������Ա����������������this��super,ѭ���������±�������źű���
				//��ĩ���������
public class Buffer {        //�ֿ�

	private char chBuffer;
	private boolean empty = true;
	
	public synchronized void put(char ch){   //���ֿ��зŲ�Ʒch
		while(!empty){
			
			try {
				wait();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		chBuffer = ch;                       //ch��ɲֿ��е�chBuffer
		empty = false;
		notify();							//�������� �����԰�  ֪ͨ����һ���γ�
	}
	
	public synchronized char get(){     
		
		while(empty){
			
			try {
				wait();						//û�з���ֻ�ܵȡ�
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		char chr = chBuffer;                //�Ӳֿ�����ȡchBuffer��chr
		chBuffer ='\0';                     //�ֿ�����Ϊ��
		empty = true;
		notify();							//���� ֪ͨ�������������з���
		return chr;                         //���Ӳֿ�����ȡ��chr����
	}
}
