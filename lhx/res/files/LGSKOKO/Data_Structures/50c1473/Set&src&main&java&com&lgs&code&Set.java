package com.lgs.code;

/**
 * @author ：李先生
 * @date ：Created in 2019/9/3 15:17
 * @description：有关于Set(集合)的接口
 * @modified By：
 * @version: $
 */
public interface Set<E> {

    void add(E e);//添加元素
    void remove(E e);//删除元素
    boolean contains(E e);//是否有某个元素
    int getSize();//获得当前集合有多少个元素
    boolean isEmpty();//判断是否为空
}
