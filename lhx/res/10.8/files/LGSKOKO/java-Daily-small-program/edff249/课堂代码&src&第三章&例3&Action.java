package 第三章.例3;

public class Action { //过程剧本，里面要有三个实体，所以三个实体类的变量在这里都要声明
	                  //每个系统都包括实体类，以及将众多实体类用起来，描述过程的类
	                  //对修改关闭，对增加开放，注意，这里都是对象型变量，不是对象
	                  

	private Animal aAnimal;
	private Box aBox;
	private Person aPerson;
	private String name;
	
	 public Action(String name) {
			super();
			this.name = name;
		}

	public Animal getaAnimal() {
		return aAnimal;
	}

	public void setaAnimal(Animal aAnimal) {
		this.aAnimal = aAnimal;
	}

	
	
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	

	//public Elephant getaElephant() {
	//	return aElephant;
	//}

	//public void setaElephant(Elephant aElephant) {
	//	this.aElephant = aElephant;
	//}

	
	public Box getaBox() {
		return aBox;
	}

	public void setaBox(Box aBox) {
		this.aBox = aBox;
	}
    public Person getaPerson(){
		return aPerson;
	}
	
    public void setaPerson(Person aPerson) {
		this.aPerson = aPerson;
	}

	public void action(){
		System.out.println(this.getName());
		aPerson.pull();
		aBox.open();
		aAnimal.enter();    //面向抽象编程
		aPerson.push();
		aBox.close();
	}
}
