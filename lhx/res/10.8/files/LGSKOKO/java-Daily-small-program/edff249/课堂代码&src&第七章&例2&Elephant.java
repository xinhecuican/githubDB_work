package ������.��2;

public class Elephant {

	private int age;
	
	public void setAge(int i) throws Exception{//throws��������쳣��
											   //throws����˼�����ﲻ���ˣ��������������쳣
											   //�����쳣������˦���ϼ������������ø÷����ķ���
											//throws��λ���ڷ��������з������ĺ��� {֮ǰ
		if(age>0 &&age<150)
			this.age = age;
		else
			throw new Exception("�Ƿ���������");	//throw ��������쳣����  Exception���쳣��
												//throw��λ���ڳ�����
	}
	
	public static void main(String[] args) throws Exception  {
														//mian����������throws���ͽ��쳣����������Ƹ������
														//ʵ���ϣ����е�throws���ǽ������Ƹ��������JVM)
														//?һ������£������޷�������쳣���Ƹ�JVM
														//�����ļ��Ҳ������������Ӳ��ϣ���Щ���ǳ���Ա�ڳ������޷������
														//������Ա�ڳ������ܹ�����Ĵ���Ӧ����try{}catch(Exception e){}									
		// TODO Auto-generated method stub
		Elephant aElephant = new Elephant();
		aElephant.setAge(250);
	}

}
