package ��ʮ��.��5;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

//���ڴ����������һ��double�͵����飬����д��һ���ļ��У�Ȼ���ڴӸ��ļ���ȡ������������ȡ������ʾ��console�С�

public class CharactorStream {

	private String fileName;
	public CharactorStream(String fileName){
		
		this.fileName = fileName;
	}
	public static void main(String[] args) throws IOException {
		
		int buffer[] = new int[100];			//16-17-19-23-34-41
		for(int i=0;i<buffer.length;i++){		//��������,���ڴ�������
			
			buffer[i] = (int) (Math.random()*100);//ͨ�������������һ��byte���͵���������������
		}
		
		CharactorStream fileStream = new CharactorStream("CharFile.dat");
		fileStream.write2File(buffer);	//���ڴ������ɵ�double����д��һ����DoubleFile.dat���ļ�
										//FileStream��ʾ
		fileStream.readFileContent();	//����

	}
	private void readFileContent() throws IOException {
		
		
		FileReader fin = new FileReader(this.fileName);		//�������������󣬲��Һ��ļ�����ϵ����
		
		BufferedReader din = new BufferedReader(fin);
		

		int count = 0;
		String aline = null;
		do{
			aline = din.readLine();
			if(aline != null){
				System.out.println(aline);
			}
		}while(aline != null);							//�ַ����뻺���������ı�־�� aline =null
		System.out.println("���ζ���"+count+"��");
		System.out.println("���ζ���"+count+"��˫���ȸ�����");
		din.close();
		

		
		fin.close();
	}
	private void write2File(int[] buffer) throws IOException {//����ʱ buffer�����ͼ������ʾ��Ҫ�У�����ʱ����
		
		FileWriter fout = new FileWriter(this.fileName);	//��buffer���ַ���ʽд���ļ�
		//Elephant  aElephant = new Elephant("̩������")
																		//FileoutputStream()д���ļ���
																		//�ַ������
		BufferedWriter dout = new BufferedWriter(fout);				//�����ַ��������һ�ν������ַ�д��
		for(int i=0; i<buffer.length;i++){
			dout.write(buffer[i]);								//���ֽ�����writer(buffer������ͬ���ǿ��Զ�д����
														//��ͬ���ǵײ��д�ĸ�ʽ��ͬ��byte��char����
			if((i+1)%10 == 0) dout.newLine();
		}
																		//дbuffer�� fout
		dout.close();																//22-10-12-35ʹ��
		fout.close();													//fileName��Ӧ ByteFile.dat
		System.out.println("�ɹ�д���ļ���"+this.fileName);
	}

}
