import java.io.File;
import java.io.IOException;


public class Menu {
	public static void main(String[] args) throws IOException {
				
		String arquivo = "C:\\lilicad\\pontos.txt";

		GeraPontos g = new GeraPontos();

		
		String nomeDoc = (arquivo);
		File doc = new File(nomeDoc);
		if (doc.exists()) {
			//doc.delete();
			g.RecebePontos(arquivo);
		}
		else{
			System.out.printf("O arquivo não existe ");
		}
		
		double matrizTeste[][] = new double[3][6];
		//Calculos.exibeMatriz(matrizTeste);
		
		matrizTeste[0][0] = 2;
		matrizTeste[1][0] = 8;
		matrizTeste[2][0] = 1;//
		
		matrizTeste[0][1] = 4;
		matrizTeste[1][1] = 1;
		matrizTeste[2][1] = 1;//
		
			
		matrizTeste[0][2] = 7;
		matrizTeste[1][2] = 4;
		matrizTeste[2][2] = 1;//
		
		matrizTeste[0][3] = 6;
		matrizTeste[1][3] = 8;
		matrizTeste[2][3] = 1;//
		
		matrizTeste[0][4] = 4;
		matrizTeste[1][4] = 4;
		matrizTeste[2][4] = 1;//
		
		matrizTeste[0][5] = 1;
		matrizTeste[1][5] = 4;
		matrizTeste[2][5] = 1;//
		
		g.GravaPontos(matrizTeste);
		
	}

}
