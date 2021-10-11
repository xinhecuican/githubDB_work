package br.com.ibta.AES;

import java.util.Random;

import javax.crypto.spec.SecretKeySpec;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.Cipher;

/*
 * http://www.caelum.com.br/apostila-java-testes-xml-design-patterns/graficos-com-jfreechart/#7-5-exercicios-jfreechart
 * http://stackoverflow.com/questions/15554296/simple-java-aes-encrypt-decrypt-example
 * http://www.java2s.com/Code/Java/Security/EncryptionanddecryptionwithAESECBPKCS7Padding.htm
 * https://gist.githubusercontent.com/bricef/2436364/raw/2070f666ad990c57f3e08d49b3749da877d0b9e0/AES.java
 * http://www.code2learn.com/2011/06/encryption-and-decryption-of-data-using.html
 * http://karanbalkar.com/2014/02/tutorial-76-implement-aes-256-encryptiondecryption-using-java/
 */

public class AES {
	
	static String IV = "AAAAAAAAAAAAAAAA";
	static String plaintext = "10101010010101"; /* Note null padding */
	static String encryptionKey = "0123456789abcdef";
	public Random rd = new Random(System.currentTimeMillis());

	public static void main(String[] args) {
		try {

			System.out.println("plain:   " + plaintext);

			byte[] cipher = encrypt(plaintext, encryptionKey);

			System.out.print("cipher:  ");
			for (int i = 0; i < cipher.length; i++)
				System.out.print(new Integer(cipher[i]) + " ");
			System.out.println("");

			String decrypted = decrypt(cipher, encryptionKey);

			System.out.println("decrypt: " + decrypted);

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static byte[] encrypt(String plainText, String encryptionKey)
			throws Exception {
		Cipher cipher = Cipher.getInstance("AES/CBC/NoPadding", "SunJCE");
		SecretKeySpec key = new SecretKeySpec(encryptionKey.getBytes("UTF-8"),
				"AES");
		cipher.init(Cipher.ENCRYPT_MODE, key,
				new IvParameterSpec(IV.getBytes("UTF-8")));
		return cipher.doFinal(plainText.getBytes("UTF-8"));
	}

	public static String decrypt(byte[] cipherText, String encryptionKey)
			throws Exception {
		Cipher cipher = Cipher.getInstance("AES/CBC/NoPadding", "SunJCE");
		SecretKeySpec key = new SecretKeySpec(encryptionKey.getBytes("UTF-8"),
				"AES");
		cipher.init(Cipher.DECRYPT_MODE, key,
				new IvParameterSpec(IV.getBytes("UTF-8")));
		return new String(cipher.doFinal(cipherText), "UTF-8");
	}
}