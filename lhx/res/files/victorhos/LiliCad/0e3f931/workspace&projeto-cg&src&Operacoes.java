/*
-----------------------------------------------------------------------------
--
--  Class: Operacoes
--
--  
--
--  Date    Sign		History
--  ------	----		--------------------------------------------------------
--	141113	Lilian		Formatação de números decimais
--	131113	Lilian		Ajustes nos métodos de cisalhamento e rotação
--  101113	Lilian   	Criação
-----------------------------------------------------------------------------
*/

import java.lang.*;
import javax.swing.*;

class Operacoes 
{
	//Variável que será usada como parametro para criação da matriz identidade
	public static int tamanho = 3; //***IMPORTANTE - se necessário criar uma matriz de tamanho maior, alterar o valor desta variável
	
	 //6.1 Cálculo da área do polígono
     
     //6.2 Identificação dos vértices côncavos e convexos
     
     //6.3 Transformação de escala, dado o parâmetro necessário - START
     public static double[][] escala(int valorEscala, double matrizTransformacao[][])
     {
     	//criando a matriz para a escala
     	double matrizEscala[][] = new double[tamanho][tamanho];    	
     		     	
     	//criando a matriz para escala
     	matrizEscala = Calculos.montaMatrizIdentidade(tamanho);
     	     	
		//modificando a matriz identidade para ser uma matriz de operação de escala
     	matrizEscala[0][0] = valorEscala;
     	matrizEscala[1][1] = valorEscala;
     	    		
     	//efetuando a multiplicação da matriz da escala com a matriz recebida
     	matrizTransformacao = Calculos.multiplicaMatriz (matrizEscala, matrizTransformacao);     		
     	
     	//retornar a matriz de transformação com a operação de escala	
     	return matrizTransformacao;
     } 
	//6.3 Transformação de escala, dado o parâmetro necessário - END
     
     //6.3 Transformação de espelhamento, fornecida(s) a(s) direção(ões) - START
     public static double[][] espelhamento(boolean direcaoX, boolean direcaoY, double matrizTransformacao[][])
     {     	
     	//criando a matriz para espelhamento
     	double matrizEspelhamento[][] = new double[tamanho][tamanho];    	
     	
     	//montando a matriz para espelhamento
     	matrizEspelhamento = Calculos.montaMatrizIdentidade(tamanho);
     	
        //modificando a matriz identidade para ser uma matriz de operação de espelhamento
       //espelhamento em x
     	if (direcaoX && !direcaoY)
     	{
     		matrizEspelhamento[0][0] = -1.0;
     	}
     	else
     		//espelhamento em y
     		if (!direcaoX && direcaoY)
     		{
     			matrizEspelhamento[1][1] = -1.0;
     		}
     		//espelhamento em x e y
     		else
     		{
     			matrizEspelhamento[0][0] = -1.0;
     			matrizEspelhamento[1][1] = -1.0;
     		}	
     	
     	//efetuando a multiplicação da matriz de espelhamento com a matriz recebida	
     	matrizTransformacao = Calculos.multiplicaMatriz (matrizEspelhamento, matrizTransformacao);     		
     	
     	//retornar a matriz de transformação com a operação de escala	
     	return matrizTransformacao;     			
     }        
     //6.3 Transformação de espelhamento, fornecida(s) a(s) direção(ões) - END
	 
     //6.4 Transformação de translação, dados os deslocamentos em x e em y - START
     public static double[][] translacao(int valorTranslacaoX, int valorTranslacaoY, double matrizTransformacao[][])
     {
     	//criando a matriz para translacao
     	double matrizTranslacao[][] = new double[tamanho][tamanho];
     	
     	//montando a matriz para translacao
     	matrizTranslacao = Calculos.montaMatrizIdentidade(tamanho);
     	
     	//modificando a matriz identidade para ser uma matriz de operação de translação
     	matrizTranslacao[0][2] = valorTranslacaoX;
     	matrizTranslacao[1][2] = valorTranslacaoY;
     	
     	//efetuando a multiplicação da matriz de translação com a matriz recebida
     	matrizTransformacao = Calculos.multiplicaMatriz (matrizTranslacao, matrizTransformacao);     	
     	
     	//retornar a matriz de transformação com a operação de escala	
     	return matrizTransformacao;
     }
     //6.4 Transformação de translação, dados os deslocamentos em x e em y - END
	 
