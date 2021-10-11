package ตฺถþีย.ภý6;

public class ShortCircuit {
	
public static void shortc(){
		
		int n=3;
		int m=4;
		System.out.println("compare result is "+((n>m)&&(++n)>m));
		System.out.println("n is "+n);
		System.out.println("compare result is "+((n<m)&&(++n)>m));
		System.out.println("n is "+n);
	}
	public static void main(String[] args) {
		ShortCircuit.shortc();

	}
}
