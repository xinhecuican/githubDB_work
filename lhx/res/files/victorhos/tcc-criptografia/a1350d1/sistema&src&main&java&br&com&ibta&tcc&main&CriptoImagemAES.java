package br.com.ibta.tcc.main;

import java.awt.Color;

import br.com.ibta.AES.AES;

public class CriptoImagemAES {

	public static void main(String[] args) {

		byte[] cipher = null;
		int QTD_PIXEL = 16;
		byte[] descipher = new byte[QTD_PIXEL];

		Color[] listaColor = new Color[QTD_PIXEL];

		String color = Integer.toHexString(Integer.valueOf("16777000"));
		color = "0000000000" + color;

		System.out.println("color: " + color);

		AES aes = new AES("AAAAAAAAAAAAAAAA", "minhasenha123456");

		System.out.println("-----------------------------");
		System.out.println("       Criptografia");
		System.out.println("-----------------------------");

		try {
			cipher = aes.encrypt(color);
		} catch (Exception e) {
			e.getMessage();
			e.printStackTrace();
		}

		for (int i = 0; i < cipher.length; i++) {

			Integer number = new Integer(cipher[i]);

			System.out.println(number);

			if (number > 0) {
				number = number * (-1000);
			}

			listaColor[i] = new Color(number);

			// System.out.println(number + " / " + listaColor[i].getRGB());

		}

		System.out.println("-----------------------------");
		System.out.println("      Descriptografia");
		System.out.println("-----------------------------");

		for (int i = 0; i < listaColor.length; i++) {

			Integer number = listaColor[i].getRGB();

			if (number < -1000) {
				number = (number / 1000) * (-1);
			}

			descipher[i] = number.byteValue();
			System.out.println(number.byteValue());

		}
		
		try {
			System.out.println(aes.decrypt(descipher));
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

}
