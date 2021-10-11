package br.com.ibta.tcc.main;

import java.awt.Color;

public class Pixel {

	private Integer pixel;
	private Color color;

	public Pixel(Integer p) {

		this.pixel = p;
		this.color = new Color(p);

	}

	public Color getColor() {
		return color;
	}

	public void setColor(Color color) {
		this.color = color;
	}

	public Integer getPixel() {
		return pixel;
	}

	public void setPixel(Integer pixel) {
		this.pixel = pixel;
	}

}
