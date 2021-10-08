package 第三章.例1;

public class Action { //过程剧本，里面要有三个实体，所以三个实体类的变量在这里都要声明
	                  //每个系统都包括实体类，以及将众多实体类用起来，描述过程的类
	                  

	private Elephant aElephant;//注意：这里都是对象型变量，不是对象
	private IceBox aIceBox;
	private Person aPerson;
	
	private String name;
	
	
	
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	

	public Elephant getaElephant() {
		return aElephant;
	}

	public void setaElephant(Elephant aElephant) {
		this.aElephant = aElephant;
	}

	public IceBox getaIceBox() {
		return aIceBox;
	}

	public void setaIceBox(IceBox aIceBox) {
		this.aIceBox = aIceBox;
	}

	public Person getaPerson() {
		return aPerson;
	}

	public void setaPerson(Person aPerson) {
		this.aPerson = aPerson;
	}
    public void action(){
		
		aPerson.pull();
		aIceBox.open();
		aElephant.enter();
		aPerson.push();
		aIceBox.close();
	}
}
