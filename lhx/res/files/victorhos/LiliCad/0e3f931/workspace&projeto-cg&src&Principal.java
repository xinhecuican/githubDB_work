/*
-----------------------------------------------------------------------------
--
--  Class: Principal
--
--  
--
--  Date    Sign		History
--  ------	----		--------------------------------------------------------
--  101113	Lilian   	Cria��o
-----------------------------------------------------------------------------
*/

class Principal 
{
	public static void main (String args[])
	{
		/*
		 *MATRIZ DE IDENTIDADE SER� USADA APENAS NA CRIA��O!
		 **/

		//Calculos.exibeMatriz(Calculos.montaMatrizIdentidade(3));
		//Operacoes.escala(3);
		
		double matrizTeste[][] = new double[3][3];
		matrizTeste[0][0] = 2;
		matrizTeste[0][1] = 4;
		matrizTeste[0][2] = 3;
		matrizTeste[1][0] = 2;
		matrizTeste[1][1] = 2;
		matrizTeste[1][2] = 4;
		matrizTeste[2][0] = 1;
		matrizTeste[2][1] = 1;
		matrizTeste[2][2] = 1;		
		
		
		Calculos.exibeMatriz(matrizTeste);
		//System.out.println("--");
		
		
		//ESCALA
		//Calculos.exibeMatriz(Operacoes.escala(3, matrizTeste));	
		
		//ESPELHAMENTO
		//Calculos.exibeMatriz(Operacoes.espelhamento(true, false, matrizTeste));
		//Calculos.exibeMatriz(Operacoes.espelhamento(false, true, matrizTeste));
		//Calculos.exibeMatriz(Operacoes.espelhamento(true, true, matrizTeste));
		
		//TRANSLA��O - ***IMPORTANTE - NA CHAMADA DESSE M�TODO CASO N�O HAJA TRANSL��O EM UM DOS PONTOS (X OU Y) PASSAR 0
		//Calculos.exibeMatriz(Operacoes.translacao(3, 2, matrizTeste));
		//Calculos.exibeMatriz(Operacoes.translacao(3, 0, matrizTeste));
		//Calculos.exibeMatriz(Operacoes.translacao(0, 2, matrizTeste));
		
		//**** VERIFICAR A FUN��O TANGENTE ******//
		//CISALHAMENTO - ***IMPORTANTE - NA CHAMADA DESSE M�TODO, CASO N�O HAJA CISALHAMENTO EM UM DOS PONTOS (X OU Y) PASSAR O ANGULO DESTE COMO ???
		//Calculos.exibeMatriz(Operacoes.cisalhamento(60, 60, false, false, matrizTeste));
		
		//ROTACAO
		//Calculos.exibeMatriz(Operacoes.rotacao(60, matrizTeste));

//******* D�VIDAS GERAIS ******//		
		//math.... ??
		//****usar? "\nArredondamento: " + Math.round(nr));
//******* D�VIDAS GERAIS ******//
		
	}
}
