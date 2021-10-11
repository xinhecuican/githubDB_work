package com.lgs.code;

import sun.invoke.empty.Empty;

import java.util.Arrays;

/**
 * @author ：李先生
 * @date ：Created in 2019/8/12 21:00
 * @description：循环队列
 * @modified By：
 * @version: $
 */
public class LoopQueue<E> implements Queue<E> {

    private E[] data;
    private int front,tail;//头指针 尾指针
    private int size;

    //有参构造函数
    public LoopQueue(int capacity){
        data = (E[])new Object[capacity+1];
    }

    //无参构造函数 代码复用
    public LoopQueue(){
        this(10);
    }
    public int getCapacity(){
        return data.length-1;
    }
    @Override
    public int getSize() {
        return size;
    }

    @Override
    public boolean isEmpty() {
        return front == tail;
    }

    public void enqueue(E e){
        if((tail+1)%data.length == front)
            resize(getCapacity()*2);//进行扩容操作
         data[tail] = e;
         tail = (tail+1) % data.length;
         size++;
    }

    @Override
    public E dequeue() {
        if(isEmpty())
            throw new IllegalArgumentException("The LoopQueue is empty");
        E ret = data[front];
        data[front] = null;
        front = (front+1)% data.length;//重新指定front大小
        size--;//当前队列元素个数减一
        if(size == getCapacity()/4 && getCapacity()/2 !=0)
            resize(getCapacity()/2);//进行缩容操作
        return ret;
    }

    @Override
    public E getFront() {
            if(isEmpty())
                throw new IllegalArgumentException("Queue is empty");
        return data[front];
    }

    private void resize(int newCapacity){

        E[] newData = (E[]) new Object[newCapacity+1];
        for (int i = 0; i < size; i++) {
            newData[i] = data[(i + front) % data.length];
        data = newData;
        front = 0;
        tail = size;
        }
    }

    @Override
    public String toString() {

        StringBuilder res = new StringBuilder();
        res.append(String.format("Queue: size = %d , capacity = %d\n", size, getCapacity()));
        res.append("front [");
        for(int i = front ; i != tail ; i = (i + 1) % data.length){
            res.append(data[i]);
            if((i + 1) % data.length != tail)
                res.append(", ");
        }
        res.append("] tail");
        return res.toString();
    }
}
