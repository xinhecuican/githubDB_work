package com.lgs.test;

import com.lgs.code.BSTMap;
import com.lgs.code.FileOperation;

import java.util.ArrayList;

/**
 * @author ：李先生
 * @date ：Created in 2019/9/8 9:36
 * @description：基于二分搜索树实现的Map的测试类
 * @modified By：
 * @version: $
 */
public class BSTMapTest {

    public static void main(String[] args){

        System.out.println("Pride and Prejudice");

        ArrayList<String> words = new ArrayList<>();
        if(FileOperation.readFile("Map/src/main/pride-and-prejudice.txt", words)) {
            System.out.println("Total words: " + words.size());

            BSTMap<String, Integer> map = new BSTMap<>();
            for (String word : words) {
                if (map.contains(word))
                    map.set(word, map.get(word) + 1);
                else
                    map.add(word, 1);
            }

            System.out.println("Total different words: " + map.getSize());
            System.out.println("Frequency of PRIDE: " + map.get("pride"));
            System.out.println("Frequency of PREJUDICE: " + map.get("prejudice"));
        }

        System.out.println();
    }
}
