package com.lgs.code;

import java.util.Arrays;

/**
 * @author ：李先生
 * @date ：Created in 2019/8/6 10:54
 * @description：二次封装数组，添加增、删、改、查等相关方法
 * @modified By：
 * @version: $
 */
public class Array02 {

    private int[] data;//数组
    private int size;//数组个数

    /**
     * 有参构造函数 创建指定大小的数组
     * @param capacity  数组容量
     */
    public Array02(int capacity){
        data = new int[capacity]; //开辟内存空间
        size = 0;//数组个数为0
    }

    /**
     * 无参构造函数
     * 默认创建大小为10的数组
     */
    public Array02(){
        //调用有参构造函数的方法
        this(10);
    }
    //==========================基本操作==========================
     // size 获取当前数组元素个数
    public int getSize() {
        return size;
    }

      //获取数组的容量
    public int getCapacity(){
        return data.length;
    }

    //判断数组是否为空
    public boolean isEmpty(){
        return size == 0;
    }

    //==========================添加操作==========================

    //在数组末尾后面添加一个新元素 1.0版
   /* public void addLast(int e){
        //判断数组是否已满
        if(size == data.length)
            throw new IllegalArgumentException("addLast is  failed");

        data[size] = e; //添加元素 因为索引是0开始
        size++;//数组元素大小自增

        // data[size++] = e; //可使用这句话达到上面两句的效果
    }*/

   //在数组末尾添加一个新元素  e:插入元素
    public void addLast(int e){
        //通过代码复用实现
        add(size,e);
    }

    //在数组前面添加一个新元素 e:插入元素
    public void addFirst(int e){
        //通过代码复用实现
        add(0,e);
    }

    //在数组指第index位置添加一个新元素 index:指定位置 e:插入元素
    public void add(int index,int e)
    {
        //判断数组是否已满
        if(size == data.length)
            throw new IllegalArgumentException("addLast is  failed");

        //判断输入的位置是否合法
        if(index<0 || index>size)
            throw new IllegalArgumentException("add is failed,require 0<=index<=length");
        //将包括index在内的之后的数值都往后移 直接通过覆盖实现
        for (int i = data.length - 1; i >=size; i--)
            data[i+1] = data[i];

        data[size] = e;
        size++;
    }
    //==========================查询操作==========================
    //获取index位置的元素
    public int get(int index){
        if(index < 0 || index>=size)
            throw new IllegalArgumentException("get is failed,index is illegal");
         return data[index];
    }

    //==========================修改操作==========================
    //修改index位置的元素
    public void set(int index,int e){
        if(index<0 || index>=size)
            throw new IllegalArgumentException("set is failed,index is illegal");
        data[index] = e;
    }

    @Override
    public String toString() {
        StringBuilder res = new StringBuilder();
        res.append(String.format("Array:size = %d,capacity = %d\n"),size,data.length);
        res.append("[");
        for (int i = 0; i < size; i++) {
            res.append(data[i]);
            if (i != size-1)
                res.append(",");
        }
        res.append("]");
        return  res.toString();
    }
}
