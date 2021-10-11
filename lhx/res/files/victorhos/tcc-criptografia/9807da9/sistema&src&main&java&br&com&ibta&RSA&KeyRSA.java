package br.com.ibta.RSA;

import java.math.BigInteger;

/*
 * Classe que guardara as chaves
 */

public class KeyRSA {

	//base em que vão ser impressos os numeros	
	private static int BASE_PRINT = 2;
	private BigInteger k; //chave
	private BigInteger n; //modulo
	
	public static KeyRSA create (BigInteger k, BigInteger n)
	{
		return (new KeyRSA(k,n));
	}
	
	private KeyRSA (BigInteger k, BigInteger n)
	{
		this.k = k;
		this.n = n;
	}
	
	public String toString()
	{
		return "{[" + k.toString(KeyRSA.BASE_PRINT)+"]["+n.toString(KeyRSA.BASE_PRINT)+" ]}";
	}
	
	BigInteger getKey()
	{
		return k;
	}
	
	BigInteger getModulo()
	{
		return n;
	}
}
