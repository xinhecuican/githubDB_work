package com.lgs.code;

/**
 * @author ：李先生
 * @date ：Created in 2019/8/10 16:33
 * @description：用动态数组来实现的栈 Stack接口的实现类
 * @modified By：
 * @version: $
 */
public class ArrayStack<E> implements Stack<E>{

    //这里array的类型是 我们自己编写的动态数组
    Array<E> array ;

    //无参构造函数  创建默认大小为10的动态数组
    public ArrayStack(){
        this.array = new Array<>();
    }

    //有参构造函数 创建容量为capacity的动态数组
    public ArrayStack(int capacity){
        this.array = new Array<>(capacity);
    }

    //获取栈里面的元素个数
    @Override
    public int getSize() {
        return array.getSize();
    }

    //判断栈是否为空
    @Override
    public boolean isEmpty() {
        return array.isEmpty();
    }

    //进行入栈操作
    @Override
    public void push(E e) {
        array.addLast(e);
    }

    //进行出栈操作
    @Override
    public E pop() {
        return array.removeLast();
    }

    //查看栈顶元素
    @Override
    public E top() {
        return array.getLast();
    }

    //查看栈容量大小 特有方法
    public int getCapacity(){
        return array.getCapacity();
    }

    @Override
    public String toString() {
        StringBuilder res = new StringBuilder();
        res.append("Stack: ");
        res.append('[');
        for (int i=0; i<array.getSize();i++){
            res.append(array.get(i));
            if(i != array.getSize()-1)
                res.append(',');
        }
        res.append("] top");
        return res.toString();
    }
}
