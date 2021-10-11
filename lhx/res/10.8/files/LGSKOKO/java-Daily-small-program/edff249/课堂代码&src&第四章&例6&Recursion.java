package µÚËÄÕÂ.Àı6;

public class Recursion {
//	private int n;
//	
//	public void setN(int n)
//	{
//		this.n = n;
//	}
//	public int getN()
//	{
//		return n;
//	}
	
	public int f( int n)
	{
		if( n ==0){
			return 1;
		}else if( n == 1){
			System.out.println("1!=1");
			System.out.println("0!=1");
			return 1;
		}else{
			System.out.println(n +"!="+ n +"*"+(n-1)+"!");
			return f(n-1);
		}
	}
}
