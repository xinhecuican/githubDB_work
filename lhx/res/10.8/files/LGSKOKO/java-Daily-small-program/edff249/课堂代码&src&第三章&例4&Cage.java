package ������.��4;

public class Cage extends Box {
	
	public  Cage(String name) {    //�������еĹ��췽��������ҲҪ��
		super(name);             //super����Animal����˼
		
	}


	public void open() {
		System.out.println(this.name+"�Ŵ�");

	}

	public void close() {
		System.out.println(this.name+"�Źر�");

	}

}
