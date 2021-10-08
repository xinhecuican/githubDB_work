package com.lgs.test;

import com.lgs.code.ArrayStack;

/**
 * @author ：李先生
 * @date ：Created in 2019/8/10 16:52
 * @description：用动态数组实现栈的测试类
 * @modified By：
 * @version: $
 */
public class ArrayStackTest {

    public static void main(String[] args) {

        ArrayStack<Integer> arrayStack = new ArrayStack<>();
        //用for循环进行 入栈操作
        for(int i=0;i<5;i++)
        {
            arrayStack.push(i);
            System.out.println(arrayStack);
        }
        //进行出栈操作
        arrayStack.pop();
        System.out.println(arrayStack);

    }
}