     //6.5 Transformação de cisalhamento, fornecida(s) a(s) direção(ões) e o(s) ângulo(s) - START
     public static double[][] cisalhamento(double anguloX, double anguloY, boolean direcaoX, boolean direcaoY, double matrizTransformacao[][])
     {
     	//criando a matriz para cisalhamento
     	double matrizCisalhamento[][] = new double [tamanho][tamanho];
		//DecimalFormat formato = new DecimalFormat("#.###"); //141113 - Lilian - Instanciando um objeto do DecimalFormat
	
     	//variáveis auxiliares para o cálculo da tangente dos ângulos
     	double tangenteX = 0;
     	double tangenteY = 0;
     	
     	//montando a matriz para translacao
     	matrizCisalhamento = Calculos.montaMatrizIdentidade(tamanho);
     	     	
     	//calculando a tangente do angulo
     	// 131113 - Lilian - START
		//tangenteX = Math.tan(anguloX);
		//141113 - Lilian - START
		tangenteX = Math.tan(Calculos.converteGraus(anguloX));		
		//141113 - Lilian - END
		System.out.println("Tangente ang X " + tangenteX);//
     	//tangenteY = Math.tan(anguloY);
		tangenteY = Math.tan(Calculos.converteGraus(anguloY));
		System.out.println("Tangente ang Y " + tangenteY);//
		// 131113 - Lilian - END
		
     	//cisalhamento em x
     	if (direcaoX && !direcaoY)
     	{
     		matrizCisalhamento[0][0] = tangenteX;
     	}
     	else
     		//cisalhamento em y
     		if (!direcaoX && direcaoY)
     		{
     			matrizCisalhamento[1][1] = tangenteY;
     		}
     		//cisalhamento em x e y
     		else
     		{
     			matrizCisalhamento[0][0] = tangenteX;
     			matrizCisalhamento[1][1] = tangenteY;
     		}
     	
     	//efetuando a multiplicação da matriz de cisalhamento com a matriz recebida
     	matrizTransformacao = Calculos.multiplicaMatriz (matrizCisalhamento, matrizTransformacao);     	
     	
     	return matrizTransformacao;
     }
	 //6.5 Transformação de cisalhamento, fornecida(s) a(s) direção(ões) e o(s) ângulo(s) - END

     //6.6.Transformação de rotação, dadas  as coordenadas do ponto em torno do qual o polígono será rotacionado e o ângulo - START
     public static double[][] rotacao(double anguloRotacao, double matrizTransformacao[][])
     {
     	//criando a matriz para rotacao
     	double matrizRotacao[][] = new double [tamanho][tamanho];
     	
     	//variáveis auxiliares para o cálculo do seno e cosseno do ângulo
     	double seno = 0;
     	double cosseno = 0;
     	
     	//montando a matriz para translacao
     	matrizRotacao = Calculos.montaMatrizIdentidade(tamanho);
     	
     	//calculando o seno e o cosseno do ângulo
		//131113 - Lilian - START
     	//seno = Math.sin(anguloRotacao);
		seno = Math.sin(Calculos.converteGraus(anguloRotacao));
     	System.out.println(seno);//
     	//cosseno = Math.cos(anguloRotacao);
     	cosseno = Math.cos(Calculos.converteGraus(anguloRotacao));
		System.out.println(cosseno);//
     	//131113 - Lilian - END
		
     	matrizRotacao[0][0] = cosseno;
     	matrizRotacao[0][1] = (- seno);
     	matrizRotacao[1][0] = seno;
     	matrizRotacao[1][1] = cosseno;
     	
     	Calculos.exibeMatriz(matrizRotacao);
     	
     	//efetuando a multiplicação da matriz de rotação com a matriz recebida
     	matrizTransformacao = Calculos.multiplicaMatriz (matrizRotacao, matrizTransformacao);     	     	
 
 		return matrizTransformacao; 
     }
	 //6.6.Transformação de rotação, dadas  as coordenadas do ponto em torno do qual o polígono será rotacionado e o ângulo - END
}	
