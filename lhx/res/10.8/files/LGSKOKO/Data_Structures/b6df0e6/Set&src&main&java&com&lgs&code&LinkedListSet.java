package com.lgs.code;

import java.util.ArrayList;

/**
 * @author ：李先生
 * @date ：Created in 2019/9/4 11:08
 * @description：基于链表实现的Set集合类
 * @modified By：
 * @version: $
 */
public class LinkedListSet<E> implements Set<E> {

    private LinkedList<E> list;

    //构造函数
    public LinkedListSet(){
        list = new LinkedList<>();
    }
    @Override
    public void add(E e) {
        if(!list.contains(e))
            list.addFirst(e);

    }

    @Override
    public void remove(E e) {
        list.removeElement(e);
    }

    @Override
    public boolean contains(E e) {
        return list.contains(e);
    }

    @Override
    public int getSize() {
        return list.getSize();
    }

    @Override
    public boolean isEmpty() {
        return list.isEmpty();
    }


}
