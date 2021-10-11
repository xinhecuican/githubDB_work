package com.lgs.code;

/**
 * @author ：李先生
 * @date ：Created in 2019/9/5 17:46
 * @description：基于linkedList实现Map
 * @modified By：
 * @version: $
 */
public class LinkedListMap<K,V> implements Map<K,V> {

    //内部类 用来实现结点
    private class Node{
        private  K key;
        private V value;
        private Node next;
        public Node(K key,V value,Node next){
            this.key = key;
            this.value = value;
            this.next =  next;
        }
        public Node(K key){
            //直接调用上面写好的构造函数 this()
            this(key,null,null);
        }
        public Node(){this(null,null,null);}

        @Override
        public String toString() {
            return key.toString()+":"+value.toString();
        }
    }

    private Node dummyHead;//虚拟头结点
    private int size;

    //构造函数
    public LinkedListMap(){
        dummyHead = new Node();
        size = 0;
    }

    //通过传入参数K key来查找相应的结点
    public Node getNode(K key){
        Node cur = dummyHead.next;//将虚拟头结点指向下一个结点 即首元结点
        while(cur != null)
        {
            if(cur.key.equals(key)) //如果当前结点的key值等于传入的key则返回 当前结点
                return cur;
            cur = cur.next;
        }
        //如果没有查询到则返回null
        return null;
    }

    @Override
    public int getSize() {
        return size;
    }

    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    @Override
    public boolean contains(K key) {
        return getNode(key) != null;
    }

    @Override
    public V get(K key) {
        Node node = getNode(key);
        //这里用到了三元运算符 如果node为空 则返回空 否则返回node的value
        return node == null ? null : node.value;
    }

    @Override
    public void add(K key, V value) {

        Node node = getNode(key);
        if(node == null)
        {   //这里使用的是链表的头插法
            dummyHead.next = new Node(key,value,dummyHead.next);
            size++;
        }else //否则的话 就是存在结点 我这里使用的是覆盖的方法将其value值重新覆盖
            node.value = value;
    }

    @Override
    public void set(K key, V newValue) {

        Node node = getNode(key);
        if(node == null)
            throw new IllegalArgumentException(key+"doesn't exist!");
        node.value = newValue;
    }

    @Override
    public V remove(K key) {

        Node prev = dummyHead;
        while(prev.next != null){
            if(prev.next.key.equals(key))
                break;
            prev = prev.next;
        }

        if(prev.next != null){
            Node delNode = prev.next;
            prev.next = delNode.next;
            delNode.next = null;
            size --;
            return delNode.value;
        }
        return null;
    }






}
