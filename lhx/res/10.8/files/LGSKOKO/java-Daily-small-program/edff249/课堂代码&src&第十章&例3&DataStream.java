package ��ʮ��.��3;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

//���ڴ����������һ��double�͵����飬����д��һ���ļ��У�Ȼ���ڴӸ��ļ���ȡ������������ȡ������ʾ��console�С�

public class DataStream {

	private String fileName;
	public DataStream(String fileName){
		
		this.fileName = fileName;
	}
	public static void main(String[] args) throws IOException {
		
		double buffer[] = new double[100];			//16-17-19-23-34-41
		for(int i=0;i<buffer.length;i++){		//��������,���ڴ�������
			
			buffer[i] = (Math.random()*100);//ͨ�������������һ��byte���͵���������������
		}
		
		DataStream fileStream = new DataStream("DoubleFile.dat");
		fileStream.write2File(buffer);	//���ڴ������ɵ�double����д��һ����DoubleFile.dat���ļ�
										//FileStream��ʾ
		fileStream.readFileContent();	//����

	}
	private void readFileContent() throws IOException {
		
		
		FileInputStream fin = new FileInputStream(this.fileName);		//�������������󣬲��Һ��ļ�����ϵ����
		
		DataInputStream din = new DataInputStream(fin);
		int count = 0;
		while(true)
		{  try{
			double i = din.readDouble();		//��din��һ������ȡ�������أ���read()ͬ
			System.out.println(i+" ");
			count++;
			}catch(EOFException ioe){
				break;							//���꣬�׳�EOFException
												//������쳣����breakǿ�ƽ���ѭ��
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
	private void write2File(double[] buffer) throws IOException {//����ʱ buffer�����ͼ������ʾ��Ҫ�У�����ʱ����
		
		FileOutputStream fout = new FileOutputStream(this.fileName);	//��buffer���ֽ�д���ļ�
		//Elephant  aElephant = new Elephant("̩������")
																		//FileoutputStream()д���ļ���
																		//fout �ļ��ֽ�������Ķ���
		DataOutputStream dout = new DataOutputStream(fout);				//������Ƥ���ǣ�����������ֽ�ת��Ϊ������������
		for(int i=0; i<buffer.length;i++){
			dout.writeDouble(buffer[i]);							//writeDoubleֻ��һ��дһ��double���͵���
		}	
																		//дbuffer�� fout
		dout.close();																//22-10-12-35ʹ��
		fout.close();													//fileName��Ӧ ByteFile.dat
		System.out.println("�ɹ�д���ļ���"+this.fileName);
	}

}
