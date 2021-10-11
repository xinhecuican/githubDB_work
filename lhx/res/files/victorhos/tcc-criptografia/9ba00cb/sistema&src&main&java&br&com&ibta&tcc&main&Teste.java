package br.com.ibta.tcc.main;

public class Teste {

	public static void main(String[] args) {

		Image img = new Image(
				"/Users/victor/image2px.jpg",
				"/Users/victor/image2pxx.jpg"
		);
		img.loadImage();
		img.transformImage();
		img.createNewImage();

	}

}
