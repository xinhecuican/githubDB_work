package ������.��3;

public abstract class Animal {
	
	protected Box aBox;
	protected String name;
	
	protected double width,height;   //������еĳ�Ա���������������
	 
	

//	public String getName() {
//		return name;
//	}
//
//	public void setName(String name) {
//		this.name = name;
//	}
	public void hhh(){
		System.out.println("hhh");
	}

	
	

		public Box getaBox() {
			return aBox;
		}

		public void setaBox(Box aBox) {
			this.aBox = aBox;
		}

		

		public void setWidth(double width) {
			this.width = width;
		}

		

		public void setHeight(double height) {
			this.height = height;
		}
		
		public double getWidth() {
			return width;
		}
		
		public double getHeight() {
			return height;
		}

		public Animal(String name) {
			super();
			this.name = name;
		}
		public abstract void enter();  //�������еķ�������ǳ��󷽷���û�У�����Χ�ķ�����
        //Ŀ������Ӧǧ���򻯵������enter�����������enter����
        //���˲���abstract�����������ݲ�ͬ�⣬��������͸����enter������ͬ
	
		
}
