package com.lgs.code;

/**
 * Queue（队列）接口
 * @param <E>
 */
public interface Queue<E> {

    int getSize();    //获取队列里面的元素个数
    boolean isEmpty();    //判断是否为队空
    //void enqueue(E e);//进行入队操作
    E dequeue();//出队操作
    E getFront();//获得队首元素


}
