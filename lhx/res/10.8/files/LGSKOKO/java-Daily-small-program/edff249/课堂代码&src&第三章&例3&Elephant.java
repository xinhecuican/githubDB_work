package ������.��3;

public class Elephant extends Animal{//�ֳ��м������ʵ�壬�Ͷ��弸������࣬ÿ���඼Ҫ�����񣬶�Ҫ���£�����function��
	                     //���ݣ���Ļ�������£�����أ����ԾͲ�������
	
	public Elephant(String name) {    //���췽��������Ա�������������췽�����Ƿ������������ķ����������Ǵ�������
		super(name);                      //���ø��๹�췽����super�൱�ڸ��������������Object
		                              //Object��java�����ڸ��࣬super()�����๹�췽���б����ǵ�һ��
	    
	}
	//private double height;
	//private double width;//�������õ��ģ�����ģ�ĳ�������������ֵ,?����Ϊ�����Ǵ������ݵ�
	                             //�����೤���ȶ�֣�ʲô���򣬸�enter����û�й�ϵ�����Բ�����
	
/*	private String name;
	
	
	public Elephant(String name) {
	      super(name);
			this.name = name;						
								}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}

	public double getWidth() {
		return width;
	}
	public void setWidth(double width) { //�����Ĳ��������������������д��Σ�˫������������˭��Ϊ��ɫ��
		this.width = width;              //��������width��this.width = width;��=�����width
		                                 //this.width = width����=��ߵ�width�ǳ�Ա������width
    */  
	/*	public void set(double width, double height ){
			
			this.width = width;   //�������еľ��巽������������������޸ĵĻ�������ֱ�Ӽ̳С�
			                      //�̳о��Ǹ����еģ����಻�ö��壬�����Ŵ�
			this.height=height;   //enter�������Ǽ̳У��Ǹ��ǣ����������㺬�壬һ��������ľ���
		}                         //�������Ǹ���ĳ��󷽷���һ��������ľ��巽�����Ǹ��಻ͬ
		       */                   //ʵ�ֵķ���  
		
		
		//˫��this.width = �е�width���ῴ����������width�����ɫ
		//Ҫ��ĳ����ĳ�Ա������ֵ����Ҫ�������Ķ���������ĳ�Ա����set������˴���aElephant.setwidth(1.5)
		//���Ķ�ȥ���ã���main���������С�i=1���ָ������������ͱ�����ֵ�ķ������ٸ�����ĳ�Ա������ֵʱ�������á�
		
	//}
	
	
/*	public IceBox getaIceBox() {
		return aIceBox;
	}
	public void setaIceBox(IceBox aIceBox) {
		this.aIceBox = aIceBox;
	}
	*/
	//private IceBox aIceBox;     //�������������������������
    //��ֲ�������ͬ���ڷ������涨�壬���Դ�͸�κη����������κη�����
    //�ֲ������Ƿ����ڲ�����ģ����븳ֵ���˴νг�Ա����
    //��Ա�������Բ����ã���Ĭ��ֵ��int��0�� double��0.0
    //boolean�� false
    //˫��������width��������е�width�����ɫ�ģ�˵��������һ������
    
public void enter() {   //˫��������width���������width�����ɫ��˵������Ϊһ������
		
		if((this.width<aBox.width)&&(this.height<aBox.height))
		{	
		System.out.println(this.name+"���صؽ���");
        System.out.println(this.width);   //sysout+alt+/  �ͳ�����
        System.out.println(this.height);
        
        System.out.println(aBox.width);   //�˴�����������·ɱ��䡱���������aIceBox������ڴ�����
        System.out.println(aBox.height);
		}
    //System.out.println(aIceBox); //�˴�����������·ɱ��䡱������Ҫ���aIcBox������ڴ�����
                                 //��������aIcBox��������ȡֵ�ǡ��·ɱ��䡱�����������xinfeibingxiang
                                   //�����ֵ�ǵ�����.��1.IceBox@15db9742
   
    }
    // ���������֡���Ա�����������������ֲ����������ã���Ա�����Ƕ�������ԡ���������Ϊ�������Ρ��ֲ������ڷ�������ʱʹ�á�
    //����λ�ã���Ա���������з���֮�⣬���������ڷ�������������У��ֲ������ڷ����С���ֵ����Ա���������븳ֵ����Ĭ��ֵ��
    //����������main���������д�����ֵ���ֲ������ڷ����б��븳ֵ��



}