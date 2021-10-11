

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;

import org.apache.commons.lang3.StringUtils;

public class GeraPontos {
	
	private static PrintWriter pw;
	
	private static String arquivo = "C:/lilicad/pontos.txt";
	
	//Grava as linhas do arquivo
	public static void GravarReg(String linha) throws IOException {

		pw = new PrintWriter(new FileOutputStream(arquivo, true), true);
		pw.print(linha);
		pw.write(13);
		pw.write(10);
		pw.close();

	}
	
	//Grava pontos em arquivo
	public static void GravaPontos(double mat[][]) throws IOException {
		
		String nomeDoc = (arquivo);
		File doc = new File(nomeDoc);
		if (doc.exists()) {
			doc.delete();
		}
		int index = 0;
		while(mat[0].length > index){
			GravarReg(mat[0][index] + "/" + mat[1][index]);
			index++;
		}		
		
	}
		
	
	//Classe que lê os arquivos
	public double[][] RecebePontos(String nome) {
		
		int tam=0;

		try {
			//Conta as linhas do arquivo
			FileReader arqTam = new FileReader(nome);
			BufferedReader lerArqTam = new BufferedReader(arqTam);
			String linhaTam = lerArqTam.readLine();
			while (linhaTam != null) {
				tam++;	
				linhaTam = lerArqTam.readLine();
			}
			double matriz [][]= new double[3][tam];
			
			FileReader arq = new FileReader(nome);
			
			BufferedReader lerArq = new BufferedReader(arq);

			String linha = lerArq.readLine();
			
			String tempX, tempY;

			int index = 0;
			int numLinha = 0;

			//lê o conteúdo das linhas
			while (linha != null) {
				index = linha.indexOf("/");
				tempX = linha.substring(0, index);
				tempY = linha.substring(index+1,linha.length());
				linha = lerArq.readLine();
				System.out.println("X " + tempX + " Y " + tempY + "1");
				matriz[0][numLinha] = Double.parseDouble(tempX);
				matriz[1][numLinha] = Double.parseDouble(tempY);
				matriz[2][numLinha] = 1;
				numLinha++;
			}

			//GravarReg(linha);
			//linha = lerArq.readLine();

			arq.close();
			return matriz;

		} catch (IOException e) {

			System.err.printf("Erro na abertura do arquivo: %s.\n",

			e.getMessage());

		}
		return null;

	
	}
	
}
