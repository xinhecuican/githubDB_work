/*
-----------------------------------------------------------------------------
--
--  Class: Fila
--
--  
--
--  Date    Sign		History
--  ------	----		--------------------------------------------------------
--  101113	Lucas   	Criação
-----------------------------------------------------------------------------
*/

import javax.swing.JOptionPane;

public class Fila 
{
	//101113 - Lucas - Variáveis auxiliares
	int tamanho;
	int total=0;
	int inicio=0;
	int fim=0;
	Pontos vetorControle[];
	
	//101113 - Lucas - Construtor da fila
	Fila(int tamanho)
	{		
		this.tamanho=tamanho;
		vetorControle=new Pontos[this.tamanho];
	}
	
	//101113 - Lucas - Retorna se a fila esta vazia
	public boolean filavazia()
	{	
		if(this.total<=0)
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	
	//101113 - Lucas - Retorna se a  fila esta cheia
	public boolean filacheia()
	{	
		if(total>=tamanho)
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	
	//101113 - Lucas - Coloca o ponto capturado na fila
	public void enfileirar(double x, double y)
	{
		Pontos aux=new Pontos();
		aux.setX(x);
		aux.setY(y);
		if(filacheia()!=true)
		{
			vetorControle[fim]=aux;	
			this.fim=fim+1;
			if(fim>=tamanho)
			{
				fim=0;
			}
			total=total+1;
		}
		else
		{
			JOptionPane.showMessageDialog(null, "Fila Cheia, o dado nao foi inserido");
		}
	}
	
	//101113 - Lucas - Retira o ponto da lista
	public Pontos desenfileirar()
	{
		Pontos aux=new Pontos();
		if(filavazia()!=true)
		{
			aux.setX(vetorControle[inicio].getX());
			aux.setY(vetorControle[inicio].getY());
			inicio= inicio +1;
			if(inicio>=tamanho)
			{
				inicio=0;
			}		
			this.total=total-1;		
		}
		return aux;
	}
	
	//101113 - Lucas - Retorna o elemento da posição inicio
	public Pontos elementoinicio()
	{
		if(filavazia()!=true)
		{
			return vetorControle[inicio];
		}
		return null;	
	}
	
	//101113 - Lucas - Retorna o elemento na posição final
	public Pontos elementofinal()
	{
		if(filavazia()!=true)
		{
			return vetorControle[fim-1];
		}
		else
		{
			return null;
		}
	}
	
	//101113 - Lucas - Exibe a fila
	public void exibirfila()
	{ 
		int cont = 0, x = 0;
		cont = inicio;
		for(x = 1; x <= total; x++)
		{
			System.out.println("Posicao: "+x+"\nx= "+vetorControle[cont].getX()+" y= "+vetorControle[cont].getY());
			cont = cont+1;
			if(cont >= tamanho)
			{
				cont=0;	
			}
		}
	}
	
	//101113 - Lucas - Retorna o tamanho da fila
	public int totalFila()
	{
		return this.total;
	}

	//101113 - Lucas - Passa os dados da fila para a matriz
	public static double[][] filaParaMatriz(Fila fila)
	{
		/*
		//****IMPORTANTE****
			*Antes da chamada dessa função a matriz que vai receber o resultado deve ser inicializada da seguinte maneira:
			* double matriz = new double [3][fila.total]; 
		*/
		double matriz[][]=new double [3][fila.total];
		Pontos cordenadas=new Pontos();
		for(int cont1=0;cont1<matriz[0].length;cont1++)
		{
			cordenadas=fila.desenfileirar();
			matriz[0][cont1]=cordenadas.getX();
			matriz[1][cont1]=cordenadas.getY();
			matriz[2][cont1]=cordenadas.getpontoImaginario();
		}
		
		return matriz;
	}		
}


