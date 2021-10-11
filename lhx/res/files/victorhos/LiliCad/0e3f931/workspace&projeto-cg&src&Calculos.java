/*
-----------------------------------------------------------------------------
--
--  Class: Calculos
--
--  
--
--  Date    Sign		History
--  ------	----		--------------------------------------------------------
--	131113	Lilian		Inclusão do método converteGraus
--  101113	Lucas 		Criação
-----------------------------------------------------------------------------
*/

class Calculos 
{	
	//101113 - Lucas - Criação dos métodos usados para os cálculos - START
	//Método que efetua a multiplicação entre as matrizes recebidas - START
	//***IMPORTANTE - A matriz de transformação deve ser passada em primeiro na chamada desse método***//
	public static double [][] multiplicaMatriz(	double matrizGeral[][], double matrizForm[][])
	{
		//retorna uma matriz com o resultado da multiplicação das matrizes
		
		int y = 0;//controle de movimentação das matrizes multiplicadas
		int  controleY = 0;//controle da posição da matriz resultado e movimentação das colunas na matrizForm
		int linhaMatriz = matrizForm.length,colunaMatriz=matrizForm[0].length; //tamanho da matriz
		int tamanhoTotalMatriz = linhaMatriz*colunaMatriz;//tamanho total X*Y
		double mat_aux[][] = new double[linhaMatriz][colunaMatriz];//armazena o resultado da multiplicação
				
		for(int cont1 = 0; cont1 < linhaMatriz; cont1++)
		{			
			controleY = 0;
			y = 0;
			for(int cont2 = 0; cont2 < tamanhoTotalMatriz; cont2++)
			{	
				if(y == linhaMatriz)
				{
					y = 0;
					controleY++;
				}
								
				mat_aux[cont1][controleY] = mat_aux[cont1][controleY] + (matrizGeral[cont1][y] * matrizForm[y][controleY]);						
				y++;
			}			
		}	
		return mat_aux;		
	}
	//Método que efetua a multiplicação entre as matrizes recebidas - END
	
	//Método que exibe a Matriz recebida - START
	public static void exibeMatriz(double m1[][])
	{
		for(int x = 0; x < m1.length;x++)
		{
			for(int y =0;y<m1[0].length;y++)
			{
				//System.out.println(m1[x][y]+" x="+x+" y="+y);
				System.out.print(m1[x][y]+ " ");
			}
		System.out.println();
		}
		System.out.println("------");
	}
	//Método que exibe a Matriz recebida - END
	
	//Método responsável por montar a matriz identidade - START
	public static double[][] montaMatrizIdentidade(int tamanhoMatriz)
	{
		double matrizIdentidade[][] = new double [tamanhoMatriz][tamanhoMatriz];
		
		for(int i = 0; i < tamanhoMatriz; i++)
		{
			for(int j = 0; j < tamanhoMatriz; j++)
			{
				if(i == j)
				{
					matrizIdentidade[i][j]=1;
				}
				else
				{
					matrizIdentidade[i][j]=0;
				}
			}	
		}
		return matrizIdentidade;
	}
	//Método responsável por montar a matriz identidade - END
	//101113 - Lucas - Criação dos métodos usados para os cálculos - END
	
	// 131113 - Lilian - Método que será responsável por converter graus em radianos - START
	public static double converteGraus(double graus)
	{
		double anguloRadianos = (2 * Math.PI * graus) / 360;
		return anguloRadianos;
	}
	// 131113 - Lilian - Método que será responsável por converter graus em radianos - END
}
