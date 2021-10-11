package com.lgs.code;

/**
 * @author ：李先生
 * @date ：Created in 2019/8/13 9:49
 * @description：链表实现类
 * @modified By：
 * @version: $
 */
public class LinkedList<E> {

    //内部类用来实现结点
    private class Node{
        public E e;//泛型数据
        public Node next;//指向Node的引用 相当于指针

        public Node(E e ,Node next){
            this.e = e;
            this.next = next;
        }

        public Node(E e){
            this(e,null);
        }

        public Node(){
            this(null,null);
        }

        @Override
        public String toString() {
           return e.toString();
        }

    }//end class Node

    private Node head;//头指针
    private int size;//记录当前链表的元素个数

    //构造函数 初始化链表
    public LinkedList(){
        head = null;
        size = 0;
    }

    //获取链表中的元素个数
    public int getSize(){
        return size;
    }

    //判断链表是否为空
    public boolean isEmpty(){
        return  size ==0;
    }

    //在表头添加新的元素e
    public void addFirst(E e){
//        Node node = new Node(e);
//        node.next = head;
//        head = node;
        //这句话能够实现上面三句话一样的效果
        head = new Node(e,head);
        size++;
    }//end method addFirst

    //在链表中间添加新的元素e
    //在链表中不是一个常用的操作，练习用
    public void add(int index,E e){
        //判断输入的index是否合法
        if(index<0 || index>size)
            throw new IllegalArgumentException("Add Failed .Illegal index");
        if(index == 0)
            addFirst(e);
        else{
            Node prev = head;
            //找到插入位置的前一个结点 默认下标和数组一样从0开始
            for (int i = 0; i < index-1; i++) {
                prev = prev.next;
            }//end for i

//            Node node = new Node(e);
//            node.next = prev.next;
//            prev.next = node;
            //这句话起到了和上面三句话一样的效果
            prev.next = new Node(e,prev.next);
            size++;
        }
    }//end method add

    //在链表的末尾添加新的元素e
    public void addLast(E e){
        //代码复用
        add(size,e);
    }


}
