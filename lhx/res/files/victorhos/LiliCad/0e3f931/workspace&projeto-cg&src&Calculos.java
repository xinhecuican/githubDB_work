/*
-----------------------------------------------------------------------------
--
--  Class: Calculos
--
--  
--
--  Date    Sign		History
--  ------	----		--------------------------------------------------------
--	131113	Lilian		Inclus�o do m�todo converteGraus
--  101113	Lucas 		Cria��o
-----------------------------------------------------------------------------
*/

class Calculos 
{	
	//101113 - Lucas - Cria��o dos m�todos usados para os c�lculos - START
	//M�todo que efetua a multiplica��o entre as matrizes recebidas - START
	//***IMPORTANTE - A matriz de transforma��o deve ser passada em primeiro na chamada desse m�todo***//
	public static double [][] multiplicaMatriz(	double matrizGeral[][], double matrizForm[][])
	{
		//retorna uma matriz com o resultado da multiplica��o das matrizes
		
		int y = 0;//controle de movimenta��o das matrizes multiplicadas
		int  controleY = 0;//controle da posi��o da matriz resultado e movimenta��o das colunas na matrizForm
		int linhaMatriz = matrizForm.length,colunaMatriz=matrizForm[0].length; //tamanho da matriz
		int tamanhoTotalMatriz = linhaMatriz*colunaMatriz;//tamanho total X*Y
		double mat_aux[][] = new double[linhaMatriz][colunaMatriz];//armazena o resultado da multiplica��o
				
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
	//M�todo que efetua a multiplica��o entre as matrizes recebidas - END
	
	//M�todo que exibe a Matriz recebida - START
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
	//M�todo que exibe a Matriz recebida - END
	
	//M�todo respons�vel por montar a matriz identidade - START
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
	//M�todo respons�vel por montar a matriz identidade - END
	//101113 - Lucas - Cria��o dos m�todos usados para os c�lculos - END
	
	// 131113 - Lilian - M�todo que ser� respons�vel por converter graus em radianos - START
	public static double converteGraus(double graus)
	{
		double anguloRadianos = (2 * Math.PI * graus) / 360;
		return anguloRadianos;
	}
	// 131113 - Lilian - M�todo que ser� respons�vel por converter graus em radianos - END
}
