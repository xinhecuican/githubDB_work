package com.lgs.code;

/**
 * @author ：李先生
 * @date ：Created in 2019/8/11 14:04
 * @description：用动态数组实现的队列
 * @modified By：
 * @version: $
 */
public class ArrayQueue<E> implements Queue {

    private Array<E> array;

    //无参构造函数  创建默认大小为10的动态数组
    public ArrayQueue(){
        this.array = new Array<>();
    }

    //有参构造函数 创建容量为capacity的动态数组
    public ArrayQueue(int capacity) {
        this.array = new Array<>(capacity);
    }
    //获取队列里面的元素个数
    @Override
    public int getSize() {
        return array.getSize();
    }
    //判断是否为队空
    @Override
    public boolean isEmpty() {
        return array.isEmpty();
    }

    //入队操作
    public void enqueue(E e){
        array.addFirst(e);
    }
    //出队操作
    @Override
    public Object dequeue() {
        return array.removeLast();
    }
    //获得队首元素
    @Override
    public Object getFront() {
        return array.getFirst();
    }

    //获得队列的容量
    public int getCapacity(){
        return  array.getCapacity();
    }

    @Override
    public String toString() {
        StringBuilder res = new StringBuilder();
        res.append("Queue: ");
        res.append("front[");
        for (int i=0; i<array.getSize();i++){
            res.append(array.get(i));
            if(i != array.getSize()-1)
                res.append(',');
        }
        res.append("] tail");
        return res.toString();
    }
}
