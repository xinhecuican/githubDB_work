package ��ʮ��.��2;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

//���ڴ����������һ���ֽ��͵����飬����д��һ���ļ��У�Ȼ���ڶ�ȡ���ļ������ļ�������ʾ��console�С�

public class FileStream {

	private String fileName;
	public FileStream(String fileName){
		
		this.fileName = fileName;
	}
	public static void main(String[] args) throws IOException {
		
		byte buffer[] = new byte[100];			//16-17-19-23-34-41
		for(int i=0;i<buffer.length;i++){		//��������,���ڴ�������
			
			buffer[i] = (byte)(Math.random()*100);//ͨ�������������һ��byte���͵���������������
		}
		
		FileStream fileStream = new FileStream("ByteFile.dat");
		fileStream.write2File(buffer);	//���ڴ������ɵ��ֽ������ɵ��ֽ�����д��һ����ByteFile.dat���ļ�
										//FileStream��ʾ
		fileStream.readFileContent();	//����

	}
	private void readFileContent() throws IOException {
		
		FileInputStream fin = new FileInputStream(this.fileName);		//�������������󣬲��Һ��ļ�����ϵ����
		byte[] buffer1 = new byte[20];
		int count = 0;
		do{
			count = fin.read(buffer1);
			for(int i=0; i<count;i++){
				System.out.println(buffer1+" ");
			}
		}while(count != -1);
		
		fin.close();
	}
	private void write2File(byte[] buffer) throws IOException {//����ʱ buffer�����ͼ������ʾ��Ҫ�У�����ʱ����
		
		FileOutputStream fout = new FileOutputStream(this.fileName);	//��buffer���ֽ�д���ļ�
		//Elephant  aElephant = new Elephant("̩������")
																		//FileoutputStream()д���ļ���
																		//fout �ļ��ֽ�������Ķ���
		fout.write(buffer);												//дbuffer�� fout
																		//22-10-12-35ʹ��
		fout.close();													//fileName��Ӧ ByteFile.dat
		System.out.println("�ɹ�д���ļ���"+this.fileName);
	}

}
