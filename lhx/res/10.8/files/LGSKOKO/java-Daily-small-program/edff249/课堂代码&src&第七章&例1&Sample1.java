package ������.��1;

public class Sample1 {

	
	public static void tryError(){
		
		int[] a = new int[5];
		for(int i =0; i<a.length;i++){
			
			try{
			a[i] = 10/i;
			}catch(ArithmeticException e){
				e.printStackTrace();
			}catch(ArrayIndexOutOfBoundsException e){
				e.printStackTrace();
			}
			System.out.println("ѭ������i=" + i);
			System.out.println("�����߼�");
		}
		
	}
	
	//EXception inthread "main" java.lang.ArithmeticException: / by zero :��������
	//at ������.��1.Samole1.tryError(Sample1.java:11)			:�����Ĵ�����Դ��˫��
	//at������.��1.sample1.mai(Sample1.java:21��				��JVM��ʼ����
	//û���쳣����Ĵ��� һ�����ִ��� �������̱��� ����������� ֮��ĳ���Ҳ����ִ��
	
	//���쳣����Ĵ���󣬳���֮�������򽫴����׳���������֮����������
	public static void main(String[] args) {
		// TODO Auto-generated method stub
         Sample1.tryError();
	}

}
