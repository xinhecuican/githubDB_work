package com.lgs.test;

import com.lgs.code.ArrayQueue;

/**
 * @author ：李先生
 * @date ：Created in 2019/8/11 14:23
 * @description：基于动态数组创建的队列的测试类
 * @modified By：
 * @version: $
 */
public class ArrayQueueTest {
    public static void main(String[] args) {

        ArrayQueue<Integer> queue = new ArrayQueue<>();
        for (int i = 0; i < 10; i++) {
            queue.enqueue(i);
            System.out.println(queue);

            //每插入三个元素 进行一次出队 因为这里下标是0开始
            if(i%3 == 2){
                queue.dequeue();
                System.out.println(queue);
            }//end if
        }//end for i
    }//end main

}
