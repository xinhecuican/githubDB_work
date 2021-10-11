package br.com.ibta.tcc.main;

public class Utils {

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

	public static String timer(long nanoSecs) {

		int minutes = (int) (nanoSecs / 60000000000.0);
		int seconds = (int) (nanoSecs / 1000000000.0) - (minutes * 60);
		int millisecs = (int) (((nanoSecs / 1000000000.0) - (seconds + minutes * 60)) * 1000);

		if (minutes == 0 && seconds == 0)
			return millisecs + "ms";
		else if (minutes == 0 && millisecs == 0)
			return seconds + "s";
		else if (seconds == 0 && millisecs == 0)
			return minutes + "min";
		else if (minutes == 0)
			return seconds + "s " + millisecs + "ms";
		else if (seconds == 0)
			return minutes + "min " + millisecs + "ms";
		else if (millisecs == 0)
			return minutes + "min " + seconds + "s";

		return minutes + "min " + seconds + "s " + millisecs + "ms";

		System.out.println(String.format("%-2d: %s", (i + 1), toString(endTime
				- startTime)));

	}

}
