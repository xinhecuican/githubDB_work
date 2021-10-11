package 第三章.例4;

public interface Openning {

       void controlOpen(); //去掉 public 和abstract试试，没有错误出现，接口中的方法默认public和abstract
                          //这点和抽象类不同，抽象类中可以有非抽象方法和抽象方法，接口中只能有抽象方法
                           //抽象类中有的set，get方法不能有，与此同时，set，get方法对应的成员变量也不能有
                          //但可以有常量，定义一个变量试试，会出错，（（（（考试））））！！！！！！
       public final int i=1;
}