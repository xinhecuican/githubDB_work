package br.com.ibta.tcc.main;

public class Mensagem {

	public static String LINHA = "-----------------------------------";
	public static String IMG_SUCESSO = "Imagem carregada com sucesso";
	public static String IMG_FALHA = "Erro ao carregar imagem";
	public static String IMG_CRIADA = "Imagem criada em:";

	public static void imgSucesso() {

		System.out.println(LINHA);
		System.out.println(IMG_SUCESSO);
		System.out.println(LINHA);

	}

	public static void imgFalha() {

		System.out.println(LINHA);
		System.out.println(IMG_FALHA);
		System.out.println(LINHA);

	}

	public static void imgCriada(String path) {

		System.out.println(LINHA);
		System.out.println(IMG_CRIADA);
		System.out.println(path);
		System.out.println(LINHA);

	}

}
