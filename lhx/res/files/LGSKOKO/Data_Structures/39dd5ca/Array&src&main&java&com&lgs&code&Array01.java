package com.lgs.code;

/**
 * @author ：李先生
 * @date ：Created in 2019/8/6 10:39
 * @description：在Java中使用数组
 * @modified By：
 * @version: $
 */
public class Array01 {

    /**
     * 第一种使用方法：在声明是指定其容量大小为20
     */
    public void use1(){
        int[] arr = new int[20];
        //这里可以通过快捷操作生成循环 arr.fori 生成
        for (int i = 0; i < arr.length; i++) {
            arr[i] = i;
            //快捷操作：sout 生成System.out.println();
            System.out.println(arr[i]);
        }
    }

    /**
     * 第二种使用方法：可以在声明的时候并直接赋值，这里score数组的大小为3
     */
    public void use2(){
        int[] score = new int[]{60,80,100};
        //这里可以通过快捷操作生成循环 arr.fori 生成
        for (int i = 0; i < score.length; i++) {
            //快捷操作：sout 生成System.out.println();
            System.out.println(score[i]);
        }
    }
}
