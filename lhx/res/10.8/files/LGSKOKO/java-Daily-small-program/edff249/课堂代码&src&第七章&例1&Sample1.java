package 第七章.例1;

public class Sample1 {

	
	public static void tryError(){
		
		int[] a = new int[5];
		for(int i =0; i<a.length;i++){
			
			try{
			a[i] = 10/i;
			}catch(ArithmeticException e){
				e.printStackTrace();
			}catch(ArrayIndexOutOfBoundsException e){
				e.printStackTrace();
			}
			System.out.println("循环次数i=" + i);
			System.out.println("其他逻辑");
		}
		
	}
	
	//EXception inthread "main" java.lang.ArithmeticException: / by zero :错误类型
	//at 第七章.例1.Samole1.tryError(Sample1.java:11)			:真正的错误来源，双击
	//at第七章.例1.sample1.mai(Sample1.java:21）				：JVM初始调用
	//没有异常处理的代码 一旦出现错误 程序立刻崩溃 所有输出作废 之后的程序也不再执行
	
	//有异常处理的代码后，出错之处，程序将错误抛出，但正常之处照样进行
	public static void main(String[] args) {
		// TODO Auto-generated method stub
         Sample1.tryError();
	}

}
