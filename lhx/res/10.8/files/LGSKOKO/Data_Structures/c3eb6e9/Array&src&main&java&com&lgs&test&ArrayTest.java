package com.lgs.test;

import com.lgs.code.Array01;
import com.lgs.code.Array02;
import com.lgs.code.Array03;
import org.junit.jupiter.api.Test;

/**
 * @author ：李先生
 * @date ：Created in 2019/8/7 15:24
 * @description：Array的测试类
 * @modified By：
 * @version: $
 */
public class ArrayTest {

    //Array01类的测试方法
    @Test
    public void arr01(){
        Array01 arr01 = new Array01();
        arr01.use1();
        arr01.use2();
    }

    //Array02类的测试方法
    @Test
    public void array02(){
        //创建容量为20的数组
        Array02 arr02 = new Array02(20);
        //给数组赋值
        for (int i = 0;i <10;i++ )
            arr02.addLast(i);
        System.out.println(arr02);
        //在指定位置 添加元素
        arr02.add(1,100);
        System.out.println(arr02);
        //在数组最前面添加元素
        arr02.addFirst(-1);
        System.out.println(arr02);
        //删除指定位置的元素
        arr02.remove(2);
        System.out.println(arr02);
        //删除指定值
        arr02.removeElement(4);
        System.out.println(arr02);
        //删除数组最前面的元素
        arr02.removeFirst();
        System.out.println(arr02);
    }

    @Test
    //Array03类的测试方法
    public void array03(){
        //创建容量为20的数组
        Array03<Integer> arr03 = new Array03<Integer>(20);
        //给数组赋值
        for (int i = 0;i <10;i++ )
            arr03.addLast(i);
        System.out.println(arr03);
        //在指定位置 添加元素
        arr03.add(1,100);
        System.out.println(arr03);
        //在数组最前面添加元素
        arr03.addFirst(-1);
        System.out.println(arr03);
        //删除指定位置的元素
        arr03.remove(2);
        System.out.println(arr03);
        //删除指定值
        arr03.removeElement(4);
        System.out.println(arr03);
        //删除数组最前面的元素
        arr03.removeFirst();
        System.out.println(arr03);
    }
}
