package 第八章.例6;

public class Buffer {        //仓库

	private char chBuffer;
	
	public synchronized void put(char ch){   //往仓库中放产品ch
		
		chBuffer = ch;                       //ch变成仓库中的chBuffer
	}
	
	public synchronized char get(){         
		
		char chr = chBuffer;                //从仓库中提取chBuffer给chr
		chBuffer ='\0';                     //仓库设置为空
		return chr;                         //将从仓库中提取的chr返回
	}
}
