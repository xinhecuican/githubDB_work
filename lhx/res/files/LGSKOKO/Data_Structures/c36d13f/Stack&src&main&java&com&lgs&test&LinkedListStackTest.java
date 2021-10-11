package com.lgs.test;

import com.lgs.code.ArrayStack;
import com.lgs.code.LinkedListStack;

/**
 * @author ：李先生
 * @date ：Created in 2019/8/16 9:19
 * @description：基于链表实现的栈 的测试类
 * @modified By：
 * @version: $
 */
public class LinkedListStackTest {
    public static void main(String[] args) {
        LinkedListStack<Integer> linkedStack = new LinkedListStack<>();
        //用for循环进行 入栈操作
        for(int i=0;i<5;i++)
        {
            linkedStack.push(i);
            System.out.println(linkedStack);
        }
        //进行出栈操作
        linkedStack.pop();
        System.out.println(linkedStack);
    }
}
