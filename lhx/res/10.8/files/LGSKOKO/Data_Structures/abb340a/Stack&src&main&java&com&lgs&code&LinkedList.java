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

//    private Node head;//头指针 1.0版
    private Node dummyHead;//头节点 不存值
    private int size;//记录当前链表的元素个数

    //构造函数 初始化链表
    public LinkedList(){
//        head = null; //1.0
        dummyHead = new Node(null,null);
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


    //在链表中间添加新的元素e
    //在链表中不是一个常用的操作，练习用
    public void add(int index,E e){
        //判断输入的index是否合法
        if(index<0 || index>size)
            throw new IllegalArgumentException("Add Failed .Illegal index");

       /* if(index == 0)      //1.0版
            addFirst(e);
        else{
            Node prev = head;
            //找到插入位置的前一个结点 默认下标和数组一样从0开始
            for (int i = 0; i < index-1; i++) {
                prev = prev.next;
            }//end for i
        */

        Node prev = dummyHead;
        //找到插入位置的前一个结点 这里因为加了一个不存值的头节点 所以 i<index
        for (int i = 0; i < index; i++)
             prev = prev.next;
//      Node node = new Node(e);
//      node.next = prev.next;
//      prev.next = node;

        prev.next = new Node(e,prev.next); //这句话起到了和上面三句话一样的效果
        size++;

    }//end method add

    //在表头添加新的元素e  1.0版
//    public void addFirst(E e){
////        Node node = new Node(e);
////        node.next = head;
////        head = node;
//        //这句话能够实现上面三句话一样的效果
//        head = new Node(e,head);
//        size++;
//    }//end method addFirst

    //在报表头添加新的元素e
    public void  addFirst(E e){
        add(0,e);//代码复用
    }


    //在链表的末尾添加新的元素e
    public void addLast(E e){
        add(size,e); //代码复用
    }

    //获得链表的第index(0-based）个位置的元素
    //在链表中不是一个常用的操作，练习用
    public E get(int index){
        if(index<0 || index>=size)
            throw new IllegalArgumentException("Get Failed .Illegal index");
        Node cur = dummyHead.next;//指向首元结点
        for (int i = 0; i < index; i++)
            cur = cur.next;

        return cur.e;
    }

    //获取第一个元素
    public void getFirst(){
        get(0);
    }

    //获取最后一个元素
    public void getLast(){
        get(size-1);
    }

    //修改链表的第index个位置的元素为e
    //在链表中不是很常用的操作，练习用
    public void set(int index,E e){
        if(index<0 || index>=size)
            throw new IllegalArgumentException("set Failed .Illegal index");
        Node cur = dummyHead.next; //指向首元结点
        for (int i = 0; i < index; i++)
            cur = cur.next;//指向下一个结点
        cur.e = e;
    }

    //查找链表中是否存在元素e
    public boolean contains(E e){
        Node cur = dummyHead.next;//指向首元结点
        //循环遍历
        while (cur != null){
            if(cur.e.equals(e))
                return true;
            cur = cur.next;//指向下一个结点
        }
        //如果遍历完这个链表还没有返回true的话 代表没找到
        return false;
    }

    @Override
    public String toString(){
        StringBuilder res = new StringBuilder();

        Node cur = dummyHead.next;//指向首元结点
        //进行循环遍历
        while(cur != null){
            res.append(cur+"->");
            cur = cur.next;
        }
        res.append("NULL");//这里是虚拟头结点
        return  res.toString();
    }

    //从链表中删除index位置的元素，返回删除的元素
    public E remove(int index){
        if(index<0 || index>=size)
            throw new IllegalArgumentException("remove Failed .Illegal index");

        Node prev = dummyHead;
        for (int i = 0; i < index; i++)
            prev = prev.next;

        //实现删除具体逻辑
        Node retNode = prev.next;
        prev.next = retNode.next;
        retNode.next = null;//释放资源 为了JVM更好回收资源
        size--;

        return retNode.e;
    }

    //删除第一个元素
    public E removeFirst(){
        return remove(0);
    }
    //删除最后一个元素
    public E removeLast(){
        return remove(size-1);//
    }


}
