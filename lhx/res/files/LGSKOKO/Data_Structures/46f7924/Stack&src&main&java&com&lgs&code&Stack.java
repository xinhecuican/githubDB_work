package com.lgs.code;

/**
 * 泛型栈的接口
 */
public interface Stack<E> {


    int getSize();//获取栈的里面数据元素个数
    boolean isEmpty();//判断栈是否为空
    void push(E e);//入栈操作
    E pop();//出栈操作
    E top();//查看栈顶元素

}
