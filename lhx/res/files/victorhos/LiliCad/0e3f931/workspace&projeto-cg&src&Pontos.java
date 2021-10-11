/*
-----------------------------------------------------------------------------
--
--  Class: Pontos
--
--  
--
--  Date    Sign		History
--  ------	----		--------------------------------------------------------
--  101113	Lucas   	Criação
-----------------------------------------------------------------------------
*/

public class Pontos 
{
	private double x;
	private double y;
	private double pontoImaginario;
	
	Pontos()
	{
		this.x = 0.0;
		this.y = 0.0;
		this.pontoImaginario = 1.0;
	}

	public double getX() 
	{
		return x;
	}

	public void setX(double x) 
	{
		this.x = x;
	}

	public double getY() 
	{
		return y;
	}

	public void setY(double y) 
	{
		this.y = y;
	}
	
	public double getpontoImaginario()
	{
		return this.pontoImaginario;
	}
}
