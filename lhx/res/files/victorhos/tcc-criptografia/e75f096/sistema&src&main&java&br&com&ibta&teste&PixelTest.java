package br.com.ibta.teste;

import java.math.BigInteger;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import br.com.ibta.tcc.main.Pixel;

public class PixelTest {

	private static BigInteger PIXEL_CRIPTOGRAFADO = new BigInteger(
			"79502169818938959280363064769819069673");
	private Pixel pixel;

	@Before
	public void setUp() throws Exception {
		pixel = new Pixel();
		pixel.setPixelCriptografado(PIXEL_CRIPTOGRAFADO);

	}

	@After
	public void tearDown() throws Exception {
	}

	@Test
	public void testSetPixelCriptografado() {

		assertEquals(PIXEL_CRIPTOGRAFADO, pixel.getPixelCriptografado());

	}

	@Test
	public void testSetPixelCriptografadoBinary() {


		assertEquals(PIXEL_CRIPTOGRAFADO, pixel.getPixelCriptografado());

	}

}
