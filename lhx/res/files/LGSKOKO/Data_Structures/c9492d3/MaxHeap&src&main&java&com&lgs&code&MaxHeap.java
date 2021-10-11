package com.lgs.code;

/**
 * @author ：李先生
 * @date ：Created in 2019/9/8 11:15
 * @description：基于动态数组实现的MaxHeap(大根堆)的实现类
 * @modified By：
 * @version: $
 */
public class MaxHeap<E extends Comparable<E>> {
    private Array<E> data;
    //构造函数 capacity：数组的容量
    public MaxHeap(int capacity){
        data = new Array<>(capacity);
    }

    //构造函数
    public MaxHeap(){
        data = new Array<>();
    }

    //返回堆中的元素个数
    public int size(){
        return data.getSize();
    }

    //返回一个布尔值，表示堆中是否为空
    public boolean isEmpty(){
        return data.isEmpty();
    }

    //返回完全二叉树的数组表示中，一个索引所表示的元素的父亲节点的索引
    private int parent(int index){
        if(index == 0)
            throw new IllegalArgumentException("index-0 doesn't have parent");
        return (index-1)/2;
    }
    //返回完全二叉树的数组表示中，一个索引所表示的元素的左孩子的索引
    private int leftChild(int index){
        return index*2 +1;
    }
    //返回完全二叉树的数组表示中，一个索引所表示的元素的右孩子的索引
    private int rightChild(int index){
        return index*2 + 2;
    }
}
