package 第二章.例2;

public class BasicMath {

	public static void basic(){
		
		byte b1=1;     //一般byte类型只在输入输出流，及文件读写中，现实中没有byte类型,这里是为了举例
		byte b2=2;
		byte b3=b1+b2; //现实中没有byte类型,两个byte类型相加最低位int整型，这里将b3设置为int类型即可。
						//+号是给现实中int类型准备的，字节类型自动升格为int类型，不能缩小范围后赋值
						//不能削足适履
	    byte b4=3+2;   //没有升格问题
	    byte b5=2+b1;  //b1升格为int类型 削足适履
	    long m2=2L;    //long为长整型
	    int i1=m2+b1; //m2是长整型，b1自动升格为长整型 削足适履
	    int i2=2L+3;  //3自动升格为长整型 削足适履
	    long m3=m2+b1;
	    float z3=2.0f+3.0; //3.0是默认的double型 2.0f自动升格为double类型 相加结果为double型 削足适履
	    double z4=2.0f+3.0;
	}
	public static void main(String[] args) {
		

	}

}
