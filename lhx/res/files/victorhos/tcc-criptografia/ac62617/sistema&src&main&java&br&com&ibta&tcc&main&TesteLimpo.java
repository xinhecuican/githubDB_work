package br.com.ibta.tcc.main;

import java.util.Random;

import br.com.ibta.RSA.EngineRSA;
import br.com.ibta.RSA.KeyRSA;
import br.com.ibta.RSA.RSA;

public class TesteLimpo {

	private static int KEY_LENGTH = 64;

	public static void main(String[] args) {

		KeyRSA keys[];

		/* Criando chaves */
		keys = RSA.createKeys(KEY_LENGTH);
		Random rd = new Random(System.currentTimeMillis());
		EngineRSA eng = EngineRSA.create(keys[0], keys[1]);
		
		/* Carregando imagem */
		Image img = new Image("/Users/victor/Lenna.png", "/Users/victor/Lenna2.png");
		img.loadImage();
		
		/* Fazendo critogrfia da imagem*/
		CriptoImagem ci = new CriptoImagem();
		
		ci.criptografarImagem(img, eng);
		
		
	}

}
