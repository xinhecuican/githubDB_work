package com.lgs.code;

/**
 * @author ：李先生
 * @date ：Created in 2019/9/3 15:20
 * @description：基于二分搜索树实现的Set(集合)
 * @modified By：
 * @version: $
 */
public class BSTSet<E extends Comparable<E>> implements Set<E>  {

    private BST<E> bst;

    //构造函数
    public BSTSet(){
        bst = new BST<>();
    }
    @Override
    public void add(E e) {
        bst.add(e);
    }

    @Override
    public void remove(E e) {
        bst.remove(e);
    }

    @Override
    public boolean contains(E e) {
        return bst.contains(e);
    }

    @Override
    public int getSize() {
        return bst.getSize();
    }

    @Override
    public boolean isEmpty() {
        return bst.isEmpty();
    }
}
