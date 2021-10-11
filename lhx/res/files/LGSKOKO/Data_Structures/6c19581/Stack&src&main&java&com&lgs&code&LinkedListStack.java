package com.lgs.code;

/**
 * @author ：李先生
 * @date ：Created in 2019/8/16 9:03
 * @description：基于链表实现的栈
 * @modified By：
 * @version: $
 */
public class LinkedListStack<E> implements Stack<E> {

    private LinkedList linkedStack ;

    public LinkedListStack(){
        linkedStack = new LinkedList<Integer>();
    }
    @Override
    public int getSize() {
        return linkedStack.getSize();
    }

    @Override
    public boolean isEmpty() {
        return linkedStack.isEmpty();
    }

    @Override
    public void push(E e) {
        //因为我们自己编写的链表的插入 使用的是头插法 所以这里要addFirst
        linkedStack.addFirst(e);
    }

    @Override
    public E pop() {
        //因为我们自己编写的链表的插入 使用的是头插法 所以这里要removeFirst
        return (E) linkedStack.removeFirst();
    }

    @Override
    public E top() {
        //因为我们自己编写的链表的插入 使用的是头插法 所以这里要getFirst
        return (E) linkedStack.getFirst();
    }

    @Override
    public String toString() {
        StringBuilder res = new StringBuilder();
        res.append("Stack: top ");
        res.append(linkedStack);
        return res.toString();
    }
}
