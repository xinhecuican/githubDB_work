package ������.��1; //��ҵ������Computer��ͶӰ��Projector����Ļscreen��Action��Client��
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
		Action aAction;
		Elephant taiguoxiang;
		IceBox xinfeibingxiang;
		Person lurenjia;
		
		                    
	    aAction = new Action();
	    //����һ��̩������·�˼ף��·ɱ���
	    taiguoxiang = new Elephant("̩����");  //new���������Ѿ�ǣ���������ڴ����Ѹ�����ռ䣬Ĭ��ֵnull����
	                                     //���û�д��εĹ��췽����javaĬ�ϸ��޲εĹ��췽����Elephant����
	                                     //֮ǰ���ǲ�û�ж��壬Ҳû�г�����һ�������˴��ι��캯����ϵͳ����
	                                     //Ĭ�ϸ������޲ι��캯�����˴����췽�����޲ξͻ����
	    xinfeibingxiang = new IceBox("�·ɱ���");      //�����ѷź�
	    lurenjia = new Person("·�˼�");      //�������ŵ���������׼��
	                                //���϶�����ʵ�У������ڴ����Ѵ��ڵĻ������Ķ��󣬵��;籾�еĶ���û�й���
	                                //Client��֮����඼�Ǿ籾����ͼ���滮ͼ���ƻ��飬����ģ���������
		                            //Client����Ŀǰ�����г�Ա������Action�е���Ȼͬ���ĳ�Ա��������һ����
	                                //˭����Client���г�Ա������Action���г�Ա����֮��Ĺ�ϵ
	                                //�ĸ���ӵ����Щ��Ա���������Ķ���͵���set����
     	 
	aAction.setaElephant(taiguoxiang)	;//˫��ѡ��setaElephant(),���һ���open declaration
	                                 //�����Զ�ת��Action���б������Ķ���
	aAction.setaIceBox(xinfeibingxiang);
	aAction.setaPerson(lurenjia);
	
	taiguoxiang.setaIceBox(xinfeibingxiang);
	
	taiguoxiang.setWidth(1.0);
	taiguoxiang.setHeight(1.8);
	xinfeibingxiang.setHeight(2.0);
	xinfeibingxiang.setWidth(1.5);
	aAction.action();
	
	}                        
	
}
