package ������.��4; //��ҵ������Computer��ͶӰ��Projector����Ļscreen��Action��Client��
                  //�����г�Ա����String data����Ա����processData����
                 //transferData(),ͶӰ���г�Ա����data����Ա����receiveData������projectData������
                  //��Ļ�еĳ�Ա����
                 //ͬ����data����Ա������displayData���� 

public class Client {             //��main����һ����������,��Ϊjava�������ڣ���ͻ��ˣ�����
	                              //main�����ⲻ��д���룬ֻ����main������д����
	                              //main����������֮һ�Ǹ����г�Ա������ֵ�����磬�û����������

	public static void main(String[] args){  //main+alt+/
		                                     //main�����о���ָ������ʵ�壬����������˭��
		
		                    //main�����ȵ��ù�����Action����������ø���ʵ����
		Action aAction;       //���������,һ��ģ���һ�ζ���ɸ���ʱ��������ɳ�����
	                         //��������Ժ�������޸�һ�������࣬��Ҫ�޸ģ�Ҫ���´���һ����
		Animal aAnimal;
		Box aBox;
		Openning aOpenning;       //���������̳�ԭ��Ҫ���޸ĵľ����ࡣ
		Closing aClosing;
		aAction = new Action("����һ");
		
	    //����һ��̩������·�˼ף��·ɱ���
	    aAnimal = new Elephant("̩����");  //��ת�ͣ��������͵Ķ��󸳸��˸������͵ı�����ע��˴��Ǳ�����
	                                     //Elephant aElephant = new Elephant();������ת��
	                                     //Animal aAnimal = new Animal();����Animal�ǳ������ͣ�
	                                     //�������ɶ���
	                                     //�������͵ı����������������͵�ֵ������
	                                     //����Ǹ��ף��ұ��Ƕ��ӣ�����Ǹ������ͱ���
	                                     //�ұ����������Ͷ���
	                                     //��̬���������ͱ������Ա����������Ķ���
	                                     //aAnimal�����Ǵ���è����
	    
	                                     //new���������Ѿ�ǣ���������ڴ����Ѹ�����ռ䣬Ĭ��ֵnull����
	                                     //���û�д��εĹ��췽����javaĬ�ϸ��޲εĹ��췽����Elephant����
	                                     //֮ǰ���ǲ�û�ж��壬Ҳû�г�����һ�������˴��ι��캯����ϵͳ����
	                                     //Ĭ�ϸ������޲ι��캯�����˴����췽�����޲ξͻ����
	    aBox = new IceBox("�·ɱ���");    //�����ѷź�
	     
	    aOpenning = new Person("·�˼�");  
	    aClosing = new Person("·�˼�");
     	 
	aAction.setaAnimal(aAnimal)	;//˫��ѡ��setaElephant(),���һ���open declaration
	                                 //�����Զ�ת��Action���б������Ķ���
	aAction.setaBox(aBox);
	aAction.setaOpenning(aOpenning);
	aAction.setaClosing(aClosing);

	
	aAnimal.setWidth(1.0);
	aAnimal.setHeight(1.8);
	aAnimal.setaBox(aBox);
	aBox.setWidth(1.5);
	aBox.setHeight(2.0);
	aAction.action();
	//��������è���磬����
	aAction = new Action("������");
	aAnimal = new Cat("��˹è");
	aBox = new Cage("����");
	aOpenning = new Electricity("��");
	//aOpenning.setName("��");
	
	aClosing = new Electricity("��");
	aAction.setaAnimal(aAnimal);
	aAction.setaBox(aBox);
	aAction.setaOpenning(aOpenning);
	aAction.setaClosing(aClosing);
	
	aAnimal.setWidth(0.1);
	aAnimal.setHeight(0.4);
	aAnimal.setaBox(aBox);
	aBox.setWidth(0.6);
	aBox.setHeight(0.6);
	aAction.action();
	}                        
	
}
