package ������.��4;

public class Action {
	
//	��Ա����
    private Animal aAnimal;
    private Box aBox;
    private Openning aOpenning;
    private Closing  aClosing;
    private String name;
    
   // ���췽��
	public Action(String name) {
		super();
		this.name = name;
	}

//	��ȡ��������س�Ա����
	public String getName() {
		return name;
	}


	public void setName(String name) {
		this.name = name;
	}
	
	public Animal getaAnimal() {
		return aAnimal;
	}


	public void setaAnimal(Animal aAnimal) {
		this.aAnimal = aAnimal;
	}


	public Box getaBox() {
		return aBox;
	}


	public void setaBox(Box aBox) {
		this.aBox = aBox;
	}




// action����
	public void action(){
		System.out.println(this.name);
		aOpenning.controlOpen();
		aBox.open();
		aAnimal.enter();
		aAnimal.print();//aAnimal ��һ�������Ǵ���,����������ת�Ͷ���,��ת�Ͷ�����õķ���
						//����ķ���,������������û�������������ô�죿�̳�����,���ü̳е�
						//����ķ�������� print()�е�num�Ǹ����num ���������Ҳ�ж���
							//print������ô��animal��Ϊ��ת�Ͷ�����õ����������
						//Elephant ��print���� ���print()�е�num����Elephant
		                //��num�ˣ�������Animal�е�num��,Ҳ�͵ò������м���������.ֻ�ܵõ����������ˡ�
		    			// ��ת�Ͷ�����õ�ͬ���ĳ�Ա������ͬ����static�����Ǹ���ĳ�Ա�����ͷ���
						//��ת�Ͷ�����õ�ͬ��ʵ��������û��static����)�����õ�������ķ���
						//��ת�Ͷ�����õ�ʵ�������¹�����û�У������е��õ��Ǹ���ķ���
						//���������ĳ�Ա�������Ǹ���ġ�
		aClosing.controlClose();
		aBox.close();
	}

	
//	
	public Openning getaOpenning() {
		return aOpenning;
	}

	public void setaOpenning(Openning aOpenning) {
		this.aOpenning = aOpenning;
	}

	public Closing getaClosing() {
		return aClosing;
	}

	public void setaClosing(Closing aClosing) {
		this.aClosing = aClosing;
	}
	
	
    
    
    
}
