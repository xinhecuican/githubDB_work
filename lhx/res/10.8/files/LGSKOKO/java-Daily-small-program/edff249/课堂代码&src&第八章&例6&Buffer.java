package �ڰ���.��6;

public class Buffer {        //�ֿ�

	private char chBuffer;
	
	public synchronized void put(char ch){   //���ֿ��зŲ�Ʒch
		
		chBuffer = ch;                       //ch��ɲֿ��е�chBuffer
	}
	
	public synchronized char get(){         
		
		char chr = chBuffer;                //�Ӳֿ�����ȡchBuffer��chr
		chBuffer ='\0';                     //�ֿ�����Ϊ��
		return chr;                         //���Ӳֿ�����ȡ��chr����
	}
}
