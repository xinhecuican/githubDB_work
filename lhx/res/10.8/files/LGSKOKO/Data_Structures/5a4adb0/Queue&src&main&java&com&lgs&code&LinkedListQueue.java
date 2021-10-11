package com.lgs.code;

/**
 * @author ：李先生
 * @date ：Created in 2019/8/16 10:17
 * @description：使用带有尾指针的链表 实现队列
 * @modified By：
 * @version: $
 */
public class LinkedListQueue<E> implements Queue<E> {
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

    private  Node head,tail;//头结点 尾结点
    private int size;//记录大小
    //构造函数
    public LinkedListQueue(){
        head = null;
        tail = null;
        size = 0;
    }
    @Override
    public int getSize() {
        return size;
    }

    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    public void enqueue(E e){
        //先判断尾是否为空
        if (tail == null) {
            tail = new Node(e);
            head = tail;
        }else{
            tail.next = new Node(e);
            tail = tail.next;
        }
        size++;
    }

    @Override
    public E dequeue() {
        //判断是否为队空
        if(isEmpty())
            throw new IllegalArgumentException("Can not dequeue");

        Node retNode = head;
        head = head.next;
        retNode.next = null;//将ret从链表中断开
        //判断此时head是否为空 因为可能有当前队列中只有一个元素的情况
        if(head == null)
            tail = null;
        size--;
        return retNode.e;
    }

    @Override
    public E getFront() {
        //判断是否为队空
        if(isEmpty())
            throw new IllegalArgumentException("Can not dequeue");
        return head.e;
    }

    @Override
    public String toString(){
        StringBuilder res = new StringBuilder();
        res.append("Queue: front ");

        Node cur = head;
        while(cur != null) {
            res.append(cur + "->");
            cur = cur.next;
        }
        res.append("NULL tail");
        return res.toString();
    }
}
