package ��ʮ��.��4;

class MyInt implements java.io.Serializable{
	
	private int value;
	private String number;
	private static int count = 0;
	
	public MyInt(int v){
		this.number =""+this.count;
		this.value = v;
		this.count++;
	}
	
	public String toString(){
		return "��" + this.number+"�����ֵ�ֵ�ǣ�"+this.value;
	}
}
