package ������.��2;

public class SwitchExample { //��һ���������ж��������ĸ��ȼ���

	private int grade;

	 
	public void setGrade(int grade) {
		this.grade = grade;
	}
	
	public int getGrade() {
		return grade;
	}

	public void grade(){
		switch(grade/10)  //if�ı��֣�if�����ں��������еĽ���ǲ�ȷ�������Σ�switch������ȷ�����Σ���������
		                  //һ�����������������Σ���С����ģ����ʺϣ����޵Ĳ��ʺϣ�char����Ҳ��
		                  //char��������ȥ���ַ���ʵ���ڵײ������������
		                  //ע��switch����䣬һ��Ҫ���ڷ�����
		{
		case 6: System.out.println(this.getGrade()+"�����ڼ���");
		                                         //switch��case�ɶԳ��֣�ð�ŵ�����
		                                         //ÿ��case��Ҫ��break����������case����һ�ֺ����߼�
		break;
		case 7:
		case 8: System.out.println(this.getGrade()+"����������");
		break;
		case 9: System.out.println(this.getGrade()+"����������");
		break;
		case 10: System.out.println(this.getGrade()+"����������");
		break;
		default:  System.out.println(this.getGrade()+"�����ڲ�����");//�൱��if�����һ��else������
		                                                         //��Ϊ�ǳ��ڣ�����ǰ����һcase����
		break;
		}
			
	}
	
}
