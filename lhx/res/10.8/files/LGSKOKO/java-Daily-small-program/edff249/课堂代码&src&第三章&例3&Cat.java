package ������.��3;

public class Cat extends Animal{ 

	public Cat(String name) {     //�������еĹ��췽��������ҲҪ��
		super(name);             //super����Animal����˼
		
	}

	//private double width;  //Ĭ�ϴ�������int ���ͣ���Ϊdouble����
	//private double height;
    //private IceBox aIceBox; //Ĭ�ϴ�������Object���ͣ�Ҫ��ΪIceBox����
    //private String name;
    
	
	
	
	public void enter(){//�������ں�ɫ�������ϣ���ʾCreate field "width",
		
		 if((width<aBox.width)&&(height<aBox.height))
		 
			System.out.println(this.name+"������Ϣ�Ľ���");
		    System.out.println(this.width);
	        System.out.println(this.height);
	        
	        System.out.println(aBox.width); 
	        System.out.println(aBox.height);
	
	}
}
