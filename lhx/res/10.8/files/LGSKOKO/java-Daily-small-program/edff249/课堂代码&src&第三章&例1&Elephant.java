package ������.��1;

public class Elephant {//�ֳ��м������ʵ�壬�Ͷ��弸������࣬ÿ���඼Ҫ�����񣬶�Ҫ���£�����function��
	                     //���ݣ���Ļ�������£�����أ����ԾͲ�������
	
	
	private double width,height;//�������õ��ģ�����ģ�ĳ�������������ֵ,?����Ϊ�����Ǵ������ݵ�
	                             //�����೤���ȶ�֣�ʲô���򣬸�enter����û�й�ϵ�����Բ�����
	private String name;
	
	
	public Elephant(String name)
	{
		super();
		this.name = name;
								
	}
//	public String getName() {
//		return name;
//	}
//	public void setName(String name) {
//		this.name = name;
//	}
	





	public double getWidth() {
		return width;
	}
	public void setWidth(double width) { //�����Ĳ��������������������д��Σ�˫������������˭��Ϊ��ɫ��
		this.width = width;              //��������width��this.width = width;��=�����width
		                                 //this.width = width����=��ߵ�width�ǳ�Ա������width
		                                 //˫��this.width = �е�width���ῴ����������width�����ɫ
		//Ҫ��ĳ����ĳ�Ա������ֵ����Ҫ�������Ķ���������ĳ�Ա����set������˴���aElephant.setwidth(1.5)
		//���Ķ�ȥ���ã���main���������С�i=1���ָ������������ͱ�����ֵ�ķ������ٸ�����ĳ�Ա������ֵʱ�������á�
		
	}
	public double getHeight() {
		return height;
	}
	public void setHeight(double height) {
		this.height = height;
	}
	public IceBox getaIceBox() {
		return aIceBox;
	}
	public void setaIceBox(IceBox aIceBox) {
		this.aIceBox = aIceBox;
	}
	
	private IceBox aIceBox;     //�������������������������
    //��ֲ�������ͬ���ڷ������涨�壬���Դ�͸�κη����������κη�����
    //�ֲ������Ƿ����ڲ�����ģ����븳ֵ���˴νг�Ա����
    //��Ա�������Բ����ã���Ĭ��ֵ��int��0�� double��0.0
    //boolean�� false
    //˫��������width��������е�width�����ɫ�ģ�˵��������һ������
    public void enter(){
    if((width<aIceBox.width)&&(height<aIceBox.height))//���󣬳�Ա��������ʾ���������ֵ
                       //NullPointException��ָ����û��new

    System.out.println(this.name+"���صؽ���");
    System.out.println(this.width);  //sysout+alt+/
    System.out.println(this.height);

    System.out.println(aIceBox); //�˴�����������·ɱ��䡱������Ҫ���aIcBox������ڴ�����
                                 //��������aIcBox��������ȡֵ�ǡ��·ɱ��䡱�����������xinfeibingxiang
                                   //�����ֵ�ǵ�����.��1.IceBox@15db9742
    System.out.println(aIceBox.height); 
    System.out.println(aIceBox.width); 
    System.out.println(aIceBox.getName()); 
    }
    // ���������֡���Ա�����������������ֲ����������ã���Ա�����Ƕ�������ԡ���������Ϊ�������Ρ��ֲ������ڷ�������ʱʹ�á�
    //����λ�ã���Ա���������з���֮�⣬���������ڷ�������������У��ֲ������ڷ����С���ֵ����Ա���������븳ֵ����Ĭ��ֵ��
    //����������main���������д�����ֵ���ֲ������ڷ����б��븳ֵ��



}