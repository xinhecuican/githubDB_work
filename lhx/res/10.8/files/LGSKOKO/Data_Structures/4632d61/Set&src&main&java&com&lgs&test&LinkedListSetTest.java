package com.lgs.test;

import com.lgs.code.FileOperation;
import com.lgs.code.LinkedListSet;

import java.util.ArrayList;

/**
 * @author ：李先生
 * @date ：Created in 2019/9/4 11:20
 * @description：基于链表实现的Set集合类的测试类
 * @modified By：
 * @version: $
 */
public class LinkedListSetTest {

    public static void main(String[] args) {

        System.out.println("Pride and Prejudice");

        ArrayList<String> words1 = new ArrayList<>();
        if(FileOperation.readFile("Set/src/main/pride-and-prejudice.txt", words1)) {
            System.out.println("Total words: " + words1.size());

            LinkedListSet<String> set1 = new LinkedListSet<>();
            for (String word : words1)
                set1.add(word);
            System.out.println("Total different words: " + set1.getSize());
        }

        System.out.println();


        System.out.println("A Tale of Two Cities");

        ArrayList<String> words2 = new ArrayList<>();
        if(FileOperation.readFile("Set/src/main/a-tale-of-two-cities.txt", words2)){
            System.out.println("Total words: " + words2.size());

            LinkedListSet<String> set2 = new LinkedListSet<>();
            for(String word: words2)
                set2.add(word);
            System.out.println("Total different words: " + set2.getSize());
        }
    }
}
