package ��ʮ��.��1;

import java.io.IOException;

public class StandardIO {

	int count = 0;
	byte buffer[];		//byte����ֻ�����ڴ��г��֣���ʵ��û��
	
	public StandardIO() throws IOException{//�ļ��Ҳ������ڳ���Ա�޷��ٳ����д���ģ���˲���try/catch
										   //����throws IOException �������Ƹ������JVM������Щ�쳣
		do{
			System.out.println("�����룺");
			buffer = new byte[512];
			count = System.in.read(buffer);		//System.in��io���е���		IOException
			System.out.println("������ֽ��ǣ�");
			for(int i=0;i<count;i++){
				
				System.out.println(buffer[i]);//in��out�Ǿ�̬����
				System.out.println(" ");	  //out �� printStream���͵� in ��INputStream���͵�
											  
			}
			
			System.out.println();
			System.out.println("����"+count+"���ֽ���");
		}while(count != 2);
	}
	
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		new StandardIO();

	}

}
