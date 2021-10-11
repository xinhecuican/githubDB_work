package br.com.ibta.tcc.main;

import java.math.BigInteger;

import br.com.ibta.RSA.EngineRSA;

public class CriptoImagem {

	public void criptografarImagem(Image img, EngineRSA eng) {

		for (int x = 0; x < img.getImage().getWidth(); x++) {
			for (int y = 0; y < img.getImage().getHeight(); y++) {
				
				BigInteger p, pixelCripto, t3;

				p = BigInteger.valueOf(img.getImage().getRGB(x, y) * (-1));
				pixelCripto = eng.encript(p);
				
				Pixel pixel = new Pixel();
				pixel.setPixelCriptografado(pixelCripto);
				System.out.println(pixel.getPixelCriptografadoBinary());
				
				pixel.getListColor();


			}
		}

	}

}
