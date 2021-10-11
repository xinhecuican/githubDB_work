package com.lgs.test;

import com.lgs.code.LinkedList;
import org.jcp.xml.dsig.internal.dom.DOMDigestMethod;

/**
 * @author ：李先生
 * @date ：Created in 2019/8/15 19:12
 * @description：链表测试类
 * @modified By：
 * @version: $
 */
public class LinkedListTest  {
    public static void main(String[] args) {
        LinkedList<Integer> linkedList = new LinkedList<>();
        for (int i = 0; i < 5; i++) {
            linkedList.addFirst(i);
            System.out.println(linkedList);
        }
        linkedList.add(2,666);
        System.out.println(linkedList);

        linkedList.remove(2);
        System.out.println(linkedList);

        linkedList.removeFirst();
        System.out.println(linkedList);

        linkedList.removeLast();
        System.out.println(linkedList);
    }
}
