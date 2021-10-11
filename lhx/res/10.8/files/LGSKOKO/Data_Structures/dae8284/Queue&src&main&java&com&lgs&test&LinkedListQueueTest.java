package com.lgs.test;

import com.lgs.code.LinkedListQueue;

/**
 * @author ：李先生
 * @date ：Created in 2019/8/16 10:36
 * @description：带尾指针的链表实现队列 的测试类
 * @modified By：
 * @version: $
 */
public class LinkedListQueueTest {
    public static void main(String[] args){

        LinkedListQueue<Integer> queue = new LinkedListQueue<>();
        for(int i = 0 ; i < 10 ; i ++){
            queue.enqueue(i);
            System.out.println(queue);

            if(i % 3 == 2){
                queue.dequeue();
                System.out.println(queue);
            }
        }
    }
}
