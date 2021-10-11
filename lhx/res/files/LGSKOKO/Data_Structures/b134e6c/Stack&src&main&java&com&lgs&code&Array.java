package com.lgs.code;

/**
 * @author ：李先生
 * @date ：Created in 2019/8/7 17:10
 * @description：在Array03类的基础上改进为动态数组
 * 这里作为栈实现的一部分引用 ：动态数组栈
 * @modified By：
 * @version: $
 */
public class Array<E> {

    private E[] data;//数组
    private int size;//数组个数

    /**
     * 有参构造函数 创建指定大小的数组
     * @param capacity  数组容量
     */
    public Array(int capacity){
        //data = new int[capacity]; //开辟内存空间
        //由于我们使用的是泛型 所以这里 先new 一个类型为Object容量为capacity的数组 在将其转化为
        data = (E[])new Object[capacity];
        size = 0;//数组个数为0
    }

    /**
     * 无参构造函数
     * 默认创建大小为10的数组
     */
    public Array(){
        //调用有参构造函数的方法
        this(10);
    }
    //==========================实现动态数组操作==========================
    //扩容、缩容方法
    public void resize(int capacity){
        E[] newdata = (E[])new Object[capacity];
        for (int i = 0; i < size; i++)
            newdata[i] = data[i];
        data = newdata;//将data指向newdata的引用
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
    public void addLast(E e){
        //通过代码复用实现
        add(size,e);
    }

    //在数组前面添加一个新元素 e:插入元素
    public void addFirst(E e){
        //通过代码复用实现
        add(0,e);
    }

    //在数组指第index位置添加一个新元素 index:指定位置 e:插入元素
    public void add(int index,E e)
    {

        //判断输入的位置是否合法
        if(index<0 || index>size)
            throw new IllegalArgumentException("add is failed,require 0<=index<=length");

        //判断数组是否已满 若是已满进行扩容操作
        if(size == data.length)
            resize(2*data.length); //扩容操作 最好保持扩容后的长度 和 原先的数组长度是一样的数量级

        //将包括index在内的之后的数值都往后移 直接通过覆盖实现
        for (int i = size-1; i >=index; i--)
            data[i+1] = data[i];

        data[index] = e;
        size++;
    }
    //获取最后一个元素值
    public E getLast(){
        //代码复用
        return get(size-1);
    }
    //获取第一个元素值
    public E getFirst(){
        //代码复用
        return get(0);
    }

    //==========================删除操作==========================
    //从数组中删除index位置的元素，返回删除的元素
    public E remove(int index){

        //判断输入的位置是否合法
        if(index<0 || index>=size)
            throw new IllegalArgumentException("remove is failed,index is illegal");

        //判断是否需要进行缩容操作
        if(size == data.length/2)
            resize(data.length/2);//缩容操作 最好保持缩容后的长度 和 原先的数组长度是一样的数量级

        E ret = data[index];//用来暂存index位置的数据
        for (int i = index+1; i < size; i++) {
            data[i-1] = data[i];
        }
        size--;
        return ret;
    }

    //删除数组第一个元素
    public E removeFirst(){

        return remove(0);
    }

    //删除数组最后一个元素
    public E removeLast(){
        return remove(size-1);
    }

    //从数组中删除指定元素e
    public void removeElement(E e){
        int index = find(e);
        if(index != -1)
            remove(index);
    }

    //==========================修改操作==========================
    //修改index位置的元素
    public void set(int index,E e){
        if(index<0 || index>=size)
            throw new IllegalArgumentException("set is failed,index is illegal");
        data[index] = e;
    }


    //==========================查询操作==========================
    //获取index位置的元素
    public E get(int index){
        if(index < 0 || index>=size)
            throw new IllegalArgumentException("get is failed,index is illegal");
        return data[index];
    }

    //查找数组中是否有元素e
    public boolean contain(E e){

        for (int i = 0; i < data.length; i++) {
            //这里我们使用equal比较合适 我们只进行值的比较
            if(data[i].equals(e))
                return true;
        }
        return false;
    }

    //查找数组中元素e所在的索引，如果不存在元素e，则返回-1
    public int find(E e){

        for (int i = 0; i < data.length; i++) {
            //这里我们使用equal比较合适 我们只进行值的比较
            if(data[i].equals(e))
                return i;
        }
        return -1;
    }

    @Override
    public String toString() {
        StringBuilder res = new StringBuilder();
        res.append(String.format("Array:size = %d,capacity = %d\n",size,data.length));
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
