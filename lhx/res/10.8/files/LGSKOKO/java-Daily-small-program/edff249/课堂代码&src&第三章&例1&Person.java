package ������.��1;

public class Person {  // �˵����Ա�������������û�й�ϵ�����Բ������Ա������ֻ�����Ա����

	private String name;
	
	
	public Person(String name) {
	super();
	this.name = name;
}
	
//	public String getName() {
//		return name;
//	}
//
//	public void setName(String name) {
//		this.name = name;
//	}

	public void pull() { //ƽ������˵�˿��Ź��ţ���ô���ź͹��Ŷ����ڱ��仹���˵����У�
		//ԭ�򣺿��Ź����õ��ĳߴ������ĸ��࣬�Ͷ������Ǹ����С��������ڱ��䡣���ԣ����Ź��ŵķ��������ڱ����У���������������С�
		//�ٱ��磬���ﳵ������ֻ�ֱʣ��ֱʵ���������+1�����Ǹֱʵ����಻��+1��compareID��������������ڻ���������У�
		//public class Goods{public void compareID��String ID��{if��this.ID==ID��}}
        //�����ǹ��ﳵ������С���Ϊ��������ID�š���Ա�����ͳ�Ա������һ�������ֵܣ�ͬʱ����һ����
		//��Ϊ�����Ǵ�������ġ���������A�࣬��Ա��������B�࣬�޷�������
		System.out.println(this.name+"����");

	}
public void push(){
	
	System.out.println(this.name+"����");
}
}
