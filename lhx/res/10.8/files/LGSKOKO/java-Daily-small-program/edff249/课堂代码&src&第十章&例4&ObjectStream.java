package ��ʮ��.��4;		//��ҵ����d�̽�������text�ļ�file1��file2��file1����"����"�����֣�file2���С�java����"
						//�����֣���file2�еġ�java����"����file1�У�file2�е����ݲ���,file�����ݱ�Ϊ"����java����".
						//Ҳ�����ڳ����д���file1��file2����file2�е����ݿ�����file1����Ҫ�Ƚ�file2�е����ݶ���
						//�ڴ棬Ȼ����ڴ�д��file1.

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

//���ڴ����������һ��double�͵����飬����д��һ���ļ��У�Ȼ���ڴӸ��ļ���ȡ������������ȡ������ʾ��console�С�

public class ObjectStream {

	private String fileName;
	public ObjectStream(String fileName){
		
		this.fileName = fileName;
	}
	public static void main(String[] args) throws IOException {
		
		
		ObjectStream fileStream = new ObjectStream("D:\\ObjFile.dat");
		MyInt[] myInt = new MyInt[10];
		for(int i=0;i<10;i++)
		{
			int v = (int)(Math.random()*100);
			myInt[i] = new MyInt(v);
		}
		fileStream.write2File(myInt);	//���ڴ������ɵ�double����д��һ����DoubleFile.dat���ļ�
										//FileStream��ʾ
		fileStream.readFileContent();	//����

	}
	private void readFileContent() throws IOException {
		
		
		FileInputStream fin = new FileInputStream(this.fileName);		//�������������󣬲��Һ��ļ�����ϵ����
		
		ObjectInputStream din = new ObjectInputStream(fin);
		int count = 0;
		while(true)
		{  try{
			MyInt myInt = (MyInt) din.readObject();		//��din��һ������ȡ�������أ���read()ͬ
			System.out.println(myInt.toString());
			count++;
			}catch(IOException ioe){
				System.out.println(ioe);
				break;							//���꣬�׳�EOFException
												//������쳣����breakǿ�ƽ���ѭ��
			}catch(Exception e){				//��ȡ�������Ҳ���׳��쳣
				System.out.println(e);
				break;
			}
			
		}
		System.out.println("���ζ���"+count+"��˫���ȸ�����");
		din.close();
		
//		byte[] buffer1 = new byte[20];
//		int count = 0;
//		do{
//			count = fin.read(buffer1);
//			for(int i=0; i<count;i++){
//				System.out.println(buffer1+" ");
//			}
//		}while(count != -1);
		
		fin.close();
	}
	private void write2File(Object[] obj) throws IOException {//����ʱ buffer�����ͼ������ʾ��Ҫ�У�����ʱ����
		
		FileOutputStream fout = new FileOutputStream(this.fileName);	//��buffer���ֽ�д���ļ�
		//Elephant  aElephant = new Elephant("̩������")
																		//FileoutputStream()д���ļ���
																		//fout �ļ��ֽ�������Ķ���
		ObjectOutputStream dout = new ObjectOutputStream(fout);				//������Ƥ���ǣ�����������ֽ�ת��Ϊ������������
		for(int i=0; i<obj.length;i++){
			dout.writeObject(obj[i]);								//writeDoubleֻ��һ��дһ��double���͵���
		}
																		//дbuffer�� fout
		dout.close();																//22-10-12-35ʹ��
		fout.close();													//fileName��Ӧ ByteFile.dat
		System.out.println("�ɹ�д���ļ���"+this.fileName);
	}
	
	

}
