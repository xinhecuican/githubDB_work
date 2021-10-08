package µÚÆßÕÂ.Àý3;

public class MyException extends Exception {

	public MyException(String message, Throwable cause){
		
		super(message,cause);
	}
	
	public static void myE() throws MyException{
		
		try{
			int a =10/0;
		}catch(ArithmeticException e){
			
			throw new MyException(e.getMessage(),e.getCause());
		}
	}
	
	public static void main(String[] args) {
		
		try{
			MyException.myE();
		}catch(MyException e){
			System.out.println(e);
		}
	}

}
